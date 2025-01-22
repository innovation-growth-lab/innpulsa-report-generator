"""Module to interact with the OpenAI API to generate content for a given report section."""

import asyncio
from typing import Union
import logfire
from openai import OpenAI
from .models import ReportSection, APIResponse
from .prompts_config import SYSTEM_PROMPT

client = OpenAI()


async def call_openai_api(
    section: ReportSection, prompt_template: str, model_name: str
) -> Union[APIResponse, None]:
    """Asynchronously call the OpenAI API to generate content for a given report section."""
    if section:
        variables_json = [
            {
                "variable": data.variable,
                "description": data.description,
                "value_before_intervention": data.value_initial_intervention,
                "value_after_intervention": data.value_final_intervention,
                "percentage_change": data.percentage_change,
            }
            for data in section.variables.values()
        ]

        prompt = prompt_template.format(variables=variables_json)
    else:
        prompt = prompt_template

    logfire.info(f"Calling OpenAI API with prompt: {prompt}")

    try:
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )

        generated_text = response.dict()["choices"][0]["message"]["content"]

        if response.dict()["choices"][0]["finish_reason"] == "length":
            logfire.warning(
                "The response was truncated due to reaching the maximum token limit."
            )

            # continue generating content
            continuation_response = await asyncio.to_thread(
                client.chat.completions.create,
                model=model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                    {"role": "system", "content": generated_text},
                    {"role": "user", "content": "Continue."},
                ],
                temperature=0.5,
            )

            continuation_text = continuation_response.dict()["choices"][0]["message"][
                "content"
            ]

            generated_text += continuation_text

        logfire.info("Received response from OpenAI API.")

        return APIResponse(
            status="success",
            message="Content generated successfully.",
            data={"content": generated_text},
        )

    except Exception as err:  # pylint: disable=broad-except
        logfire.error(f"An unexpected error occurred: {err}")
        return APIResponse(status="error", message=str(err))

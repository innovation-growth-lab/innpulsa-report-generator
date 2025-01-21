"""Module to interact with the OpenAI API to generate content for a given report section."""

import asyncio
from typing import Union
import logfire
from openai import OpenAI
from .models import ReportSection, APIResponse
from .prompts_config import SYSTEM_PROMPT

client = OpenAI()


async def call_openai_api(
    section: ReportSection, prompt_template: str
) -> Union[APIResponse, None]:
    """Asynchronously call the OpenAI API to generate content for a given report section."""
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
    logfire.info(f"Calling OpenAI API with prompt: {prompt}")

    try:
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model="gpt-3.5-turbo",  # Using the cheapest GPT model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1_000,
            temperature=0.5,
        )

        generated_text = response.dict()["choices"][0]["message"]["content"]
        logfire.info(f"Received response from OpenAI API: {generated_text}")

        return APIResponse(
            status="success",
            message="Content generated successfully.",
            data={"content": generated_text},
        )

    except Exception as err:  # pylint: disable=broad-except
        logfire.error(f"An unexpected error occurred: {err}")
        return APIResponse(status="error", message=str(err))

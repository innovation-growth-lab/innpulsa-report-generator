"""Module to interact with the OpenAI API to generate content for a given report section."""

import asyncio
from typing import Union
import logging
from openai import OpenAI
from .models import ReportSection, APIResponse
from .prompts_config import SYSTEM_PROMPT

logger = logging.getLogger(__name__)
client = OpenAI()


async def call_openai_api(
    section: ReportSection, prompt_template: str, model_name: str
) -> Union[APIResponse, None]:
    """Asynchronously call the OpenAI API to generate content for a given report section."""
    if section:
        logger.info("Calling OpenAI API for section: %s", section.title)
        
        # Join all interpretations from the section's variables
        combined_interpretation = "\n\n".join(
            data.interpretation 
            for data in section.variables.values()
        )
        
        prompt = prompt_template.format(interpretations=combined_interpretation)
    else:
        logger.info("Calling OpenAI API for no section")
        prompt = prompt_template

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
            logger.warning(
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
                    {"role": "user", "content": "Continua generando el contenido."},
                ],
                temperature=0.5,
            )

            continuation_text = continuation_response.dict()["choices"][0]["message"][
                "content"
            ]

            generated_text += continuation_text

        logger.info("Received response from OpenAI API.")

        return APIResponse(
            status="success",
            message="Content generated successfully.",
            data={"content": generated_text},
        )

    except Exception as err:  # pylint: disable=broad-except
        logger.error("An unexpected error occurred: %s", err)
        return APIResponse(status="error", message=str(err))

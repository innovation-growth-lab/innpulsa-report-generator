"""Module to interact with the Google Gemini API to generate content for a given report section."""

import asyncio
import os
from typing import Union
import logging
from google import genai
from ..models.sections import ReportSection, APIResponse
from ..config.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


async def call_gemini_api(
    section: Union[ReportSection, None], prompt_template: str, model_name: str
) -> Union[APIResponse, None]:
    """Async call the gemini api to generate content for a given report section."""

    if section:
        logger.info("Calling Gemini API for section: %s", section.title)

        # join all interpretations from the section's variables
        combined_interpretation = "\n\n".join(
            data.interpretation for data in section.variables.values()
        )

        prompt = prompt_template.format(interpretations=combined_interpretation)

    else:
        logger.info("Calling Gemini API for no section - likely executive summary")
        prompt = prompt_template

    try:
        # Combine system prompt and user prompt
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}"

        response = await asyncio.to_thread(
            client.models.generate_content, model=model_name, contents=full_prompt
        )

        generated_text = response.text

        logger.info("Received response from Gemini API.")

        return APIResponse(
            status="success",
            message="Content generated successfully.",
            data={"content": generated_text},
        )

    except Exception as err:  # pylint: disable=broad-except
        logger.error("An unexpected error occurred: %s", err)
        return APIResponse(status="error", message=str(err))

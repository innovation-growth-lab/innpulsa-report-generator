"""Asynchronous functions to generate content for the report sections using the OpenAI API."""

import asyncio
from typing import List
from src.models.sections import ReportSection
from src.services.openai_api import call_openai_api
from src.config.prompts import (
    executive_summary_prompt,
    final_edit_prompt,
    section_prompts,
)


async def generate_section_contents(
    sections: List[ReportSection], cohort_info: str, model_name: str, progress_bar=None
) -> None:
    """Generate content for each section asynchronously using the OpenAI API."""
    # Track sections that need processing
    sections_to_process = []
    tasks = []

    # Create tasks and track corresponding sections
    for section in sections:
        prompt_template = section_prompts.get(section.title)
        if prompt_template:
            sections_to_process.append(section)
            # Include cohort details in the prompt
            prompt_template = prompt_template.replace("{cohort_details}", cohort_info)
            task = asyncio.create_task(
                call_openai_api(section, prompt_template, model_name)
            )
            tasks.append(task)

    total_sections = len(tasks)
    if total_sections == 0:
        return

    if progress_bar:
        progress_bar.progress(
            0, f"Iniciando generación de {total_sections} secciones..."
        )

    # Process responses as they complete
    completed = 0
    pending = set(tasks)

    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

        for task in done:
            response = await task
            # Update the corresponding section
            section = sections_to_process[tasks.index(task)]
            section.content = (
                response.data.get("content", "Error generando el contenido.")
                if response and response.status == "success"
                else "Error generando el contenido."
            )

            completed += 1
            if progress_bar:
                progress_bar.progress(
                    completed / total_sections,
                    f"Completadas {completed} de {total_sections} secciones...",
                )


async def generate_executive_summary(
    contentful_sections: List[ReportSection], cohort_info: str, model_name: str
) -> str:
    """Generate an executive summary using the OpenAI API."""
    content = "\n".join(
        [f"{i+1}. {section.content}" for i, section in enumerate(contentful_sections)]
    )

    prompt_template = executive_summary_prompt.replace("{cohort_details}", cohort_info)
    prompt_template = prompt_template.replace("{sections_content}", content)

    response = await call_openai_api(None, prompt_template, model_name)

    return (
        response.data.get("content", "Error generando el contenido.")
        if response and response.status == "success"
        else "Error generando el contenido."
    )


async def edit_report_sections(
    sections: List[ReportSection], model_name: str, disable_api_call: bool = False
) -> str:
    """Edit the content of all sections for consistency and logical flow."""
    sections_content = "\n\n".join(
        [f"{section.title}\n{section.content}" for section in sections]
    )
    prompt = final_edit_prompt.format(sections_content=sections_content)

    if not disable_api_call:
        response = await call_openai_api(None, prompt, model_name)

        edited_content = (
            response.data.get("content", "Error editing content.")
            if response and response.status == "success"
            else "Error editing content."
        )
    else:
        edited_content = sections_content

    return edited_content

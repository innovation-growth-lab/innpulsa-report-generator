"""Asynchronous functions to generate content for the report sections using the OpenAI API."""

import asyncio
from typing import List
from src.models import ReportSection
from src.openai_api import call_openai_api
from src.prompts_config import (
    executive_summary_prompt,
    final_edit_prompt,
    section_prompts,
)


async def generate_section_contents(
    sections: List[ReportSection], cohort_info: str, model_name: str, progress_bar=None
) -> None:
    """Generate content for each section asynchronously using the OpenAI API."""
    tasks = []
    total_sections = len([s for s in sections if section_prompts.get(s.title)])
    completed = 0
    
    if progress_bar:
        progress_bar.progress(0, f"Iniciando generación de {total_sections} secciones...")

    for section in sections:
        prompt_template = section_prompts.get(section.title)
        if prompt_template:
            # Include cohort details in the prompt
            prompt_template = prompt_template.replace("{cohort_details}", cohort_info)
            tasks.append(call_openai_api(section, prompt_template, model_name))
    
    responses = []
    for task in asyncio.as_completed(tasks):
        response = await task
        responses.append(response)
        completed += 1
        if progress_bar:
            progress_bar.progress(
                completed / total_sections,
                f"Completadas {completed} de {total_sections} secciones..."
            )

    # Match responses back to sections
    for section, response in zip(sections, responses):
        section.content = (
            response.data.get("content", "Error generando el contenido.")
            if response and response.status == "success"
            else "Error generando el contenido."
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


async def edit_report_sections(sections: List[ReportSection]) -> str:
    """Edit the content of all sections for consistency and logical flow."""
    sections_content = "\n\n".join(
        [f"{section.title}\n{section.content}" for section in sections]
    )
    prompt = final_edit_prompt.format(sections_content=sections_content)

    response = await call_openai_api(None, prompt, "gpt-4o-2024-08-06")

    edited_content = (
        response.data.get("content", "Error editing content.")
        if response and response.status == "success"
        else "Error editing content."
    )

    return edited_content

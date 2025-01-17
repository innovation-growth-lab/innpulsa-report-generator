"""Application."""
import asyncio
from typing import List
import streamlit as st
from src.models import ReportSection
from src.openai_api import call_openai_api
from src.prompts_config import section_prompts
from src.sections_config import sections_config
from src.utils import load_data, aggregate_data, generate_json_output


async def generate_section_contents(sections: List[ReportSection]):
    """Generate content for each section asynchronously using the OpenAI API."""
    tasks = []
    for section in sections:
        prompt_template = section_prompts.get(section.title)
        if prompt_template:
            tasks.append(call_openai_api(section, prompt_template))
    responses = await asyncio.gather(*tasks)

    for section, response in zip(sections, responses):
        section.content = (
            response.data.get("content", "Error generating content.")
            if response and response.status == "success"
            else "Error generating content."
        )


# Streamlit UI
st.title("JSON Report Generator")

# File upload
uploaded_file = st.file_uploader("Upload your dataset (XLSX)", type="xlsx")
if uploaded_file is not None:
    # Load and cache the dataset
    df = load_data(uploaded_file)
    st.write(df)

    # Generate report
    if st.button("Generate Report"):
        report_sections = aggregate_data(df, sections_config)  # Aggregating data
        executive_summary = "This is a summary of the report, highlighting key findings and insights."  # Placeholder for actual summary generation

        # Generate content for each section asynchronously
        asyncio.run(generate_section_contents(report_sections))

        # Generate JSON output
        json_output = generate_json_output(report_sections, executive_summary)
        
        # Provide download link for JSON file
        st.download_button(
            label="Download JSON report",
            data=json_output,
            file_name="report.json",
            mime="application/json",
        )
        
        # Display JSON output in a collapsible box
        with st.expander("View JSON report"):
            st.json(json_output)
        
        st.success("JSON report generated!")

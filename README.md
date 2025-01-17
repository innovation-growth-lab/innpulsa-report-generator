# Innpulsa Report Generator

This project is a Streamlit application that generates a JSON report based on data from an uploaded Excel file. The report is divided into predefined sections, and the content for each section is generated using the OpenAI API.

## Features

- Upload an Excel file containing your dataset.
- Aggregate data into predefined sections.
- Generate content for each section using the OpenAI API.
- Download the generated JSON report.
- View the JSON report in a collapsible box within the Streamlit app.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/innpulsa-report-generator.git
    cd innpulsa-report-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    conda create --name .innpulsa python=3.13.1
    conda activate .innpulsa
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API key:
    ```sh
    export OPENAI_API_KEY='your-openai-api-key'  # On Windows, use `set OPENAI_API_KEY=your-openai-api-key`. In Linux, I use direnv.
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload your dataset (Excel file) using the file uploader.

4. Click the "Generate Report" button to generate the JSON report.

5. Download the generated JSON report or view it in the collapsible box.

## Project Structure

- `app.py`: Main Streamlit application file.
- `src/models.py`: Data models for the report sections and variables.
- `src/openai_api.py`: Module to interact with the OpenAI API.
- `src/prompts_config.py`: Configuration file for the prompts used to generate content.
- `src/sections_config.py`: Configuration file for the sections and their corresponding variables.
- `src/utils.py`: Utility functions for data loading, aggregation, and JSON output generation.

## Configuration

- `sections_config.py`: Define the variables to consider for each section.
- `prompts_config.py`: Define the prompts used to generate content for each section.

## Example

Here is an example of the `sections_config.py` file:

```python
sections_config = {
    "Productividad": ["productivity_before", "productivity_after"],
    "Talento humano": ["talent_before", "talent_after"],
    "Financiero": ["sales_before", "sales_after", "profits_before", "profits_after"],
    "Practicas gerenciales": ["management_practices_before", "management_practices_after"],
    "Asociatividad": ["associativity_before", "associativity_after"]
}
```

## License

This project is licensed under the MIT License.
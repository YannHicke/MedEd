# README

## Setup

Before you start, ensure that you have defined the following environment variables:

- `COHERE_API_KEY`
- `ANTHROPIC_API_KEY`
- `TOGETHER_API_KEY`
- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`

If you do not wish to use any of these APIs, set the corresponding environment variable to an empty string `""`.

## Running the Evaluation

1. **Navigate to the evaluation directory**:
   
   ```bash
   cd code/evaluation

2. **Run the evaluation script**:

    ```bash
    python score_chat2.py

This script will utilize the configuration file `config.yaml` located in the `code/evaluation` directory.

## Configuration

In the `config.yaml` file, you can customize the following settings:

- **Models to Run**: Specify which models you want to evaluate.
- **Evaluation Type**: Choose between `mirs` evaluation and `checklist` evaluation.
- **Case Selection**: Select the specific case you want to evaluate.
- **Prompt Usage**: Decide whether to use prompts with examples or without examples.
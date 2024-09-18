# README

## Setup

Before you start, ensure that you have defined the following environment variables:

- `ANTHROPIC_API_KEY`
- `FIREWORKS_API_KEY`
- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`

If you do not wish to use any of these APIs, set the corresponding environment variable to an empty string `""`.

## Running the Simulation

1. **Navigate to the simulation directory**:
   
   ```bash
   cd code/simulation
   ```

2. **Run the simulation script**:

   ```bash
   python patient_simulation.py <case_context>
   ```

   Replace `<case_context>` with the appropriate argument corresponding to the case file located in the context folder. For example:

   ```bash
   python patient_simulation.py context_palpitations
   ```

   This runs the simulation for the case specified in the `context_palpitations.txt` file located in the context folder.

## Running the Evaluation

1. **Navigate to the evaluation directory**:
   
   ```bash
   cd code/evaluation
   ```

2. **Run the evaluation script**:

   ```bash
   python score.py
   ```

   This script will utilize the configuration file `config.yaml` located in the `code/evaluation` directory.

## Configuration

In the `config.yaml` file, located in the setup folder, you can customize the following settings:

- **Conversation Files**: Specify the list of case files for evaluation.
  ```yaml
  conversation_files: ["case1.txt", "case2.txt", "case3.txt", "case4.txt", "dental1.txt", "dental2.txt", "dental3.txt", "behavioral1.txt", "behavioral2.txt", "behavioral3.txt"]
  ```

- **Model List**: List of models to evaluate.
  ```yaml
  model_list: ["openai"]
  ```

- **MIRS Evaluation**: Whether to use MIRS evaluation.
  ```yaml
  mirs: true
  ```

- **Prompt Examples**: Whether to include examples in prompts.
  ```yaml
  examples: false
  ```

- **Checklist Evaluation**: Whether to use checklist-based evaluation.
  ```yaml
  checklist: false
  ```

- **Extract Excerpts**: Set to false to avoid excerpt extraction.
  ```yaml
  extract_excerpts: false
  ```

- **Score from Excerpts**: Set to false to avoid scoring based on excerpts.
  ```yaml
  score_from_excerpts: false
  ```
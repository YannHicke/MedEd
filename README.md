# README

## Setup

To set up the project:

1. Navigate to the setup directory:
   ```bash
   cd setup
   ```

2. Run the setup script:
   ```bash
   python setup.py
   ```

This script will guide you through the process of setting up your API keys and other necessary configurations.

## Running the Simulation

1. **Navigate to the simulation directory**:
   
   ```bash
   cd code/simulation
   ```

2. **Run the simulation script**:

   ```bash
   python patient_simulation.py <case_context>
   ```

   Replace `<case_context>` with the appropriate argument corresponding to the case file located in the `code/simulation/context` folder. For example:

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

   This script will utilize the configuration file `config.yaml` located in the `setup` directory.

   When running the script, you will be prompted to choose which dataset to evaluate. The available datasets are located in the `data` folder.

## Configuration

In the `config.yaml` file, located in the `setup` folder, you can customize the following settings:

- **Conversation Files**: Specify the list of case files for evaluation. These files should be present in the `data/datasets` folder.
  ```yaml
  conversation_files: ["case1.txt", "case2.txt", "case3.txt", "case4.txt", "dental1.txt", "dental2.txt", "dental3.txt", "behavioral1.txt", "behavioral2.txt", "behavioral3.txt"]
  ```

- **Model List**: List of models to evaluate.
  ```yaml
  model_list: ["openai", "anthropic"]
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

These options are part of a multi-step evaluation process:

1. **Extract Excerpts**: When set to `true`, the system will extract relevant pieces of the transcript for each item in the evaluation rubric. This step helps focus on specific parts of the conversation that are relevant to each evaluation criterion.

2. **Score from Excerpts**: When set to `true`, the scoring will be based only on the extracted excerpts rather than the full transcript. This can help in more targeted and efficient scoring, especially for long conversations.

If you want to perform the full multi-step evaluation:
- Set both `extract_excerpts` and `score_from_excerpts` to `true`.

If you want to skip the excerpt extraction and score based on the full transcript:
- Set both `extract_excerpts` and `score_from_excerpts` to `false`.
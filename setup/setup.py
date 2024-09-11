import os
import subprocess
import sys


def run_command(command):
    """
    Utility function to run shell commands. 
    """
    process = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if process.returncode != 0:
        sys.exit(f"Error: Command '{command}' failed")


# Check if the Conda environment exists
def check_conda_env(env_name):
    result = subprocess.run(
        ["conda", "env", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if env_name in result.stdout:
        return True
    return False

# Remove the Conda environment
def remove_conda_env(env_name):
    print(f"Removing existing Conda environment '{env_name}'...")
    run_command(f"conda env remove -n {env_name}")
    print(f"Conda environment '{env_name}' removed successfully!")

# Step 1: Create Conda environment from environment.yml
def setup_conda_env():
    print("Setting up Conda environment...")

    if os.path.exists("environment.yml"):
        try:
            import yaml
        except ImportError:
            run_command("pip install pyyaml")
            import yaml

        # Load the environment.yml file
        with open(os.path.join("environment.yml"), "r") as f:
            env_config = yaml.safe_load(f)
        env_name = env_config.get("name", "default_env_name")  # Get the environment name

        # Check if the environment already exists
        if check_conda_env(env_name):
            choice = input(f"The environment '{env_name}' already exists. Do you want to remove it and create a new one? (y/n): ").strip().lower()
            if choice == "y":
                remove_conda_env(env_name)
                run_command(f"conda env create -f environment.yml")
                print(f"Conda environment '{env_name}' created successfully!")
                return env_name, True  # Return True to indicate a new environment was created
            else:
                print(f"Keeping existing Conda environment '{env_name}'. Skipping environment setup.")
                return env_name, False  # Return False to indicate the existing environment is kept

        run_command(f"conda env create -f environment.yml")
        print(f"Conda environment '{env_name}' created successfully!")
        return env_name, True  # Return True to indicate a new environment was created
    
    else:
        print("Error: environment.yml file not found. Are you in the setup directory?")
        sys.exit(1)


def install_requirements(env_name):
    """
    Install Python packages from the requirements.txt file in the Conda environment.
    """
    print(f"\nInstalling requirements in the Conda environment '{env_name}'...")
    if os.path.exists("requirements.txt"):
        run_command(f"conda run -n {env_name} pip install -r requirements.txt")
        print("Requirements installed successfully!")
    else:
        print("Error: requirements.txt file not found. Are you in the setup directory?")


def setup_api_keys():
    """
    Setup API keys for various services by adding them to the .env file.
    """
    print("\nSetting up API keys...\n")
    env_file = ".env"
    keys = {
        "OPENAI_API_KEY": "OpenAI",
        "TOGETHER_API_KEY": "Together",
        "GOOGLE_API_KEY": "Google",
        "ANTHROPIC_API_KEY": "Anthropic",
        "COHERE_API_KEY": "Cohere",
        "FIREWORKS_API_KEY": "Fireworks"
    }

    # Load existing .env if it exists
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            existing_env = f.read().splitlines()
    else:
        existing_env = []

    # Create a dictionary of current keys from the .env file
    current_keys = {}
    for line in existing_env:
        if line and '=' in line:
            key, value = line.split('=', 1)
            current_keys[key.strip()] = value.strip()

    new_keys = {}
    for env_var, service_name in keys.items():
        if env_var in current_keys and current_keys[env_var] != '':
            skip = input(f'{service_name} key is already set. Do you want to skip this key setup? (y/n): ').strip().lower()
            if skip == 'y':
                new_keys[env_var] = current_keys[env_var]
                continue
        key_value = input(f'Enter the API key for {service_name} (press Enter to skip): ').strip()
        if key_value:
            new_keys[env_var] = key_value
        else:
            new_keys[env_var] = ''

    # Write the new keys to the .env file
    with open(env_file, "w") as f:
        for env_var, key_value in new_keys.items():
            f.write(f"{env_var}={key_value}\n")

    print('Done!\n')


if __name__ == "__main__":
    print('\n\n')
    print('- - - - - SETUP - - - - -\n')
    print("Starting repository setup...\n")
    
    # Get the environment name and flag indicating if it was newly created
    env_name, created_new_env = setup_conda_env()
    
    # Only install requirements if a new environment was created
    if created_new_env:
        install_requirements(env_name)
    
    setup_api_keys()
    print("Repository setup complete!")
    print('\n\n')

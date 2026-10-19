[Back to Index 🗂️](./README.md)

<center><h1>👨‍💻 Python Project Guide</h1></center>

**Who this is for:** Anyone starting a new Python project who wants a clean, documented layout.  
**Last reviewed:** 2026-10  
**Prerequisites:** [Python Setup Tutorial](./Python-Setup-Tutorial.md).

<details markdown="1">
<summary><b>Table of Contents</b></summary>

- [1️⃣ Project Folder Structure](#1️⃣-project-folder-structure)
- [2️⃣ Function Documentation (PEP 257 Style)](#2️⃣-function-documentation-pep-257-style)
- [3️⃣ Virtual Environments & Dependency Tracking](#3️⃣-virtual-environments--dependency-tracking)
- [4️⃣ Writing a clear README.md](#4️⃣-writing-a-clear-readmemd)
- [5️⃣ Version Control](#5️⃣-version-control)

</details>

A practical guide to organizing, documenting, and maintaining clean Python projects — whether for Deep Learning, Data Science, or Software Engineering.

<br>

# 1️⃣ Project Folder Structure

Always use a clean and modular structure:

```bash
my_project/
├── README.md                 # Project overview, installation, and usage
├── requirements.txt          # List of Python dependencies
├── .gitignore                # Files and folders to exclude from version control
├── .venv/                    # Virtual environment (excluded from Git)
├── config/                   # Centralized configuration for paths, parameters, etc.
│   └── config.yaml           # YAML file storing configurable paths or hyperparameters
├── src/                      # Main application code (organized by function or logic)
│   ├── main.py               # Entry point script
│   ├── dataset.py            # Dataset loading and preprocessing logic
│   ├── model.py              # Model architecture definitions
│   ├── train.py              # Training loop
│   └── utils.py              # General utilities
├── tests/                    # Unit and integration tests
│   └── test_*.py             # Individual test files
```

* `src/`: Contains your actual training, inference, and business logic.
* `config/`: Stores one or more `.yaml` (for path structures), `.json`(for light data storage) or `.env` (for environment variables). These files can be easily loaded in your Python scripts with the libraries `yaml`, `json`and `dotenv` respectively.
* `tests/`: Ensures all key functionality is verifiable.
* `.venv/`: Local project environment (`venv` or `uv`), kept out of version control. Conda environments live outside the project instead.
* `requirements.txt`: Captures dependencies used in the project.
* `.gitignore`: Prevents accidental commits of logs, temp files, environments, etc.
* `README.md`: Provides project setup, usage, and documentation.

> Optional directories like `notebooks/`, `scripts/`, or `data/` should be added only when necessary and clearly documented.

<br>

# 2️⃣ Function Documentation (PEP 257 Style)

Clear function documentation improves readability, usability, and maintainability. When writing your functions, you should:
- Use type hints in the function signature.
- Include a docstring that describes what the function does.
- Use `:param` and `:return` tags to document each input and output.

Template Example:

```python
def function(parameter_1: str,
             parameter_2: bool = False) -> List[float]:
    """
    Load numerical data from a file.

    :param parameter_1: Parameter 1 description.
    :param parameter_2: Parameter 2 description.
    
    :return: Returned object.
    """

    # your code here

    pass
```

> Keep your descriptions short but clear. Mention any assumptions or side effects if needed.

This format is ideal for auto-generated documentation tools and makes code easier to navigate for collaborators and future-you.

<br>

# 3️⃣ Virtual Environments & Dependency Tracking

It's good practice to activate a virtual environment when working on any Python project, ensuring your dependencies remain isolated and controlled. Pick one tool per project — `venv` + `pip`, Conda, or `uv` — as compared in the [Python Setup Tutorial](./Python-Setup-Tutorial.md#-which-tool). With `uv`, dependencies live in `pyproject.toml` + `uv.lock` and the steps below are handled by `uv add` / `uv sync`. With `venv` or Conda + `pip`, all the dependencies are kept into a `requirements.txt` file that specify the name of the library used and eventually its version:

Example:

```bash
torch>=1.13  # Package version greater or equal than
numpy==2.2.3  # Exact version needed
scikit-learn  # No version specified (the latest for your Python will be used)
```

> **Note**: `requirements.txt` cannot pin the Python version itself — state it in the README, or use `requires-python` in `pyproject.toml` / `.python-version` with `uv`.

You can automatically generate a `requirements.txt` with the `pipreqs` package:

```bash
pip install pipreqs
```

```bash
pipreqs ./  # Scans your code and creates a minimal requirements.txt
```

When starting a project or collaborating, you can install the requirements specified with:

```bash
pip install -r requirements.txt
```

> **Note**: in order to keep the testing environment clean to avoid any bugs due to package versions, it's important to create a single Virtual Environment to contains the necessary libraries with the needed versions.

<br>

# 4️⃣ Writing a clear README.md

Your `README.md` is the first place users, collaborators, and future-you will look to understand how your project works. It should serve as both a quick-start guide and high-level documentation. Recommended sections are:

- **Project Title and Description**.
- **Installation**: List dependencies and how to install them.
- **Configuration**: Explain how to configure the project. If using configuration files, include an example or point to one in the repository.
- **Project Structure**: Briefly describe the folder structure and what each directory/file is responsible for.
- **Usage**: Show how to run key scripts (e.g. training, testing, inference). 

Here follow a good structure to describe your Python script:

```markdown
### `your_script.py`

**Description**  
Briefly describe what this script does.  
_Example: This script trains a neural network on a dataset using the configuration defined in a YAML file._

**Requirements**  
List any files, pre-setup, or directories needed before running this script.

- Fill out the configuration file at `config/train_config.yaml`
- Ensure the dataset is located in the `data/` directory
- Create an empty `checkpoints/` folder for saving models

**Arguments**

| Argument         | Type    | Description                                   | Required | Default         |
|------------------|---------|-----------------------------------------------|----------|-----------------|
| `--config`       | string  | Path to the configuration file                | Yes      | -               |
| `--epochs`       | int     | Number of training epochs                     | No       | `10`            |
| `--batch_size`   | int     | Size of each training batch                   | No       | `64`            |
| `--save_dir`     | string  | Directory to save trained model checkpoints   | No       | `./checkpoints` |
| `--eval_only`    | flag    | Run in evaluation mode only                   | No       | `False`         |

**Examples**

Train the model using a specific configuration:

    ```bash
    python your_script.py --config config/train_config.yaml --epochs 100
    ```

Evaluate a pre-trained model:

    ```bash
    python your_script.py --config config/eval_config.yaml --eval_only
    ```

**Notes**  
- Logging output will be saved to the `logs/` directory, if enabled in the config.
- The script will automatically create the `save_dir` if it doesn't exist.
```

<br>

# 5️⃣ Version Control

Use Git for everything — code, configs,
dependency files -  in order to keep track of any changes.

For a day-to-day collaborative workflow, see the [Git guide](./Git.md) (and [Git LFS](./Git-LFS.md) for large files). A quick external reference: [git - the simple guide](https://rogerdudler.github.io/git-guide/).

<br>
<br>
<br>

[Back to Index 🗂️](./README.md)
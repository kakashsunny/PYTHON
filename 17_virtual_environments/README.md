# Virtual Environments in Python

## Definitions & Concepts
A virtual environment is a self-contained directory tree containing a Python installation for a particular version of Python, plus a number of additional packages. It isolates project dependencies from the global system environment.

## Why Use Virtual Environments?
- Avoid version conflicts between projects (e.g., Project A needs Django 2.2, Project B needs Django 4.0).
- Run and install Python packages without needing administrative (sudo) privileges.
- Standardize configurations across team members.

## Creation & Management Command Guide
1. **Create Environment**:
   - `python -m venv myenv`
2. **Activate Environment**:
   - **Windows**: `myenv\Scripts\activate`
   - **macOS/Linux**: `source myenv/bin/activate`
3. **Deactivate**:
   - `deactivate`
4. **Export Dependencies**:
   - `pip freeze > requirements.txt`
5. **Install Dependencies**:
   - `pip install -r requirements.txt`

## Best Practices
- Never commit virtual environment folders (e.g., `venv/`, `env/`) to version control repositories like Git. Add them to your `.gitignore`.
- Always generate a `requirements.txt` for your project.

## Common Mistakes
- Installing packages globally because the virtual environment was not activated.
- Renaming or moving the virtual environment directory (this breaks absolute paths inside environment scripts; recreate it instead).

## Interview Tips
- **Q**: What is the difference between `pip` and `venv`?
- **A**: `pip` is the Python package installer (used to download and manage third-party packages). `venv` is the module used to create isolated execution environments. They are used together.

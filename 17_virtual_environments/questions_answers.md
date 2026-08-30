# Questions & Answers: Virtual Environments

## MCQs
1. **Which file is traditionally used to list a project's dependencies?**
   - A) `package.json`
   - B) `setup.py`
   - C) `requirements.txt`
   - D) `dependencies.ini`
   - **Answer**: C
   - **Explanation**: `requirements.txt` is the standard name for listing Python package dependencies.

2. **Which folder should be added to `.gitignore`?**
   - A) The main source code folder
   - B) The virtual environment folder (e.g., `.venv/`)
   - C) `requirements.txt`
   - D) `README.md`
   - **Answer**: B
   - **Explanation**: Virtual environments contain binary libraries specific to the host OS and machine, and should not be committed to source control.

## Beginner & Intermediate Questions
### Q1: What does `pip freeze` do?
**Answer**: It prints a list of all installed packages in the current environment along with their exact version numbers, which is typically redirected into `requirements.txt`.

### Q2: What is the difference between `venv` and newer tools like `poetry` or `pipenv`?
**Answer**: `venv` is a low-level, built-in tool that handles environment isolation. Tools like `poetry` and `pipenv` are higher-level package managers that combine dependency resolution, environment isolation, and project publishing in a single workflow.

## Coding Practice & Solutions
### Problem: Write a Python command to install a package and freeze the requirements list.
**Solution**:
```bash
# Terminal Commands
pip install pandas
pip freeze > requirements.txt
```

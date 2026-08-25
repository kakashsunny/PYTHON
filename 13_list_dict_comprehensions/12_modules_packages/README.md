# Modules & Packages in Python

## Definitions & Concepts
- **Module**: A file containing Python definitions and statements (a single `.py` file).
- **Package**: A directory of Python modules containing a special file named `__init__.py` (optional in Python 3.3+, but recommended for clarity).
- **`sys.path`**: A list of strings that specifies the search path for modules.

## Importing Syntax
```python
import math               # Basic import
import statistics as stats # Import with alias
from os import path       # Specific import
```

## Creating Packages
```
my_package/
    ├── __init__.py      # Package initialization file
    ├── module_a.py
    └── module_b.py
```

## Best Practices
- Put all import statements at the top of the file.
- Group imports logically:
  1. Standard library imports.
  2. Related third-party imports.
  3. Local application/library-specific imports.
- Avoid wildcard imports (`from module import *`) as they pollute the namespace and make debugging difficult.

## Common Mistakes
- Circular imports, where Module A imports Module B, and Module B imports Module A.
- Naming a local script the same name as a standard library module (e.g., naming a test script `math.py`, causing imports to fail).

## Interview Tips
- **Q**: What does the `__init__.py` file do?
- **A**: It marks the directory as a Python package. It can also run initialization code for the package and define public APIs using the `__all__` variable.

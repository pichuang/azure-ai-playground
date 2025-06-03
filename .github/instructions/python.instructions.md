---
applyTo: "**/*.py"
---
# Project coding standards for Python

Apply the [general coding guidelines](./general-coding.instructions.md) to all code.

## Python guidelines

### Code Style

- Use Python3 syntax
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for style guidelines
- Use [PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstrings
- Use 4 spaces for indentation, instead of tabs
- Use `snake_case` for variable and function names
- Use `CamelCase` for class names
- Use `UPPER_CASE` for constants
- Use `f-strings` for string formatting
- Use double quotes for strings
- One blank lines before top-level functions/classes

### Logging

- Use the standard logging module for all logging purposes
- Configure loggers with appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Avoid using print statements for logging
- Include contextual information in log messages to aid debugging
- Follow consistent log message formatting

### Comment Style

- Write comments in English
- Ensure comments are updated promptly to reflect any code changes
- Limit comment lines to 72 characters
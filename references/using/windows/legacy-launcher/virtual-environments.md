# 4.12.1.2. Virtual environments

#### 4.12.1.2. Virtual environments

Added in version 3.5.

When the launcher is invoked without an explicit Python version and a virtual environment (built either with the standard library [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) module or the third-party `virtualenv` tool) is active, the launcher runs that virtual environment's interpreter in place of the global one. To use the global interpreter instead, either deactivate the virtual environment or name the global Python version outright.

[Subject index](INDEX.md) · [Previous source section](from-the-command-line.md) · [Following source section](from-a-script.md)

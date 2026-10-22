# PYTHONWARNINGS

PYTHONWARNINGS

This amounts to the `-W` option. When set to a comma separated string, it amounts to giving `-W` repeatedly, where filters appearing later in the list outrank those appearing earlier.

The most basic settings apply one specific action across the board to every warning a process emits (even ones that would otherwise be ignored by default):

```sh
PYTHONWARNINGS=default  # Warn once per call location
PYTHONWARNINGS=error    # Convert to exceptions
PYTHONWARNINGS=always   # Warn every time
PYTHONWARNINGS=all      # Same as PYTHONWARNINGS=always
PYTHONWARNINGS=module   # Warn once per calling module
PYTHONWARNINGS=once     # Warn once per Python process
PYTHONWARNINGS=ignore   # Never warn

```

See [The Warnings Filter](https://docs.python.org/3.14/library/warnings.html#warning-filter) and [Describing Warning Filters](https://docs.python.org/3.14/library/warnings.html#describing-warning-filters) for more details.

[Subject index](INDEX.md) · [Previous source section](pythonexecutable.md) · [Following source section](pythonfaulthandler.md)

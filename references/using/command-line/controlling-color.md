# 1.1.4. Controlling color

### 1.1.4. Controlling color

Out of the box, the Python interpreter is set up to apply colors that highlight output under particular conditions, for instance while showing tracebacks. You can govern this behavior by assigning various environment variables.

Assigning the environment variable `TERM` a value of `dumb` will switch color off.

When the [`FORCE_COLOR`](https://force-color.org/) environment variable is present, color turns on no matter what value TERM holds. This proves handy on CI systems that aren't terminals yet can still render ANSI escape sequences.

When the [`NO_COLOR`](https://no-color.org/) environment variable is present, Python turns off every color in its output. This wins out over `FORCE_COLOR`.

Every one of these environment variables is also consulted by other tools to govern color output. If you want to govern color output solely within the Python interpreter, reach for the `PYTHON_COLORS` environment variable. That variable outranks `NO_COLOR`, which itself outranks `FORCE_COLOR`.

[Subject index](INDEX.md) · [Previous source section](x-arbitrary-values-and-option-history.md) · [Following source section](environment-variables.md)

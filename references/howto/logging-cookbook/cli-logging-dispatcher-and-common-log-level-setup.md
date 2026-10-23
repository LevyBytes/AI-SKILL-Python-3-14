# CLI logging dispatcher and common log-level setup

### A CLI application starter template

Below is an example illustrating how you can:

- Choose a logging level driven by command-line arguments

- Route to several subcommands held in separate files, each logging at the same level in a uniform manner

- Rely on simple, minimal configuration

Imagine a command-line program tasked with stopping, starting, or restarting some services. For demonstration, picture this laid out as a file `app.py` serving as the application's main script, with the individual commands living in `start.py`, `stop.py` and `restart.py`. Imagine too that we'd like to govern the program's verbosity through a command-line argument, defaulting to `logging.INFO`. One way to write `app.py` is shown here:

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/logging-cookbook.html#a-cli-application-starter-template).

[Subject index](INDEX.md) · [Start, stop and restart modules](start-stop-and-restart-modules.md) · [CLI logging output at default, DEBUG and WARNING levels](cli-logging-output-at-default-debug-and-warning-levels.md) · [Previous source context](using-a-context-manager-for-selective-logging.md) · [Following source context](start-stop-and-restart-modules.md)

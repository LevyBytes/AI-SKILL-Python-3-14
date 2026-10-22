# CLI logging dispatcher and common log-level setup

### A CLI application starter template

Below is an example illustrating how you can:

- Choose a logging level driven by command-line arguments

- Route to several subcommands held in separate files, each logging at the same level in a uniform manner

- Rely on simple, minimal configuration

Imagine a command-line program tasked with stopping, starting, or restarting some services. For demonstration, picture this laid out as a file `app.py` serving as the application's main script, with the individual commands living in `start.py`, `stop.py` and `restart.py`. Imagine too that we'd like to govern the program's verbosity through a command-line argument, defaulting to `logging.INFO`. One way to write `app.py` is shown here:

```python
import argparse
import importlib
import logging
import os
import sys

def main(args=None):
    scriptname = os.path.basename(__file__)
    parser = argparse.ArgumentParser(scriptname)
    levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    parser.add_argument('--log-level', default='INFO', choices=levels)
    subparsers = parser.add_subparsers(dest='command',
                                       help='Available commands:')
    start_cmd = subparsers.add_parser('start', help='Start a service')
    start_cmd.add_argument('name', metavar='NAME',
                           help='Name of service to start')
    stop_cmd = subparsers.add_parser('stop',
                                     help='Stop one or more services')
    stop_cmd.add_argument('names', metavar='NAME', nargs='+',
                          help='Name of service to stop')
    restart_cmd = subparsers.add_parser('restart',
                                        help='Restart one or more services')
    restart_cmd.add_argument('names', metavar='NAME', nargs='+',
                             help='Name of service to restart')
    options = parser.parse_args()
    # the code to dispatch commands could all be in this file. For the purposes
    # of illustration only, we implement each command in a separate module.
    try:
        mod = importlib.import_module(options.command)
        cmd = getattr(mod, 'command')
    except (ImportError, AttributeError):
        print('Unable to find the code for command \'%s\'' % options.command)
        return 1
    # Could get fancy here and load configuration from file or dictionary
    logging.basicConfig(level=options.log_level,
                        format='%(levelname)s %(name)s %(message)s')
    cmd(options)

if __name__ == '__main__':
    sys.exit(main())

```

[Subject index](INDEX.md) · [Start, stop and restart modules](start-stop-and-restart-modules.md) · [CLI logging output at default, DEBUG and WARNING levels](cli-logging-output-at-default-debug-and-warning-levels.md) · [Previous source context](using-a-context-manager-for-selective-logging.md) · [Following source context](start-stop-and-restart-modules.md)

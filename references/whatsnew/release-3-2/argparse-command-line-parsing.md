# What's New In Python 3.2 / PEP 389: Argparse Command Line Parsing Module - argparse, optparse

### PEP 389: Argparse Command Line Parsing Module

A fresh command line parsing module, [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), arrived to address shortcomings in [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse), which lacked handling for positional arguments (not merely options), subcommands, mandatory options, and several other familiar option-declaration and validation patterns.

As a third-party package it had already proven popular among users. Richer in capability than what came before it, the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module is now recommended for processing command lines. The earlier module remains shipped because so much existing code still relies upon it.

Below is a commented sample parser illustrating capabilities such as constraining results to a fixed set of choices, naming a *metavar* on the help screen, checking that at least one positional argument appears, and declaring a mandatory option:

```python
import argparse
parser = argparse.ArgumentParser(
            description = 'Manage servers',         # main description for help
            epilog = 'Tested on Solaris and Linux') # displayed after help
parser.add_argument('action',                       # argument name
            choices = ['deploy', 'start', 'stop'],  # three allowed values
            help = 'action on each target')         # help msg
parser.add_argument('targets',
            metavar = 'HOSTNAME',                   # var name used in help msg
            nargs = '+',                            # require one or more targets
            help = 'url for target machines')       # help msg explanation
parser.add_argument('-u', '--user',                 # -u or --user option
            required = True,                        # make it a required argument
            help = 'login as user')

```

Here is the parser being invoked against a command string:

```python
>>> cmd = 'deploy sneezy.example.com sleepy.example.com -u skycaptain'
>>> result = parser.parse_args(cmd.split())
>>> result.action
'deploy'
>>> result.targets
['sneezy.example.com', 'sleepy.example.com']
>>> result.user
'skycaptain'

```

And here is the help text the parser produces on its own:

```python
>>> parser.parse_args('-h'.split())

usage: manage_cloud.py [-h] -u USER
                       {deploy,start,stop} HOSTNAME [HOSTNAME ...]

Manage servers

positional arguments:
  {deploy,start,stop}   action on each target
  HOSTNAME              url for target machines

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  login as user

Tested on Solaris and Linux

```

One particularly pleasant [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) capability is declaring subparsers, where each carries its own set of arguments and help text:

```python
import argparse
parser = argparse.ArgumentParser(prog='HELM')
subparsers = parser.add_subparsers()

parser_l = subparsers.add_parser('launch', help='Launch Control')   # first subgroup
parser_l.add_argument('-m', '--missiles', action='store_true')
parser_l.add_argument('-t', '--torpedos', action='store_true')

parser_m = subparsers.add_parser('move', help='Move Vessel',        # second subgroup
                                 aliases=('steer', 'turn'))         # equivalent names
parser_m.add_argument('-c', '--course', type=int, required=True)
parser_m.add_argument('-s', '--speed', type=int, default=0)

```

[Subject index](INDEX.md) · [Previous source section](pep-384-defining-a-stable-abi.md) · [Next source section](pep-389-argparse-command-line-parsing-module-see-also.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

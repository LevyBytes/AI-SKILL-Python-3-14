# What's New In Python 3.2 / PEP 389: Argparse Command Line Parsing Module - optparse

```shell
$ ./helm.py --help                         # top level help (launch and move)
$ ./helm.py launch --help                  # help for launch options
$ ./helm.py launch --missiles              # set missiles=True and torpedos=False
$ ./helm.py steer --course 180 --speed 5   # set movement parameters

```

See also

[**PEP 389**](https://peps.python.org/pep-0389/) - New Command Line Parsing Module

PEP written by Steven Bethard.

[Migrating optparse code to argparse](https://docs.python.org/3.14/howto/argparse-optparse.html#upgrading-optparse-code) for details on the differences from [`optparse`](https://docs.python.org/3.14/library/optparse.html#module-optparse).

[Subject index](INDEX.md) · [Previous source section](argparse-command-line-parsing.md) · [Next source section](pep-391-dictionary-based-configuration-for-logging.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Release/subject declaration](argparse-command-line-parsing.md)

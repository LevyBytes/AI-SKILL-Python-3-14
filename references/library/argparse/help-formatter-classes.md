# argparse - formatter_class - Signature and initial contract

*class *argparse.RawDescriptionHelpFormatter

 *class *argparse.RawTextHelpFormatter

 *class *argparse.ArgumentDefaultsHelpFormatter

 *class *argparse.MetavarTypeHelpFormatter

With `RawDescriptionHelpFormatter` and `RawTextHelpFormatter` you gain finer say over the way text descriptions appear. Normally, `ArgumentParser` objects line-wrap the description and epilog text within command-line help messages:

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
>>> parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

options:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines

```

Handing `RawDescriptionHelpFormatter` to `formatter_class=` signals that the description and epilog are already laid out properly and must not be line-wrapped:

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
>>> parser.print_help()
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

options:
 -h, --help  show this help message and exit

```

`RawTextHelpFormatter` keeps whitespace intact across every kind of help text, argument descriptions included. That said, runs of multiple newlines collapse to a single one. To hold on to several blank lines, drop spaces between the newlines.

`ArgumentDefaultsHelpFormatter` tacks default-value information onto each argument's help message on its own:

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
>>> parser.add_argument('--foo', type=int, default=42, help='FOO!')
>>> parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
>>> parser.print_help()
usage: PROG [-h] [--foo FOO] [bar ...]

positional arguments:
 bar         BAR! (default: [1, 2, 3])

options:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)

```

`MetavarTypeHelpFormatter` adopts the name of each argument's type argument as the display name for that argument's values (in place of the dest, which the standard formatter relies on):

[Subject index](INDEX.md) · [Previous](formatter-class.md) · [Continue](formatter-class-code-example-parser-argparse-argumentparser.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md) · [Owning module, declaration or section: formatter_class](formatter-class.md)

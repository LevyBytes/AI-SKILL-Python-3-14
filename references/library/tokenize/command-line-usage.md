# tokenize - Command-Line Usage

### Command-Line Usage

Added in version 3.3.

You can run the `tokenize` module as a script from the command line. It comes down to this:

```sh
python -m tokenize [-e] [filename.py]

```

The following options are accepted:

 -h, --help

show this help message and exit

 -e, --exact

display token names using the exact type

When `filename.py` is given, its contents get tokenized to stdout. Failing that, tokenization runs on stdin.

[Subject index](INDEX.md) · [Previous](tokenize-tokenize-to-tokenize-tokenerror.md) · [Continue](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: tokenize](tokenize-tokenizer-for-python-source.md)

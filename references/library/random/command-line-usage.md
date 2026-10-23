# random - Command-line usage

### Command-line usage

Added in version 3.13.

You can run the `random` module straight from the command line.

```sh
python -m random [-h] [-c CHOICE [CHOICE ...] | -i N | -f N] [input ...]

```

The following options are accepted:

 -h, --help

Show the help message and exit.

 -c CHOICE [CHOICE ...]

 --choice CHOICE [CHOICE ...]

Emit one randomly selected item by way of `choice()`.

 -i &lt;N&gt;

 --integer &lt;N&gt;

Emit a randomly chosen integer from 1 up to and including N, by way of `randint()`.

 -f &lt;N&gt;

 --float &lt;N&gt;

Emit a randomly chosen floating-point value from 0 up to and including N, by way of `uniform()`.

Should you supply no options, what gets produced is governed by the input:

- String or multiple: same as `--choice`.

- Integer: same as `--integer`.

- Float: same as `--float`.

[Subject index](INDEX.md) · [Previous](recipes.md) · [Continue](command-line-example.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md)

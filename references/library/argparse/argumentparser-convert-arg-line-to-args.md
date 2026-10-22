# argparse — Customizing file parsing

### Customizing file parsing

 ArgumentParser.convert_arg_line_to_args(*arg_line*)

When arguments come out of a file (set up through the *fromfile_prefix_chars* keyword argument on the `ArgumentParser` constructor), each line yields a single argument. For more elaborate handling you can override `convert_arg_line_to_args()`.

It accepts just one argument, *arg_line*, a string pulled from the argument file, and yields a list of arguments parsed out of that string. For every line read from the file, in sequence, the method runs once.

One handy way to override it is to make every space-separated word into its own argument. The snippet below shows how that is done:

```python
class MyArgumentParser(argparse.ArgumentParser):
    def convert_arg_line_to_args(self, arg_line):
        return arg_line.split()

```

Keep in mind that once this override is in place, no single argument may hold spaces any longer, because every space-separated word is split off into its own argument.

[Subject index](INDEX.md) · [Previous](argumentparser-parse-known-args.md) · [Continue](argumentparser-exit-to-argumentparser-error.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

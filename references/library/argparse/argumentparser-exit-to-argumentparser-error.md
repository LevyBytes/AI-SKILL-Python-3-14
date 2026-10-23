# argparse - Exiting methods

### Exiting methods

 ArgumentParser.exit(*status=0*, *message=None*)

It shuts the program down, leaving with the given *status*, and — when one is supplied — first writes a *message* to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). Should you want these steps done another way, override the method:

```python
class ErrorCatchingArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            raise Exception(f'Exiting because of an error: {message}')
        exit(status)

```

 ArgumentParser.error(*message*)

It sends a usage message — *message* included — to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr), then ends the program with a status code of 2.

[Subject index](INDEX.md) · [Previous](argumentparser-convert-arg-line-to-args.md) · [Continue](intermixed-argument-parsing.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

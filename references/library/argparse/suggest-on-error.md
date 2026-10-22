# argparse — suggest_on_error

### suggest_on_error

By default, should a user pass an invalid argument choice or subparser name, `ArgumentParser` quits with error info and prints the allowed argument choices (where given) or subparser names as part of that error message.

Should the user want to switch on suggestions for mistyped argument choices and subparser names, the feature comes alive by setting `suggest_on_error` to `True`. Note that this kicks in only for arguments whose specified choices are strings:

```python
>>> parser = argparse.ArgumentParser(suggest_on_error=True)
>>> parser.add_argument('--action', choices=['debug', 'dryrun'])
>>> parser.parse_args(['--action', 'debugg'])
usage: tester.py [-h] [--action {debug,dryrun}]
tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

```

When your code must remain compatible with older Python releases yet you would like to take advantage of `suggest_on_error` wherever it exists, you can assign it as an attribute once the parser is initialized rather than passing the keyword argument:

```python
>>> parser = argparse.ArgumentParser(description='Process some integers.')
>>> parser.suggest_on_error = True

```

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](exit-on-error.md) · [Continue](color.md) · [Owning module, declaration or section: argparse](argument-parser-overview.md)

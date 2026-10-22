# optparse — Conflicts between options

### Conflicts between options

Without due care, it's all too simple to declare options whose option strings clash:

```python
parser.add_option("-n", "--dry-run", ...)
...
parser.add_option("-n", "--noisy", ...)

```

(That risk grows especially if you've built your own OptionParser subclass carrying some standard options.)

Each time you add an option, `optparse` looks for conflicts against the existing options. Should it find any, it triggers the current conflict-handling mechanism. You can pin down the conflict-handling mechanism either in the constructor:

```python
parser = OptionParser(..., conflict_handler=handler)

```

or with a separate call:

```python
parser.set_conflict_handler(handler)

```

The available conflict handlers are:

>

`"error"` (default)

assume option conflicts are a programming error and raise `OptionConflictError`

`"resolve"`

resolve option conflicts intelligently (see below)

For an example, suppose we set up an `OptionParser` that resolves conflicts intelligently and then add clashing options to it:

```python
parser = OptionParser(conflict_handler="resolve")
parser.add_option("-n", "--dry-run", ..., help="do no harm")
parser.add_option("-n", "--noisy", ..., help="be noisy")

```

Here `optparse` notices that a previously added option is already claiming the `-n` option string. Because `conflict_handler` is `"resolve"`, it sorts the matter out by dropping `-n` from the earlier option's set of option strings. From now on `--dry-run` is the user's only route to that option. Should the user request help, the help message will show it:

```python
Options:
  --dry-run     do no harm
  ...
  -n, --noisy   be noisy

```

You can keep paring away the option strings of a previously added option until none survive, leaving the user with no way to invoke that option from the command-line. When that happens, `optparse` drops the option entirely, so it appears neither in help text nor anywhere else. Continuing with our current OptionParser:

```python
parser.add_option("--dry-run", ..., help="new dry-run option")

```

Now the original `-n`/`--dry-run` option is no longer reachable, so `optparse` removes it, leaving this help text:

```python
Options:
  ...
  -n, --noisy   be noisy
  --dry-run     new dry-run option

```

[Subject index](INDEX.md) · [Previous](option-parser-interspersing-and-option-removal.md) · [Continue](cleanup.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

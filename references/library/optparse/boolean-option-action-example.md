# optparse - Standard option actions - Code example: parser.add_option("--clobber", action="store_true", dest="clobber")

```python
parser.add_option("--clobber", action="store_true", dest="clobber")
parser.add_option("--no-clobber", action="store_false", dest="clobber")

```

- `"append"` [relevant: `type`, `dest`, `nargs`, `choices`]

An argument has to follow the option, and it gets appended to the list held in `dest`. When `dest` lacks a supplied default value, an empty list springs into being the moment `optparse` first meets this option on the command-line. When `nargs` > 1, several arguments are pulled in, and a tuple of length `nargs` is appended to `dest`.

The `type` and `dest` defaults match those of the `"store"` action.

Example:

```python
parser.add_option("-t", "--tracks", action="append", type="int")

```

If `-t3` is seen on the command-line, `optparse` does the equivalent of:

```python
options.tracks = []
options.tracks.append(int("3"))

```

If, a little later on, `--tracks=4` is seen, it does:

```python
options.tracks.append(int("4"))

```

The `append` action calls the `append` method belonging to the option's present value. Consequently, any default value you set has to have an `append` method. It likewise means a non-empty default leaves its elements present in the option's parsed value, with whatever came from the command line appended behind those defaults:

```python
>>> parser.add_option("--files", action="append", default=['~/.mypkg/defaults'])
>>> opts, args = parser.parse_args(['--files', 'overrides.mypkg'])
>>> opts.files
['~/.mypkg/defaults', 'overrides.mypkg']

```

- `"append_const"` [required: `const`; relevant: `dest`]

Behaves like `"store_const"`, except the value `const` is appended to `dest`; just as with `"append"`, `dest` starts out `None`, and an empty list materializes the first time the option turns up.

- `"count"` [relevant: `dest`]

Bump up the integer kept at `dest`. With no default value provided, `dest` starts at zero before its first increment.

Example:

```python
parser.add_option("-v", action="count", dest="verbosity")

```

On the very first appearance of `-v` along the command line, `optparse` carries out the equivalent of:

```python
options.verbosity = 0
options.verbosity += 1

```

Every subsequent occurrence of `-v` results in

```python
options.verbosity += 1

```

- `"callback"` [required: `callback`; relevant: `type`, `nargs`, `callback_args`, `callback_kwargs`]

[Subject index](INDEX.md) · [Previous](standard-option-actions-overview.md) · [Continue](option-action-callback-contract.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md) · [Owning module, declaration or section: Standard option actions](standard-option-actions-overview.md)

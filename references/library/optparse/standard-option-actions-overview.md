# optparse - Standard option actions - Section introduction and initial examples

### Standard option actions

Each of the various option actions carries slightly different requirements and effects. Most actions come with several relevant option attributes you can set to steer `optparse`'s behaviour; a handful carry required attributes that you must set on any option using that action.

- `"store"` [relevant: `type`, `dest`, `nargs`, `choices`]

An argument has to come after the option; that argument gets converted into a value per `type` and saved in `dest`. When `nargs` > 1, several arguments are pulled from the command line, each converted per `type` and stored to `dest` together as a tuple. See the Standard option types section.

Should `choices` be provided (a list or tuple of strings), the type falls back to `"choice"`.

Should `type` be omitted, it falls back to `"string"`.

When `dest` goes unsupplied, `optparse` works out a destination from the first long option string (so `--foo-bar` gives `foo_bar`). Lacking any long option strings, `optparse` instead takes a destination from the first short option string (so `-f` gives `f`).

Example:

```python
parser.add_option("-f")
parser.add_option("-p", type="float", nargs=3, dest="point")

```

As it parses the command line

```python
-f foo.txt -p 1 -3.5 4 -fbar.txt

```

`optparse` will set

```python
options.f = "foo.txt"
options.point = (1.0, -3.5, 4.0)
options.f = "bar.txt"

```

- `"store_const"` [required: `const`; relevant: `dest`]

The value `const` is stored in `dest`.

Example:

```python
parser.add_option("-q", "--quiet",
                  action="store_const", const=0, dest="verbose")
parser.add_option("-v", "--verbose",
                  action="store_const", const=1, dest="verbose")
parser.add_option("--noisy",
                  action="store_const", const=2, dest="verbose")

```

If `--noisy` is seen, `optparse` will set

```python
options.verbose = 2

```

- `"store_true"` [relevant: `dest`]

A special case of `"store_const"` that stores `True` to `dest`.

- `"store_false"` [relevant: `dest`]

Like `"store_true"`, but stores `False`.

Example:

[Subject index](INDEX.md) · [Previous](option-action-to-option-metavar.md) · [Continue](boolean-option-action-example.md) · [Owning module, declaration or section: optparse](optparse-parser-for-command-line-options.md)

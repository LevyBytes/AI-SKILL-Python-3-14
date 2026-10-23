# doctest - Command-line Usage

### Command-line Usage

You can drive the `doctest` module as a script straight from the command line:

```bash
python -m doctest [-v] [-o OPTION] [-f] file [file ...]

```

 -v, --verbose

A thorough rundown of every example attempted is written to standard output, capped off with various summaries:

```python
python -m doctest -v example.py

```

Doing so imports `example.py` as a freestanding module and applies `testmod()` to it. Be aware that this might misbehave when the file belongs to a package and pulls in sibling submodules from that package.

When a file's name doesn't finish in `.py`, `doctest` deduces that it should instead be processed via `testfile()`:

```python
python -m doctest -v example.txt

```

 -o, --option &lt;option&gt;

Option flags govern assorted facets of doctest's behavior; consult the section Option Flags.

Added in version 3.4.

 -f, --fail-fast

A shorthand equivalent to `-o FAIL_FAST`.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](simple-usage-checking-examples-in-a-text-file.md) · [Continue](how-it-works.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

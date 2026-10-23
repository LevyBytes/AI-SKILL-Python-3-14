# doctest - Advanced API

### Advanced API

The basic API is a thin wrapper meant to keep doctest easy to use. It is reasonably flexible and should satisfy most users' requirements; even so, if you need finer-grained command over testing, or you mean to extend what doctest can do, you should reach for the advanced API.

The advanced API centers on two container classes that hold the interactive examples pulled out of doctest cases:

- `Example`: A single Python [statement](https://docs.python.org/3.14/glossary.html#term-statement), together with the output it is expected to produce.

- `DocTest`: A grouping of `Example`s, normally pulled from one docstring or text file.

Further processing classes exist to find, parse, run, and check doctest examples:

- `DocTestFinder`: Locates every docstring inside a given module and applies a `DocTestParser` to turn each docstring that holds interactive examples into a `DocTest`.

- `DocTestParser`: Builds a `DocTest` object out of a string (for instance an object's docstring).

- `DocTestRunner`: Runs the examples within a `DocTest` and applies an `OutputChecker` to confirm their output.

- `OutputChecker`: Sets the actual output of a doctest example against the expected output and judges whether the two match.

The diagram below sums up how these processing classes relate:

```python
                            list of:
+------+                   +---------+
|module| --DocTestFinder-> | DocTest | --DocTestRunner-> results
+------+    |        ^     +---------+     |       ^    (printed)
            |        |     | Example |     |       |
            v        |     |   ...   |     v       |
           DocTestParser   | Example |   OutputChecker
                           +---------+

```

[Subject index](INDEX.md) · [Previous](doctest-set-unittest-reportflags.md) · [Continue](doctest-doctest-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

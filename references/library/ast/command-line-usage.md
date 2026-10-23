# ast - Command-line usage

### Command-line usage

Added in version 3.9.

You can run the `ast` module straight from the command line as a script. It goes like this:

```sh
python -m ast [-m <mode>] [-a] [infile]

```

The following options are accepted:

 -h, --help

Show the help message and exit.

 -m &lt;mode&gt;

 --mode &lt;mode&gt;

State which sort of code is to be compiled, mirroring the *mode* argument of `parse()`.

 --no-type-comments

Don’t parse type comments.

 -a, --include-attributes

Include attributes such as line numbers and column offsets.

 -i &lt;indent&gt;

 --indent &lt;indent&gt;

Indentation of nodes in AST (number of spaces).

 --feature-version &lt;version&gt;

A Python version given as 3.x (3.10, say). When omitted, the interpreter’s own running version applies.

Added in version 3.14.

 -O &lt;level&gt;

 --optimize &lt;level&gt;

Optimization level for parser. Defaults to no optimization.

Added in version 3.14.

 --show-empty

Display empty lists along with fields set to `None`. By default such empty objects stay hidden.

Added in version 3.14.

Supplying `infile` causes its contents to be parsed into an AST and dumped to stdout; leave it out and the input is taken from stdin instead.

See also

[Green Tree Snakes](https://greentreesnakes.readthedocs.io/), a documentation resource maintained elsewhere, lays out useful specifics on handling Python ASTs.

[ASTTokens](https://asttokens.readthedocs.io/en/latest/user-guide.html) tags Python ASTs with where each token and span of text fell in the source they came from. That proves useful for tooling that rewrites source code.

[leoAst.py](https://leo-editor.github.io/leo-editor/appendices.html#leoast-py) reconciles the token-oriented and parse-tree-oriented pictures of python programs, threading bidirectional links between tokens and ast nodes.

[LibCST](https://libcst.readthedocs.io/) reads code into a Concrete Syntax Tree resembling an ast tree while retaining every formatting detail. It serves well for crafting automated refactoring (codemod) tools and linters.

[Parso](https://parso.readthedocs.io) is a Python parser offering error recovery plus round-trip parsing across assorted Python versions (and runnable on several Python versions itself). Parso can additionally enumerate more than one syntax error within your Python file.

[Subject index](INDEX.md) · [Previous](ast-pycf-allow-top-level-await-to-ast-pycf-type-comments.md) · [Owning module, declaration or section: ast](ast-abstract-syntax-trees.md)

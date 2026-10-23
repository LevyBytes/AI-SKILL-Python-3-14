# code: `code.InteractiveInterpreter`

## code - Interpreter base classes

### `code` - Interpreter base classes

**Source code:** [Lib/code.py](https://github.com/python/cpython/tree/3.14/Lib/code.py)

---

Tools for building read-eval-print loops in Python come from the `code` module. It bundles a pair of classes plus some convenience functions, which together let you assemble applications that offer an interactive interpreter prompt.

 *class *code.InteractiveInterpreter(*locals=None*)

Parsing and the interpreter state — that is, the user's namespace — fall to this class, while buffering of input, prompting, and naming of the input file are left out (the filename is always supplied directly). Its optional *locals* argument names the mapping to serve as the namespace where code runs; absent one, a fresh dictionary is built whose `'__name__'` key holds `'__console__'` and whose `'__doc__'` key holds `None`.

Keep in mind that any function and class objects produced within an `InteractiveInterpreter` instance live in the namespace named by *locals*. Pickling them works only when *locals* happens to be the namespace of a module that already exists.

[Subject index](INDEX.md) · [Continue](code-interactiveconsole-class.md)

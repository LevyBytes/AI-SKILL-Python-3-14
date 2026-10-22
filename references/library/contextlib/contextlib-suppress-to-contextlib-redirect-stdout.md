# contextlib: `contextlib.suppress()`, `contextlib.redirect_stdout()`

contextlib.suppress(**exceptions*)

Hands back a context manager that swallows any of the listed exceptions when they surface within a `with` statement body, then carries on at the first statement past the close of the `with` statement.

Like every other device that fully swallows exceptions, reserve this context manager strictly for highly specific errors where quietly pressing on with program execution is recognized as the correct course.

To illustrate:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')

with suppress(FileNotFoundError):
    os.remove('someotherfile.tmp')

```

The equivalent of that code is:

```python
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

try:
    os.remove('someotherfile.tmp')
except FileNotFoundError:
    pass

```

You can use this context manager reentrantly.

Where the body of the `with` block throws a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup), the exceptions being suppressed get stripped out of the group. Whichever exceptions in the group escape suppression are re-raised inside a fresh group built via the original group's [`derive()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.derive) method.

Added in version 3.4.

Changed in version 3.12: the ability for `suppress` to quiet exceptions surfacing within a [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) was introduced.

 contextlib.redirect_stdout(*new_target*)

A context manager for briefly routing [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) toward another file or file-like object.

It lends extra flexibility to current functions or classes whose output is pinned to stdout.

Take, for example, [`help()`](https://docs.python.org/3.14/library/functions.html#help), whose output ordinarily travels to *sys.stdout*. By steering that output into an [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) object you can grab it as a string. The substitute stream comes back from the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method, which makes it accessible as the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement's target:

```python
with redirect_stdout(io.StringIO()) as f:
    help(pow)
s = f.getvalue()

```

If instead you want [`help()`](https://docs.python.org/3.14/library/functions.html#help)'s output written to a file on disk, point the output at an ordinary file:

```python
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)

```

And to route [`help()`](https://docs.python.org/3.14/library/functions.html#help)'s output to *sys.stderr*:

```python
with redirect_stdout(sys.stderr):
    help(pow)

```

Keep in mind that the global impact on [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) renders this context manager unfit for library code and the majority of threaded applications. Likewise, it leaves the output of subprocesses untouched. Even so, it remains a handy technique across many utility scripts.

You can use this context manager reentrantly.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](contextlib-nullcontext.md) · [Continue](contextlib-redirect-stderr-to-contextlib-chdir.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)

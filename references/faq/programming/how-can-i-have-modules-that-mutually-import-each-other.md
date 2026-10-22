# How can I have modules that mutually import each other?

### How can I have modules that mutually import each other?

Suppose you have the following modules:

`foo.py`:

```python
from bar import bar_var
foo_var = 1

```

`bar.py`:

```python
from foo import foo_var
bar_var = 2

```

The trouble is that the interpreter ends up working through this sequence:

- main imports `foo`

- an empty globals namespace for `foo` is set up

- `foo` is compiled and begins running

- `foo` imports `bar`

- an empty globals namespace for `bar` is set up

- `bar` is compiled and begins running

- `bar` imports `foo` (a no-op, because a module called `foo` already exists)

- the import machinery attempts to fetch `foo_var` out of `foo`'s globals so it can assign `bar.foo_var = foo.foo_var`

That final step blows up, since Python has not finished interpreting `foo`, leaving the global symbol dictionary for `foo` still empty.

You run into the identical situation if you write `import foo` and then reach for `foo.foo_var` at module level.

At least three ways around this trouble exist.

Guido van Rossum advises steering clear of `from <module> import ...` entirely and keeping all your code within functions. Any setup of global or class variables ought to rely solely on constants or built-in functions. Under this approach, every name from an imported module is reached as `<module>.<name>`.

Jim Roskind proposes arranging each module's contents in this sequence:

- exports (globals, functions, and classes that don’t need imported base classes)

- `import` statements

- active code (including globals that are initialized from imported values).

Van Rossum isn't fond of this style, since the imports show up in an odd spot, but it gets the job done.

Matthias Urlichs suggests reorganizing your code so the circular import never becomes necessary at all.

None of these remedies rule the others out.

[Subject index](INDEX.md)

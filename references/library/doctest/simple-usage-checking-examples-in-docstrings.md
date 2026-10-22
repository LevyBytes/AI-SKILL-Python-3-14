# doctest — Simple Usage: Checking Examples in Docstrings

### Simple Usage: Checking Examples in Docstrings

The easiest entry point into doctest (though probably not how you'll keep working with it long-term) is to close each module `M` with:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

`doctest` proceeds to inspect the docstrings within module `M`.

Launching the module as a script triggers execution and verification of the examples sitting in those docstrings:

```python
python M.py

```

Nothing surfaces here unless some example breaks, at which point the offending example(s) along with the reason(s) it failed get written to stdout, and the closing line reads `***Test Failed*** N failures.`, in which *N* counts how many examples did not pass.

Instead, run it together with the `-v` flag:

```python
python M.py -v

```

and you'll get a thorough rundown of every example attempted sent to standard output, capped off with various summaries.

Verbose mode can be compelled by handing `verbose=True` to `testmod()`, or suppressed by handing it `verbose=False`. Under either choice, [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv) goes unread by `testmod()` (so whether you supply `-v` makes no difference).

A command line shortcut also exists for invoking `testmod()`; refer to the section Command-line Usage.

Further detail on `testmod()` lives in the section Basic API.

[Subject index](INDEX.md) · [Previous](interactive-example-testing-command.md) · [Continue](simple-usage-checking-examples-in-a-text-file.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

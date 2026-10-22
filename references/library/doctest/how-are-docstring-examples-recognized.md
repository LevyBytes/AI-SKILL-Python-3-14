# doctest — How are Docstring Examples Recognized?

### How are Docstring Examples Recognized?

Usually pasting a copy of an interactive console session straight in works just fine, yet doctest makes no attempt to precisely mimic any one particular Python shell.

```python
>>> # comments are ignored
>>> x = 12
>>> x
12
>>> if x == 13:
...     print("yes")
... else:
...     print("no")
...     print("NO")
...     print("NO!!!")
...
no
NO
NO!!!
>>>

```

Whatever output is expected has to come directly after the closing `'>>> '` or `'... '` line holding the code, and that expected output (should there be any) runs through to the next `'>>> '` line or an all-whitespace line.

The fine print:

- Expected output may not include an all-whitespace line, because such a line is read as marking where expected output stops. When the expected output genuinely needs a blank line, drop `<BLANKLINE>` into your doctest example wherever a blank line should appear.

- Every hard tab gets expanded into spaces against 8-column tab stops. Tabs appearing in the output the tested code generates are left untouched. Since hard tabs in the sample output *do* get expanded, the upshot is that whenever the code's output contains hard tabs, the doctest can only pass if the `NORMALIZE_WHITESPACE` option or directive is active. Failing that, you can rework the test to capture the output and check it against an expected value within the test itself. This approach to tabs in the source emerged from trial and error, and it has turned out to be the least error-prone scheme for dealing with them. A different tab-handling algorithm is achievable by supplying a custom `DocTestParser` class.

- stdout output is captured, whereas stderr output is not (exception tracebacks get captured through a separate mechanism).

- Whenever you extend a line by backslashing within an interactive session, or otherwise employ a backslash for any reason, reach for a raw docstring, which keeps your backslashes intact exactly as typed:

```python
>>> def f(x):
...     r'''Backslashes in a raw docstring: m\n'''
...
>>> print(f.__doc__)
Backslashes in a raw docstring: m\n

```

If you don't, the backslash gets read as part of the string. To take one case, the `\n` shown above would become a newline character. As an alternative, you can write each backslash twice in the doctest version (and skip the raw string):

```python
>>> def f(x):
...     '''Backslashes in a raw docstring: m\\n'''
...
>>> print(f.__doc__)
Backslashes in a raw docstring: m\n

```

- Where the example begins columnwise makes no difference:

```python
>>> assert "Easy!"
      >>> import math
          >>> math.floor(1.9)
          1

```

and just as much leading whitespace gets trimmed off the expected output as showed up on the opening `'>>> '` line that kicked off the example.

[Subject index](INDEX.md) · [Previous](which-docstrings-are-examined.md) · [Continue](what-s-the-execution-context.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

# timeit - Examples - Section introduction and initial examples

### Examples

You can furnish a setup statement that runs only once at the start:

```shell
$ python -m timeit -s "text = 'sample string'; char = 'g'" "char in text"
5000000 loops, best of 5: 0.0877 usec per loop
$ python -m timeit -s "text = 'sample string'; char = 'g'" "text.find(char)"
1000000 loops, best of 5: 0.342 usec per loop

```

The output carries three fields. First the loop count, telling you how many times the statement body ran per timing loop repetition. Then the repetition count (‘best of 5’), telling you how many times the timing loop was repeated. Last comes the mean duration the statement body needed during whichever repetition of the timing loop proved quickest, namely how long the speediest repetition ran divided across the loop count.

```python
>>> import timeit
>>> timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
0.41440500499993504
>>> timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
1.7246671520006203

```

The same is achievable using the `Timer` class and its methods:

```python
>>> import timeit
>>> t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
>>> t.timeit()
0.3955516149999312
>>> t.repeat()
[0.40183617287970225, 0.37027556854118704, 0.38344867356679524, 0.3712595970846668, 0.37866875250654886]

```

The examples that follow demonstrate timing expressions spanning several lines. Here we weigh the cost of [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) against [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)/[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) for checking absent and present object attributes:

```shell
$ python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
20000 loops, best of 5: 15.7 usec per loop
$ python -m timeit "if hasattr(str, '__bool__'): pass"
50000 loops, best of 5: 4.26 usec per loop

$ python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
200000 loops, best of 5: 1.43 usec per loop
$ python -m timeit "if hasattr(int, '__bool__'): pass"
100000 loops, best of 5: 2.23 usec per loop

```

```python
>>> import timeit
>>> # attribute is missing
>>> s = """\
... try:
...     str.__bool__
... except AttributeError:
...     pass
... """
>>> timeit.timeit(stmt=s, number=100000)
0.9138244460009446
>>> s = "if hasattr(str, '__bool__'): pass"
>>> timeit.timeit(stmt=s, number=100000)
0.5829014980008651
>>>
>>> # attribute is present
>>> s = """\
... try:
...     int.__bool__
... except AttributeError:
...     pass
... """
>>> timeit.timeit(stmt=s, number=100000)
0.04215312199994514
>>> s = "if hasattr(int, '__bool__'): pass"
>>> timeit.timeit(stmt=s, number=100000)
0.08588060699912603

```

To let the `timeit` module reach functions you define, you can pass a *setup* parameter holding an import statement:

[Subject index](INDEX.md) · [Previous](command-line-interface.md) · [Continue](examples-code-example-def-test.md) · [Owning module, declaration or section: timeit](timeit-measure-execution-time-of-small-code-snippets.md)

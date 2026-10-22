# What's New In Python 3.0 / Print Is A Function

### Print Is A Function

Where Python 2 had a `print` statement, a [`print()`](https://docs.python.org/3.14/library/functions.html#print) function now stands in, using keyword arguments to cover most of what the old `print` statement's special syntax handled ([**PEP 3105**](https://peps.python.org/pep-3105/)). Examples:

```python
Old: print "The answer is", 2*2
New: print("The answer is", 2*2)

Old: print x,           # Trailing comma suppresses newline
New: print(x, end=" ")  # Appends a space instead of a newline

Old: print              # Prints a newline
New: print()            # You must call the function!

Old: print >>sys.stderr, "fatal error"
New: print("fatal error", file=sys.stderr)

Old: print (x, y)       # prints repr((x, y))
New: print((x, y))      # Not the same as print(x, y)!

```

The item separator can be tailored as well, for instance:

```python
print("There are <", 2**32, "> possibilities!", sep="")

```

which produces:

```none
There are <4294967296> possibilities!

```

Note:

- The ?softspace? behavior that the old `print` statement had is absent from the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function. To illustrate, under Python 2.x `print "A\n", "B"` emitted `"A\nB\n"`, while under Python 3.0 `print("A\n", "B")` emits `"A\n B\n"`.

- Early on you'll catch yourself reaching for the old `print x` repeatedly while working at the prompt. Your fingers will need to learn to reach for `print(x)` from now on!

- Run the `2to3` source-to-source conversion tool and every `print` statement gets rewritten as a [`print()`](https://docs.python.org/3.14/library/functions.html#print) function call on its own, which makes this largely a non-event on sizeable codebases.

[Subject index](INDEX.md) · [Previous source section](common-stumbling-blocks.md) · [Next source section](views-and-iterators-instead-of-lists.md) · [Release/subject declaration](common-stumbling-blocks.md)

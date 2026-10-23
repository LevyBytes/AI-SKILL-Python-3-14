# doctest - Warnings

### Warnings

`doctest` insists on precise matches in expected output. Should even one character differ, the test breaks. You will likely be caught off guard by this more than once while you discover precisely what Python does and does not promise regarding output. Consider, for instance, that when a set is printed, Python makes no promise about the order in which elements appear, so a test such as

```python
>>> foo()
{"spam", "eggs"}

```

is fragile! A first way around it is to write

```python
>>> foo() == {"spam", "eggs"}
True

```

in its place. A second option is to write

```python
>>> d = sorted(foo())
>>> d
['eggs', 'spam']

```

Other approaches exist, but the principle should be clear by now.

Printing values that include an object address is likewise unwise, for instance

```pycon
>>> id(1.0)  # certain to fail some of the time
7948648
>>> class C: pass
>>> C()  # the default repr() for instances embeds an address
<C object at 0x00AC18F0>

```

For that final example, the `ELLIPSIS` directive offers a tidy solution:

```pycon
>>> C()  # doctest: +ELLIPSIS
<C object at 0x...>

```

Floating-point values can likewise differ slightly in output from one platform to the next, since Python hands off certain floating-point math to the platform's C library, and those C libraries differ greatly in their quality here.

```python
>>> 1000**0.1  # risky
1.9952623149688797
>>> round(1000**0.1, 9) # safer
1.995262315
>>> print(f'{1000**0.1:.4f}') # much safer
1.9953

```

Values shaped like `I/2.**J` hold steady on every platform, and I frequently arrange doctest examples so they yield numbers of that shape:

```python
>>> 3./4  # utterly safe
0.75

```

Plain fractions are likewise simpler for readers to grasp, which yields better documentation as a result.

[Subject index](INDEX.md) · [Previous](directives.md) · [Continue](doctest-testfile-to-doctest-run-docstring-examples.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md)

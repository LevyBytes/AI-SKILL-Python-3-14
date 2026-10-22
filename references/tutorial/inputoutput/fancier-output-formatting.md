# 7.1. Fancier Output Formatting

### 7.1. Fancier Output Formatting

Up to this point two means of writing values have come up: *expression statements* together with the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function. (Yet a third route relies on the [`write()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.write) method that file objects carry; you can reach the standard output file through `sys.stdout`. The Library Reference goes into this further.)

Frequently you'll need finer command over how output is laid out than just emitting values separated by spaces. Output can be formatted by a number of approaches.

- For formatted string literals, put an `f` or `F` ahead of the leading quotation mark or triple quotation mark of a string. Within that string, a Python expression placed between the `{` and `}` characters may draw on variables or on literal values.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'

```

- The strings' [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method asks more of you by hand. You'll go on using `{` and `}` to flag where a variable gets slotted in, and you can attach precise formatting directives, yet you must additionally supply the data to be formatted. The code block coming up shows two ways of formatting variables:

```python
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'

```

Observe that the `yes_votes` get padded out with spaces, with a minus sign attached solely for negative numbers. The example likewise shows `percentage` scaled up by 100, carried to 2 decimal places and trailed by a percent sign (consult [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec) for the specifics).

- Lastly, you're free to manage the strings entirely on your own, leaning on slicing and concatenation operations to build whatever arrangement you picture. Among the string type's methods are several handy ones that pad strings out to a chosen column width.

Where elaborate output isn't called for and you merely want to glance at a few variables while debugging, any value can be rendered as a string through the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) or [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) functions.

The job of the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) function is to yield representations of values reasonably legible to people, whereas [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) aims at representations the interpreter can parse (or that raise a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) when no matching syntax exists). When an object carries no special human-facing representation, `str()` yields whatever `repr()` would. Plenty of values, numbers among them or structures such as lists and dictionaries, render identically under either function. Strings stand out as a case with two separate representations.

A few illustrations:

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"

```

Through [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template), the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module ships a straightforward, regular-expression-driven templating scheme. That gives you one more way to drop values into strings: you write placeholders such as `$x` and swap them out for values taken from a dictionary. The syntax is simple to work with, though it leaves you far less command over formatting.

[Subject index](INDEX.md) · [Previous source section](input-and-output.md) · [Following source section](formatted-string-literals.md)

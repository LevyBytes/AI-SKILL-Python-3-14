# What’s New In Python 3.8 / Assignment expressions

### What’s New In Python 3.8

Editor:

Raymond Hettinger

The following walkthrough covers what changed in Python 3.8 relative to the 3.7 line. The 3.8 release shipped on October 14, 2019. The complete record lives in the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog).

### Summary – Release highlights

### New Features

### Assignment expressions

A fresh piece of syntax, `:=`, lets you bind a value to a name while you are still inside a bigger expression. People fondly call it “the walrus operator” because the glyph looks like [the eyes and tusks of a walrus](https://en.wikipedia.org/wiki/Walrus#/media/File:Pacific_Walrus_-_Bull_(8247646168).jpg).

Here, the assignment expression spares you from invoking [`len()`](https://docs.python.org/3.14/library/functions.html#len) on two separate occasions:

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

```

You see a comparable payoff when matching regular expressions, since the match object gets used twice — first to check that a match exists, then to pull out a captured subgroup:

```python
discount = 0.0
if (mo := re.search(r'(\d+)% discount', advertisement)):
    discount = float(mo.group(1)) / 100.0

```

The construct shines too inside while-loops that derive a value to decide whether the loop should stop and then reuse that very value within the loop body:

```python
# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)

```

One more compelling scenario shows up in list comprehensions, where a value produced inside the filtering test is also wanted in the body expression:

```python
[clean_name.title() for name in names
 if (clean_name := normalize('NFC', name)) in allowed_names]

```

Reserve the walrus operator for tidy situations where it trims complexity and makes the code easier to read.

A complete write-up appears in [**PEP 572**](https://peps.python.org/pep-0572/).

(Emily Morehouse drove this work in [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)

[Subject index](INDEX.md) · [Next source section](positional-only-parameters.md)

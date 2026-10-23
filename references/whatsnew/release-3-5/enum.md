# What’s New In Python 3.5 / enum - enum

### enum

When you supply only *names*, the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) callable now offers a fresh *start* parameter that designates the first numeric value for the enum entries:

```python
>>> Animal = enum.Enum('Animal', 'cat dog', start=10)
>>> Animal.cat
<Animal.cat: 10>
>>> Animal.dog
<Animal.dog: 11>

```

(Contributed by Ethan Furman in [bpo-21706](https://bugs.python.org/issue?@action=redirect&bpo=21706).)

[Subject index](INDEX.md) · [Previous source section](email.md) · [Next source section](faulthandler.md) · [Release/subject declaration](summary-release-highlights.md)

# What's New In Python 3.6 / PEP 530: Asynchronous Comprehensions

### PEP 530: Asynchronous Comprehensions

[**PEP 530**](https://peps.python.org/pep-0530/) lets you write `async for` inside list, set, dict comprehensions as well as generator expressions:

```python
result = [i async for i in aiter() if i % 2]

```

On top of that, comprehensions of every variety now accept `await` expressions:

```python
result = [await fun() for fun in funcs if await condition()]

```

See also

[**PEP 530**](https://peps.python.org/pep-0530/) — Asynchronous Comprehensions

PEP written and implemented by Yury Selivanov.

[Subject index](INDEX.md) · [Previous source section](pep-525-asynchronous-generators.md) · [Next source section](pep-487-simpler-customization-of-class-creation.md) · [Release/subject declaration](summary-release-highlights.md)

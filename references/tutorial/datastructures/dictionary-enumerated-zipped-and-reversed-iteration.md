# Dictionary, enumerated, zipped and reversed iteration

### 5.6. Looping Techniques

While iterating over dictionaries, you can fetch the key together with its matching value in one step by using the [`items()`](https://docs.python.org/3.14/library/stdtypes.html#dict.items) method.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave

```

While iterating over a sequence, you can fetch the position index together with its matching value in one step by using the [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) function.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

```

When you want to iterate over two or more sequences together, the [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) function lets you pair up their entries.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

```

When you want to iterate over a sequence backward, first give the sequence in its forward direction and then wrap it in the [`reversed()`](https://docs.python.org/3.14/library/functions.html#reversed) function.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

```

[Subject index](INDEX.md) · [Previous source section](dictionaries.md) · [Following source section](sorted-unique-iteration-and-filtered-copies.md) · [Related tutorial example and explanation](sorted-unique-iteration-and-filtered-copies.md)

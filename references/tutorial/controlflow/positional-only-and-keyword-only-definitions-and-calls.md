# Positional-only and keyword-only definitions and calls

#### 4.9.3.4. Function Examples

Study the sample definitions below, watching the `/` and `*` markers carefully:

```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)

```

That opening definition, `standard_arg`, is the form you'll see most often; it imposes nothing on how it is called, so its argument can arrive positionally or by keyword:

```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2

```

Because `pos_only_arg`, the second one, carries a `/` in its definition, it is confined to positional parameters alone:

```python
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

```

For the third, `kwd_only_arg`, the `*` in its definition signals that nothing but keyword arguments are permitted:

```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3

```

The final one brings together every one of the three conventions inside a single definition:

```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

```

[Subject index](INDEX.md) · [Previous source section](keyword-only-arguments.md) · [Following source section](positional-only-names-shared-with-keyword-dictionaries.md) · [Related tutorial example and explanation](positional-only-names-shared-with-keyword-dictionaries.md)

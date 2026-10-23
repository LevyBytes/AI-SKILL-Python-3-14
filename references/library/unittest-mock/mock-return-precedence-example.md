# unittest.mock - Order of precedence of `side_effect`, `return_value` and *wraps* - Code example: >>> order_mock.get_value.return_value = "second"

```python
>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'second'

```

Assigning `None` to it, on the other hand, is not disregarded, since that counts as an explicit assignment. Consequently precedence will not advance to the wrapped object.

```python
>>> order_mock.get_value.return_value = None
>>> order_mock.get_value() is None
True

```

Setting all three together while initializing the mock still leaves the precedence order unchanged:

```python
>>> order_mock = Mock(spec=Order, wraps=Order,
...                   **{"get_value.side_effect": ["first"],
...                      "get_value.return_value": "second"}
...                   )
...
>>> order_mock.get_value()
'first'
>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'
>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

```

Once `side_effect` runs dry, precedence will not fall through to fetch a value from the successors. Instead a `StopIteration` exception gets raised.

```python
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first side effect value",
...                                     "another side effect value"]
>>> order_mock.get_value.return_value = "second"

```

```python
>>> order_mock.get_value()
'first side effect value'
>>> order_mock.get_value()
'another side effect value'

```

```python
>>> order_mock.get_value()
Traceback (most recent call last):
 ...
StopIteration

```

[Subject index](INDEX.md) · [Previous](mock-side-effect-return-and-wraps-precedence.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Order of precedence of `side_effect`, `return_value` and *wraps*](mock-side-effect-return-and-wraps-precedence.md)

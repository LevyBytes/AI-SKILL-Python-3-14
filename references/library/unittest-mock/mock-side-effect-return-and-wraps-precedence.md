# unittest.mock - Order of precedence of `side_effect`, `return_value` and *wraps* - Section introduction and initial examples

### Order of precedence of `side_effect`, `return_value` and *wraps*

Their precedence runs as follows:

1.

`side_effect`

2.

`return_value`

3.

*wraps*

With all three configured, mock yields the value from `side_effect` and disregards both `return_value` and the wrapped object entirely. With any two configured, the one ranked higher supplies the value. The order in which they were assigned makes no difference; the precedence order holds steady.

```python
>>> from unittest.mock import Mock
>>> class Order:
...     @staticmethod
...     def get_value():
...         return "third"
...
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first"]
>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'first'

```

Since `None` is the default for `side_effect`, setting its value back to `None` makes the precedence get evaluated between `return_value` and the wrapped object, with `side_effect` left out.

```python
>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'

```

When the value `side_effect` returns is `DEFAULT`, that value is disregarded and precedence advances to the next in line to source the return value.

```python
>>> from unittest.mock import DEFAULT
>>> order_mock.get_value.side_effect = [DEFAULT]
>>> order_mock.get_value()
'second'

```

Whenever `Mock` is wrapping an object, `return_value` defaults to `DEFAULT`.

```python
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.return_value
sentinel.DEFAULT
>>> order_mock.get_value.return_value
sentinel.DEFAULT

```

Precedence passes over this value and moves on to the final candidate, the wrapped object.

Because the genuine call lands on the wrapped object, instantiating this mock returns a real instance of the class. You must pass along whatever positional arguments the wrapped object requires.

```python
>>> order_mock_instance = order_mock()
>>> isinstance(order_mock_instance, Order)
True
>>> order_mock_instance.get_value()
'third'

```

```python
>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

```

[Subject index](INDEX.md) · [Previous](unittest-mock-seal.md) · [Continue](mock-return-precedence-example.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)

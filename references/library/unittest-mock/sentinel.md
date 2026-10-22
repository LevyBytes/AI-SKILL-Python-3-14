# unittest.mock: Sentinel identity example

```python
>>> real = ProductionClass()
>>> real.method = Mock(name="method")
>>> real.method.return_value = sentinel.some_object
>>> result = real.method()
>>> assert result is sentinel.some_object
>>> result
sentinel.some_object

```

[Subject index](INDEX.md) · [Continue](unittest-mock-default.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: sentinel](unittest-mock-sentinel.md) · [Owning module, declaration or section: unittest.mock.sentinel](unittest-mock-sentinel.md) · [Preceding source contract and version conditions](unittest-mock-sentinel.md)

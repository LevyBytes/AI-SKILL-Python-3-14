# unittest.mock - Autospeccing - Code example: >>> class Something:

```python
>>> class Something:
...   def __init__(self):
...     self.a = 33
...
>>> class SomethingForTest(Something):
...   a = 33
...
>>> p = patch('__main__.Something', autospec=SomethingForTest)
>>> mock = p.start()
>>> mock.a
<NonCallableMagicMock name='Something.a' spec='int' id='...'>

```

[Subject index](INDEX.md) · [Previous](autospeccing-code-example-from-urllib-import-request.md) · [Continue](unittest-mock-seal.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md) · [Owning module, declaration or section: Autospeccing](autospeccing-section-introduction-and-initial-examples.md)

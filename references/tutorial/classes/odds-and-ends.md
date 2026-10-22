# 9.7. Odds and Ends

### 9.7. Odds and Ends

Now and then a data type along the lines of Pascal’s “record” or C’s “struct” comes in handy, grouping a handful of named data items together. The idiomatic route here is to lean on [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses):

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

```

```python
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000

```

Where some Python code expects a given abstract data type, you can frequently hand it a class that mimics that type’s methods in its place. Say you’ve got a function that formats data drawn from a file object; you could build a class sporting [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) and [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) methods that pull from a string buffer instead, then pass that along as the argument.

[Instance method objects](https://docs.python.org/3.14/reference/datamodel.html#instance-methods) carry attributes as well: [`m.__self__`](https://docs.python.org/3.14/reference/datamodel.html#method.__self__) is the instance object that owns the method `m()`, while [`m.__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__) is the [function object](https://docs.python.org/3.14/reference/datamodel.html#user-defined-funcs) that backs the method.

[Subject index](INDEX.md) · [Previous source section](private-variables.md) · [Following source section](iterators.md)

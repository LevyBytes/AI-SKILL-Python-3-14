# collections: `collections.namedtuple()`, `somenamedtuple._make()`

### `namedtuple()` Factory Function for Tuples with Named Fields

Named tuples attach significance to every slot within a tuple, yielding code that reads more clearly and documents itself. Anywhere ordinary tuples would serve, named tuples work too, and they add the ability to reach a field by its name rather than by a positional index.

 collections.namedtuple(*typename*, *field_names*, ***, *rename=False*, *defaults=None*, *module=None*)

Hand back a fresh tuple subclass named *typename*. That subclass produces tuple-like objects whose fields can be reached through attribute lookup, while remaining indexable and iterable. Each subclass instance also carries a useful docstring (containing *typename* and *field_names*) plus a useful [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) method that prints the tuple contents in a `name=value` layout.

The *field_names* take the form of a string sequence such as `['x', 'y']`. As an alternative, *field_names* may be one string in which each fieldname is split by whitespace and/or commas, for instance `'x y'` or `'x, y'`.

A fieldname may be any valid Python identifier, with the exception of names that begin with an underscore. Valid identifiers are made up of letters, digits, and underscores, must not lead off with a digit or underscore, and may not be a [`keyword`](https://docs.python.org/3.14/library/keyword.html#module-keyword) like *class*, *for*, *return*, *global*, *pass*, or *raise*.

When *rename* is true, any invalid fieldnames are swapped out automatically for positional ones. For instance, `['abc', 'def', 'ghi', 'abc']` turns into `['abc', '_1', 'ghi', '_3']`, dropping the keyword `def` along with the repeated fieldname `abc`.

*defaults* may be `None` or an [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) of default values. Because any field carrying a default must follow all fields lacking one, the *defaults* line up with the rightmost parameters. As an example, given fieldnames `['x', 'y', 'z']` and defaults `(1, 2)`, `x` becomes a required argument, `y` defaults to `1`, and `z` defaults to `2`.

Whenever *module* is given, the named tuple’s [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#type.__module__) attribute is assigned that value.

Instances of a named tuple carry no per-instance dictionaries, which keeps them lightweight and no more memory-hungry than ordinary tuples.

For pickling to work, the named tuple class ought to be bound to a variable whose name equals *typename*.

Changed in version 3.1: Added support for *rename*.

Changed in version 3.6: The *verbose* and *rename* parameters became [keyword-only arguments](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

Changed in version 3.6: Added the *module* parameter.

Changed in version 3.7: Removed the *verbose* parameter and the `_source` attribute.

Changed in version 3.7: Added the *defaults* parameter and the `_field_defaults` attribute.

```pycon
>>> # Basic example
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
>>> x, y = p                # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y               # fields also accessible by name
33
>>> p                       # readable __repr__ with a name=value style
Point(x=11, y=22)

```

Named tuples shine when you want to give field names to the result tuples coming back from the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) or [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) modules:

```python
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)

```

On top of the methods they inherit from tuples, named tuples come with three extra methods plus two attributes. So that they never collide with field names, those method and attribute names lead off with an underscore.

 *classmethod *somenamedtuple._make(*iterable*, */*)

Class method that builds a fresh instance out of an existing sequence or iterable.

```pycon
>>> t = [11, 22]
>>> Point._make(t)
Point(x=11, y=22)

```

[Subject index](INDEX.md) · [Previous](defaultdict-examples.md) · [Continue](somenamedtuple-asdict-to-somenamedtuple-fields.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md)

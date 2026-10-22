# Complete Enum functional signature, parameters and start version note

Here is the full signature:

```python
Enum(
    value='NewEnumName',
    names=<...>,
    *,
    module='...',
    qualname='...',
    type=<mixed-in class>,
    start=1,
    )

```

- *value*: the name the new enum class will store for itself.

- *names*: the enum's members. It may take the form of a string split on whitespace or commas (values begin at 1 unless you say otherwise):

```python
'RED GREEN BLUE' | 'RED,GREEN,BLUE' | 'RED, GREEN, BLUE'

```

or an iterator of names:

```python
['RED', 'GREEN', 'BLUE']

```

or an iterator of (name, value) pairs:

```python
[('CYAN', 4), ('MAGENTA', 5), ('YELLOW', 6)]

```

or a mapping:

```python
{'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42}

```

- *module*: the module name in which the new enum class lives.

- *qualname*: the spot within the module where the new enum class lives.

- *type*: a type to mix into the new enum class.

- *start*: the number to begin counting from when only names get passed.

Changed in version 3.5: The *start* parameter was added.

[Subject index](INDEX.md) · [Functional Enum creation and pickling module/qualname requirements](functional-enum-pickling-module-and-qualname.md) · [Previous source context](functional-enum-pickling-module-and-qualname.md) · [Following source context](intenum.md)

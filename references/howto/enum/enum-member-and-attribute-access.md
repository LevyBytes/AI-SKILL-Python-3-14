# Programmatic access to enumeration members and their attributes

### Programmatic access to enumeration members and their attributes

There are times when reaching members of an enumeration programmatically pays off (that is, scenarios where `Color.RED` is no help because the precise color isn't known while the program is being written). `Enum` supports that kind of access:

```python
>>> Color(1)
<Color.RED: 1>
>>> Color(3)
<Color.BLUE: 3>

```

To fetch enum members by *name*, reach for item access:

```python
>>> Color['RED']
<Color.RED: 1>
>>> Color['GREEN']
<Color.GREEN: 2>

```

When you hold an enum member and want its `name` or `value`:

```python
>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1

```

[Subject index](INDEX.md) · [Previous source context](flag-chores-and-automatic-values.md) · [Following source context](duplicating-enum-members-and-values.md)

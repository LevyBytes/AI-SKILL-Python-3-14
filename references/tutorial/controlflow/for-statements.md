# 4.2. `for` Statements

### 4.2. `for` Statements

The [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement in Python is somewhat different from what you might know in C or Pascal. Where Pascal always steps through an arithmetic progression of numbers, and C hands you control over both the loop step and the stop test, Python’s `for` statement instead walks through the elements of any sequence (such as a list or a string), following the order in which they occur. To give an example (no pun intended):

```python
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12

```

Getting it right is awkward when your code alters a collection at the same time it walks through that very collection. A cleaner approach is normally to iterate across a duplicate of the collection, or else to build a fresh one:

```python
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

```

[Subject index](INDEX.md) · [Previous source section](if-statements.md) · [Following source section](the-range-function.md)

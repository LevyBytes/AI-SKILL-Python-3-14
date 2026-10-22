# 9.6. Private Variables

### 9.6. Private Variables

Python has no “private” instance variables of the sort reachable only from within an object. There is, though, a convention nearly all Python code observes: any name carrying a leading underscore (say `_spam`) is meant to be read as a non-public piece of the API — be it a function, a method, or a data member. Treat it as an implementation detail liable to change with no warning.

Because there’s a genuine reason to want class-private members (chiefly to dodge clashes between names a subclass defines and ones already in use), a modest mechanism for it exists, dubbed *name mangling*. Whenever an identifier takes the form `__spam` (two or more leading underscores, no more than one trailing underscore), the text is swapped out for `_classname__spam`, in which `classname` is the present class name minus any leading underscore(s). That rewriting happens regardless of where the identifier sits syntactically, so long as it falls inside a class definition.

See also

The [private name mangling specifications](https://docs.python.org/3.14/reference/expressions.html#private-name-mangling) cover the particulars and the corner cases.

Name mangling earns its keep by letting subclasses override methods while leaving intraclass method calls intact. Here’s an illustration:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

```

That example holds up even should `MappingSubclass` bring in a `__update` identifier of its own, because it becomes `_Mapping__update` within the `Mapping` class and `_MappingSubclass__update` within the `MappingSubclass` class, each respectively.

Keep in mind the mangling rules exist chiefly to head off mishaps; reaching or altering a variable deemed private remains feasible. In odd situations — debugging, for one — that can even come in handy.

Be aware that code fed to `exec()` or `eval()` doesn’t take the invoking class’s name as the current class; the behavior parallels that of the `global` statement, which is itself confined to code byte-compiled together. That same limit holds for `getattr()`, `setattr()`, and `delattr()`, and likewise when you touch `__dict__` straight on.

[Subject index](INDEX.md) · [Previous source section](multiple-inheritance.md) · [Following source section](odds-and-ends.md)

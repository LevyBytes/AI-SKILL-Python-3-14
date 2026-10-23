# pickle - Handling Stateful Objects

### Handling Stateful Objects

What follows is an example demonstrating how to change a class's pickling behavior. The `TextReader` class below opens a text file and, each time its `readline()` method runs, hands back the line number along with the line contents. When a `TextReader` instance is pickled, every attribute *except* the file object member gets saved. On unpickling, the file is reopened and reading picks up from where it left off. The `__setstate__()` and `__getstate__()` methods make this work.

```python
class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state['file']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Finally, save the file.
        self.file = file

```

Using it might look roughly like the following:

```python
>>> reader = TextReader("hello.txt")
>>> reader.readline()
'1: Hello world!'
>>> reader.readline()
'2: I am line number two.'
>>> new_reader = pickle.loads(pickle.dumps(reader))
>>> new_reader.readline()
'3: Goodbye!'

```

[Subject index](INDEX.md) · [Previous](dispatch-tables.md) · [Continue](custom-reduction-for-types-functions-and-other-objects.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)

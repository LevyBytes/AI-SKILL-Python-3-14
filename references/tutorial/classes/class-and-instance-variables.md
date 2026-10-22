# 9.3.5. Class and Instance Variables

### 9.3.5. Class and Instance Variables

Broadly, instance variables hold data that is particular to each individual instance, whereas class variables hold attributes and methods that every instance of the class has in common:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'

```

As covered in A Word About Names and Objects, data that is shared can produce results that catch you off guard once [mutable](https://docs.python.org/3.14/glossary.html#term-mutable) objects such as lists and dictionaries are involved. As an example, the *tricks* list in the code below ought not to be made a class variable, since one solitary list would then be common to every *Dog* instance:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']

```

A properly designed class would rely on an instance variable in its place:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

```

[Subject index](INDEX.md) · [Previous source section](method-objects.md) · [Following source section](random-remarks.md)

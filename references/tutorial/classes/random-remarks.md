# 9.4. Random Remarks

### 9.4. Random Remarks

When one attribute name shows up in both an instance and its class, attribute lookup gives the instance precedence:

```python
>>> class Warehouse:
...    purpose = 'storage'
...    region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east

```

Both methods and the ordinary users ("clients") of an object may reference its data attributes. Put differently, classes can't be used to build pure abstract data types. Indeed, nothing within Python lets you enforce data hiding — the whole thing rests on convention. (That said, the Python implementation, coded in C, is capable of fully concealing implementation details and policing access to an object when that's needed; C-written extensions to Python can make use of this.)

Clients ought to handle data attributes carefully — by trampling on an object's data attributes, a client can break invariants the methods rely on. Note that a client is free to bolt its own data attributes onto an instance object without upsetting the methods' correctness, provided name collisions are avoided — here again, a naming convention can spare a great deal of trouble.

No shorthand exists for referencing data attributes (or, for that matter, other methods!) from within methods. To my mind this genuinely improves how readable methods are: there's no risk of mixing up local variables with instance variables while scanning over a method.

Conventionally, a method's first argument bears the name `self`. That is purely a convention: the name `self` carries no special significance to Python at all. Be aware, though, that flouting the convention can make your code harder for other Python programmers to read, and it's even imaginable that someone could write a *class browser* program that depends on the convention.

A method is defined for instances of a class by any function object that is one of that class's attributes. The function definition need not be textually wrapped inside the class definition: binding a function object to a local variable within the class works just as well. For example:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

```

At this point `f`, `g`, and `h` are all attributes of class `C` referring to function objects, and as a result they are all methods of instances of `C` — with `h` being exactly the same as `g`. Bear in mind that doing this generally accomplishes nothing beyond confusing whoever reads the program.

A method can call other methods by going through method attributes of the `self` argument:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

```

Methods can reach global names exactly as plain functions do. The global scope tied to a method is the module where its definition lives. (A class is never employed as a global scope.) Although a solid justification for using global data inside a method is hard to come by, the global scope has plenty of legitimate purposes: for one, functions and modules brought into the global scope by import are usable from methods, as are functions and classes defined there. Commonly the class that holds the method is itself defined in this global scope, and in the upcoming section we'll uncover some sound reasons a method might wish to reference its own class.

Every value is an object and thus carries a *class* (otherwise termed its *type*). That is held in `object.__class__`.

[Subject index](INDEX.md) · [Previous source section](class-and-instance-variables.md) · [Following source section](inheritance.md)

# What’s New in Python 2.2 / PEPs 252 and 253: Type and Class Changes - collections

### PEPs 252 and 253: Type and Class Changes

The deepest and most sweeping revisions in Python 2.2 touch how Python models objects and classes. Because they were built to stay backward compatible, the odds are good that your existing code keeps running as-is, yet they unlock some genuinely remarkable abilities. Before diving into this — the lengthiest and trickiest portion of the whole article — let me sketch out the changes and add a few remarks.

Years back I put up a web page cataloguing the weak spots in Python’s design. Among the worst was the inability to subclass Python types that were coded in C. Built-in types specifically can’t be subclassed, so there’s no way to merely subclass, for instance, lists just to bolt on one handy method. The `UserList` module hands you a class that mirrors every list method and can be subclassed onward, yet plenty of C code demands an ordinary Python list and rejects a [`UserList`](https://docs.python.org/3.14/library/collections.html#collections.UserList) instance.

Python 2.2 corrects this, and along the way introduces some thrilling new powers. A quick rundown:

- Built-in types like lists, and even integers, can be subclassed, and those subclasses ought to function anywhere the original type is expected.

- Beyond the instance methods that earlier Python releases gave you, you can now declare static methods and class methods.

- A fresh facility called *properties* lets methods fire automatically when an instance attribute is read or assigned. Plenty of code that leaned on [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) can switch to properties, which leaves it both cleaner and quicker. A modest bonus: attributes are now allowed docstrings as well.

- By using *slots*, the set of attributes an instance may legally hold can be pinned to a chosen group of names, which guards against typos and might open the door to further optimizations down the road in Python.

A number of people have raised worries over the whole batch of changes. Granted, they admit, the additions are slick and invite all manner of tricks that earlier Python releases couldn’t manage — but they also pile more complexity onto the language. There’s a sentiment out there that Python was always praised for being simple, and that this simplicity is slipping away.

For my part, I see little cause for alarm. A good number of the additions are fairly arcane, and you can crank out plenty of Python without ever having to know they exist. Putting together a basic class stays exactly as easy as it always was, so there’s no reason to learn them or teach them until a real need arises. Certain very involved jobs that once demanded C can now be carried out in pure Python, and to my eye that’s a net win.

I won’t try to chase down every last edge case and tiny tweak that had to happen for the new machinery to work. This section instead sketches only the broad strokes. For more places to read up on Python 2.2’s reworked object model, head to the section Related Links, “Related Links”.

[Subject index](INDEX.md) · [Previous source section](introduction.md) · [Next source section](old-and-new-classes.md) · [Release/subject declaration](introduction.md)

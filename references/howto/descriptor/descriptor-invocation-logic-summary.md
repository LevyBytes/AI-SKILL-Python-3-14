# Descriptor invocation logic summary

### Summary of invocation logic
How descriptors fire is wired into the [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) methods belonging to [`object`](https://docs.python.org/3.14/library/functions.html#object), [`type`](https://docs.python.org/3.14/library/functions.html#type), and [`super()`](https://docs.python.org/3.14/library/functions.html#super).

Keep these key facts in mind:

- It is the [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) method that triggers descriptors.

- This machinery is inherited by classes from [`object`](https://docs.python.org/3.14/library/functions.html#object), [`type`](https://docs.python.org/3.14/library/functions.html#type), or [`super()`](https://docs.python.org/3.14/library/functions.html#super).

- Because every bit of the descriptor logic resides in that method, supplying your own [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) shuts off the automatic descriptor calls.

- The calls that `object.__getattribute__()` and `type.__getattribute__()` make to [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) differ. One passes the instance and possibly the class. The other substitutes `None` for the instance and always passes the class.

- Instance dictionaries are always overridden by data descriptors.

- Instance dictionaries can override non-data descriptors.

[Subject index](INDEX.md) · [Previous source context](invocation-from-super.md) · [Automatic name notification](automatic-name-notification.md) · [Previous source context](automatic-name-notification.md) · [Following source context](automatic-name-notification.md)

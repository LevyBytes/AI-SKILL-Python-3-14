# copyreg - Example

### Example

What follows demonstrates registering a pickle function and the way it gets applied:

```python
>>> import copyreg, copy, pickle
>>> class C:
...     def __init__(self, a):
...         self.a = a
...
>>> def pickle_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
>>> copyreg.pickle(C, pickle_c)
>>> c = C(1)
>>> d = copy.copy(c)
pickling a C instance...
>>> p = pickle.dumps(c)
pickling a C instance...

```

[Subject index](INDEX.md) · [Previous](copyreg-constructor-to-copyreg-pickle.md) · [Continue](../crypt/crypt-function-to-check-unix-passwords.md) · [Owning module, declaration or section: copyreg](copyreg-constructor-to-copyreg-pickle.md)

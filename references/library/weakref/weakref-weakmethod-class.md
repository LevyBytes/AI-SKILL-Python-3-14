# weakref: `weakref.WeakMethod`

*class *weakref.WeakMethod(*method*[, *callback*])

A bespoke `ref` subclass that imitates a weak reference to a bound method (that is, a method declared on a class and resolved against an instance). Because a bound method is so short-lived, an ordinary weak reference cannot retain it. `WeakMethod` carries dedicated code that rebuilds the bound method right up until either the object or the underlying function expires:

```python
>>> class C:
...     def method(self):
...         print("method called!")
...
>>> c = C()
>>> r = weakref.ref(c.method)
>>> r()
>>> r = weakref.WeakMethod(c.method)
>>> r()
<bound method C.method of <__main__.C object at 0x7fc859830220>>
>>> r()()
method called!
>>> del c
>>> gc.collect()
0
>>> r()
>>>

```

Here too, *callback* corresponds to the identically named parameter of the `ref()` function.

Added in version 3.4.

[Subject index](INDEX.md) · [Previous](weakref-weakset-class.md) · [Continue](weakref-finalize-class-to-weakref-finalize-peek.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md)

# object.__new__(*cls*[, *...*])

### 3.3.1. Basic customization

 object.__new__(*cls*[, *...*])

Invoked to produce a fresh instance of class *cls*. `__new__()` is a static method (handled as a special case, so you do not have to declare it that way) that receives, as its first argument, the class an instance of which was requested. Whatever remains are the arguments handed to the object constructor expression (the call upon the class). What `__new__()` returns should be the freshly made object instance (typically an instance of *cls*).

A common implementation makes a new instance of the class by calling the superclass’s `__new__()` method via `super().__new__(cls[, ...])` with suitable arguments, then adjusts the freshly built instance as required before handing it back.

When `__new__()` runs during object construction and hands back an instance of *cls*, the new instance’s `__init__()` method is then invoked as `__init__(self[, ...])`, where *self* refers to the new instance and the rest of the arguments match those that were given to the object constructor.

Should `__new__()` not hand back an instance of *cls*, the new instance’s `__init__()` method goes uninvoked.

`__new__()` exists chiefly so that subclasses of immutable types (such as int, str, or tuple) can tailor how instances are created. It is also frequently overridden within custom metaclasses so as to tailor class creation.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](special-method-names.md) · [Following source section](object-init.md)

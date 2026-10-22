# The Basics — PyObject_HEAD, PyObject, Py_TYPE, Py_REFCNT, PyFloatObject, PyTypeObject, PyVarObject_HEAD_INIT, tp_name, tp_doc, PyDoc_STR, tp_basicsize, tp_itemsize, tp_flags, Py_TPFLAGS_DEFAULT, tp_new, PyType_GenericNew

```c
typedef struct {
    PyObject_HEAD
} CustomObject;

```

That spells out the contents of a Custom object. `PyObject_HEAD` is required at the head of every object struct and introduces a field named `ob_base` of type [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject), which carries a reference count alongside a pointer to a type object (you reach these through the macros [`Py_TYPE`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) and [`Py_REFCNT`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT), respectively). The macro exists to hide the underlying layout and to make room for extra fields in [debug builds](https://docs.python.org/3.14/using/configure.html#debug-build).

Note

Notice that no semicolon trails the [`PyObject_HEAD`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject_HEAD) macro above. Take care not to slip one in by mistake: certain compilers will object.

Naturally, most objects carry extra data on top of the usual `PyObject_HEAD` scaffolding; as an illustration, this is how the standard Python float is declared:

```c
typedef struct {
    PyObject_HEAD
    double ob_fval;
} PyFloatObject;

```

The second piece is where the type object gets defined.

```c
static PyTypeObject CustomType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
};

```

Note

Our advice is to lean on C99-style designated initializers like the ones shown, since they spare you from spelling out every [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) field you have no interest in and also free you from worrying about the order in which the fields are declared.

In `object.h`, the genuine [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) declaration carries far more [fields](https://docs.python.org/3.14/c-api/typeobj.html#type-structs) than what appears above. The C compiler zero-fills any fields left out, and skipping the ones you don’t actually need is the usual convention.

Let’s work through it field by field:

```c
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)

```

That line is required boilerplate that initializes the `ob_base` field described earlier.

```c
.tp_name = "custom.Custom",

```

This gives our type its name. It surfaces in the default text rendering of our objects and within certain error messages, like so:

```pycon
>>> "" + custom.Custom()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "custom.Custom") to str

```

Keep in mind that the name is dotted, bundling together both the module name and the name the type has inside that module. Here the module is `custom` and the type is `Custom`, hence we assign the type name `custom.Custom`. Supplying the true dotted import path matters because it keeps your type interoperable with the [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) and [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) modules.

```c
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,

```

These tell Python the amount of memory to set aside whenever it builds a new `Custom` instance. The [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize) field matters only for variable-sized objects and should stay zero otherwise.

Note

Suppose you want Python subclasses of your type, and your type shares the same [`tp_basicsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_basicsize) as its base type; multiple inheritance can then trip you up. A Python subclass of your type has to name your type first in its [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__), otherwise calling your type’s [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method will raise an error. Sidestep the whole issue by giving your type a `tp_basicsize` value that exceeds its base type’s. That holds anyway most of the time, because your base type is either [`object`](https://docs.python.org/3.14/library/functions.html#object) or else a type you’re extending with extra data members, which grows its size.

For the class flags we use [`Py_TPFLAGS_DEFAULT`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_DEFAULT).

[Subject index](INDEX.md) · [Previous source section](the-basics-and-pymoduledef-init.md) · [Next source section](the-basics-and-pymodule-addobjectref.md) · [Owning section and setup](the-basics-and-pymoduledef-init.md)

# Abstract Protocol Support — PyNumberMethods, tp_as_number, PySequenceMethods, tp_as_sequence, PyMappingMethods, tp_as_mapping, tp_hash, Py_hash_t, PyObject, PyTypeObject, tp_call, PyArg_ParseTuple, PyArg_ParseTupleAndKeywords

### 3.5. Abstract Protocol Support

A range of *abstract* 'protocols' is supported by Python; the particular interfaces offered for working with these interfaces are documented under [Abstract Objects Layer](https://docs.python.org/3.14/c-api/abstract.html#abstract).

Several of these abstract interfaces took shape early on in the Python implementation's development. The number, mapping, and sequence protocols in particular have belonged to Python right from the start. Further protocols arrived as time went on. Where a protocol leans on multiple handler routines from the type's implementation, the older ones were defined as optional handler blocks that the type object references. The newer protocols instead get extra slots within the primary type object, accompanied by a flag bit that's set to announce the slots are present and warrant checking by the interpreter. (Setting that flag bit doesn't mean the slot values are non-`NULL`. The flag may be set to advertise that a slot exists, yet the slot itself may remain unfilled.)

```c
PyNumberMethods   *tp_as_number;
PySequenceMethods *tp_as_sequence;
PyMappingMethods  *tp_as_mapping;

```

Should you want your object to behave like a number, a sequence, or a mapping object, you supply the address of a structure that implements the C type [`PyNumberMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyNumberMethods), [`PySequenceMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PySequenceMethods), or [`PyMappingMethods`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyMappingMethods), as the case may be. Populating that structure with sensible values is left to you. Examples of each in use are available within the `Objects` directory of the Python source distribution.

```c
hashfunc tp_hash;

```

Should you decide to supply this function, it ought to yield a hash number for an instance of your data type. A straightforward example follows:

```c
static Py_hash_t
newdatatype_hash(PyObject *op)
{
    newdatatypeobject *self = (newdatatypeobject *) op;
    Py_hash_t result;
    result = self->some_size + 32767 * self->some_number;
    if (result == -1) {
        result = -2;
    }
    return result;
}

```

[`Py_hash_t`](https://docs.python.org/3.14/c-api/hash.html#c.Py_hash_t) is a signed integer type whose width depends on the platform. A return of `-1` from [`tp_hash`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_hash) signals an error, so you'll want to take care not to hand it back when the hash computes successfully, as the example above shows.

```c
ternaryfunc tp_call;

```

Python invokes this function whenever an instance of your data type is "called"; for instance, if `obj1` is an instance of your data type and the Python script holds `obj1('hello')`, the [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call) handler is triggered.

Three arguments go to this function:

1.

*self* stands for the instance of the data type that the call targets. Where the call reads `obj1('hello')`, *self* is `obj1`.

2.

*args* is a tuple holding the call's arguments. To pull out those arguments you can rely on [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple).

3.

*kwds* is a dictionary holding whichever keyword arguments were supplied. When this is non-`NULL` and keyword arguments are something you support, turn to [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) to pull out the arguments. Should you not wish to support keyword arguments while this comes in as non-`NULL`, raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) carrying a message that states keyword arguments aren't supported.

[Subject index](INDEX.md) · [Previous source section](object-comparison-and-py-newref.md) · [Required Call and iterator protocol slots continuation](call-and-iterator-protocol-slots-and-pytypeobject.md)

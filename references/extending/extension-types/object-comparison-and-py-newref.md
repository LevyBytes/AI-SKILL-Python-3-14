# Object Comparison - tp_richcompare, PyTypeObject, PyObject_RichCompare, PyObject_RichCompareBool, Py_EQ, Py_NE, Py_LE, Py_GE, Py_LT, Py_GT, Py_True, Py_False, Py_NotImplemented, PyObject, Py_NewRef

### 3.4. Object Comparison

```c
richcmpfunc tp_richcompare;

```

Python fires the [`tp_richcompare`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_richcompare) handler whenever comparisons have to happen. It parallels the [rich comparison methods](https://docs.python.org/3.14/reference/datamodel.html#richcmpfuncs), such as `__lt__()`, and is likewise driven by [`PyObject_RichCompare()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompare) and [`PyObject_RichCompareBool()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_RichCompareBool).

Its arguments are two Python objects together with the operator, the operator being one of `Py_EQ`, `Py_NE`, `Py_LE`, `Py_GE`, `Py_LT` or `Py_GT`. It's expected to weigh the two objects against the supplied operator and yield `Py_True` or `Py_False` when the comparison goes through, `Py_NotImplemented` to signal that the comparison isn't implemented and the other object's comparison method ought to be attempted, or `NULL` should an exception have been set.

Below is a sample implementation, written for a datatype regarded as equal whenever the size of an internal pointer matches:

```c
static PyObject *
newdatatype_richcmp(PyObject *lhs, PyObject *rhs, int op)
{
    newdatatypeobject *obj1 = (newdatatypeobject *) lhs;
    newdatatypeobject *obj2 = (newdatatypeobject *) rhs;
    PyObject *result;
    int c, size1, size2;

    /* code to make sure that both arguments are of type
       newdatatype omitted */

    size1 = obj1->obj_UnderlyingDatatypePtr->size;
    size2 = obj2->obj_UnderlyingDatatypePtr->size;

    switch (op) {
    case Py_LT: c = size1 <  size2; break;
    case Py_LE: c = size1 <= size2; break;
    case Py_EQ: c = size1 == size2; break;
    case Py_NE: c = size1 != size2; break;
    case Py_GT: c = size1 >  size2; break;
    case Py_GE: c = size1 >= size2; break;
    }
    result = c ? Py_True : Py_False;
    return Py_NewRef(result);
 }

```

[Subject index](INDEX.md) · [Previous source section](type-specific-attribute-management-and-pyexc-runtimeerror.md) · [Next source section](abstract-protocol-support-and-pyarg-parsetupleandkeywords.md)

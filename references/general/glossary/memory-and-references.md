# Memory and references

Open when checking Python definitions for memory and references.

## reference count

How many references point at an object. Once an object's reference count falls to zero, it gets deallocated. Certain objects are immortal and carry reference counts that never change, so those objects are never deallocated. Python code generally does not see reference counting, but it stands as a key element of the CPython implementation. To get the reference count of a particular object, programmers can call the [`sys.getrefcount()`](https://docs.python.org/3.14/library/sys.html#sys.getrefcount) function.

Within CPython, reference counts are not held to be stable or well-defined figures; the count of references to an object, and the way Python code alters that count, may vary between versions.

## strong reference

Inside Python's C API, the term strong reference denotes a reference whose owner is the very code that holds onto it. You take a strong reference by calling [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) at the moment the reference is created, and you release it with [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) when the reference is deleted.

You can mint a strong reference to an object with the [`Py_NewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef) function. As a rule, the [`Py_DECREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_DECREF) function has to be called on the strong reference before you leave its scope, so as not to leak a reference.

See also borrowed reference.

## borrowed reference

Within Python's C API, a borrowed reference points at an object while the code working with that object does not own the reference. It turns into a dangling pointer should the object be destroyed. As an example, a garbage collection may drop the object's final strong reference and thereby destroy it.

Invoking [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) on the borrowed reference is the advised way to promote it to a strong reference in place, the exception being when the object cannot be destroyed prior to the borrowed reference's last use. You can build a fresh strong reference with the [`Py_NewRef()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_NewRef) function.

## immortal

*Immortal objects* are a CPython implementation detail brought in by [**PEP 683**](https://peps.python.org/pep-0683/).

When an object is immortal, its reference count never gets altered, and so it is never freed for as long as the interpreter keeps running. For instance, [`True`](https://docs.python.org/3.14/library/constants.html#True) and [`None`](https://docs.python.org/3.14/library/constants.html#None) are immortal under CPython.

You can recognize immortal objects through [`sys._is_immortal()`](https://docs.python.org/3.14/library/sys.html#sys._is_immortal), or in the C API through [`PyUnstable_IsImmortal()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_IsImmortal).

## garbage collection

The act of reclaiming memory once it has stopped being used. Python carries out garbage collection through reference counting together with a cyclic garbage collector capable of spotting and severing reference cycles. Control over the garbage collector is available through the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module.

## cyclic isolate

A cluster of one or more objects that point at each other through a reference cycle while no object outside the cluster points at them. The cyclic garbage collector aims to spot these clusters and sever the reference cycles, allowing the memory to be reclaimed.

[Glossary context index](INDEX.md).

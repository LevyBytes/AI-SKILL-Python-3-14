# Attribute Management — PyObject, tp_getattr, tp_setattr, tp_getattro, tp_setattro

### 3.3. Attribute Management

Any object capable of holding attributes needs its type to supply the functions that govern how those attributes get resolved. One function is required to fetch attributes (assuming some are defined), with a second to assign attributes (assuming assignment is permitted). Deleting an attribute is handled as a special situation, signalled by the handler receiving `NULL` as the new value.

There are two pairs of attribute handlers offered by Python; a type holding attributes needs to implement just one of the pairs. The distinction is that one pair receives the attribute's name as a char*, whereas the other takes a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. Whichever pair best suits the convenience of the implementation is the one a given type may adopt.

```c
getattrfunc  tp_getattr;        /* char * version */
setattrfunc  tp_setattr;
/* ... */
getattrofunc tp_getattro;       /* PyObject * version */
setattrofunc tp_setattro;

```

Whenever reaching an object's attributes is consistently a simple operation (something covered in just a moment), generic implementations are on hand to furnish the [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* version of the attribute management functions. From Python 2.2 onward, the genuine call for type-specific attribute handlers has nearly vanished, even though plenty of examples remain that haven't been revised to adopt some of the new generic machinery now on offer.

[Subject index](INDEX.md) · [Previous source section](object-repr-and-string-presentation.md) · [Next source section](generic-attribute-management-and-py-readonly.md)

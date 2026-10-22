# `PyDict_Next`

#### `PyDict_Next`

One clear outlier is [`PyDict_Next()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Next): it leaves the dictionary unlocked. When the dictionary could be altered by another thread mid-iteration, wrap your loop in [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3.14/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION) to guard it:

```c
Py_BEGIN_CRITICAL_SECTION(dict);
PyObject *key, *value;
Py_ssize_t pos = 0;
while (PyDict_Next(dict, &pos, &key, &value)) {
    ...
}
Py_END_CRITICAL_SECTION();

```

[Subject index](INDEX.md) · [Previous source context](container-thread-safety.md) · [Following source context](borrowed-references.md)

# What’s New In Python 3.12 / PEP 684: A Per-Interpreter GIL

> (Contributed by Pablo Galindo, Batuhan Taskaya, Lysandros Nikolaou, Cristián Maureira-Fredes and Marta Gómez in [gh-102856](https://github.com/python/cpython/issues/102856). PEP written by Pablo Galindo, Batuhan Taskaya, Lysandros Nikolaou and Marta Gómez).

### PEP 684: A Per-Interpreter GIL

A per-interpreter [GIL](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) arrives with [**PEP 684**](https://peps.python.org/pep-0684/), letting sub-interpreters now be created each holding its own GIL. Through this, Python programs can fully exploit several CPU cores. At present this is reachable solely via the C-API, although a Python API is [**anticipated for 3.13**](https://peps.python.org/pep-0554/).

Use the new [`Py_NewInterpreterFromConfig()`](https://docs.python.org/3.14/c-api/subinterpreters.html#c.Py_NewInterpreterFromConfig) function to create an interpreter with its own GIL:

```c
PyInterpreterConfig config = {
    .check_multi_interp_extensions = 1,
    .gil = PyInterpreterConfig_OWN_GIL,
};
PyThreadState *tstate = NULL;
PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config);
if (PyStatus_Exception(status)) {
    return -1;
}
/* The new interpreter is now active in the current thread. */

```

To see more samples of driving the C-API for sub-interpreters that each own a GIL, consult `Modules/_xxsubinterpretersmodule.c`.

(Contributed by Eric Snow in [gh-104210](https://github.com/python/cpython/issues/104210), etc.)

[Subject index](INDEX.md) · [Previous source section](pep-701-syntactic-formalization-of-f-strings.md) · [Next source section](pep-669-low-impact-monitoring-for-cpython.md) · [Release/subject declaration](summary-release-highlights.md)

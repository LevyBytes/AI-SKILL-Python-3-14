# Providing a C API for an Extension Module - PyObject

```c
static int
client_module_exec(PyObject *m)
{
    if (import_spam() < 0) {
        return -1;
    }
    /* additional initialization can happen here */
    return 0;
}

```

This approach's chief drawback is how involved the `spammodule.h` file ends up being. That said, the underlying pattern repeats unchanged for every exported function, so you only have to grasp it a single time.

One last point worth noting is that Capsules bring extra capabilities, particularly handy for allocating and freeing the pointer a Capsule keeps. You will find the specifics laid out in the Python/C API Reference Manual under the section [Capsules](https://docs.python.org/3.14/c-api/capsule.html#capsules), as well as in the Capsule implementation itself (the `Include/pycapsule.h` and `Objects/pycapsule.c` files within the Python source code distribution).

Footnotes

[Subject index](INDEX.md) · [Previous source section](capsule-api-pointer-initialization.md) · [Owning section and setup](providing-a-c-api-for-an-extension-module-and-py-mod-exec.md)

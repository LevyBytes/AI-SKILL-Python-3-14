# Providing a C API for an Extension Module — PyObject, PySpam_API, PySpam_API_pointers, PySpam_System_NUM, PySpam_System, PyCapsule_New, PyModule_Add, PyInit_spam, Py_SPAMMODULE_H, PySpam_System_RETURN, PySpam_System_PROTO, PyCapsule_Import, Py_mod_exec

```c
static int
spam_module_exec(PyObject *m)
{
    static void *PySpam_API[PySpam_API_pointers];
    PyObject *c_api_object;

    /* Initialize the C API pointer array */
    PySpam_API[PySpam_System_NUM] = (void *)PySpam_System;

    /* Create a Capsule containing the API pointer array's address */
    c_api_object = PyCapsule_New((void *)PySpam_API, "spam._C_API", NULL);

    if (PyModule_Add(m, "_C_API", c_api_object) < 0) {
        return -1;
    }

    return 0;
}

```

Observe that `PySpam_API` carries the `static` declaration; without it, the pointer array would vanish the instant `PyInit_spam()` returns!

Most of the heavy lifting lives inside the `spammodule.h` header file, shown below:

```c
#ifndef Py_SPAMMODULE_H
#define Py_SPAMMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

/* Header file for spammodule */

/* C API functions */
#define PySpam_System_NUM 0
#define PySpam_System_RETURN int
#define PySpam_System_PROTO (const char *command)

/* Total number of C API pointers */
#define PySpam_API_pointers 1

#ifdef SPAM_MODULE
/* This section is used when compiling spammodule.c */

static PySpam_System_RETURN PySpam_System PySpam_System_PROTO;

#else
/* This section is used in modules that use spammodule's API */

static void **PySpam_API;

#define PySpam_System \
 (*(PySpam_System_RETURN (*)PySpam_System_PROTO) PySpam_API[PySpam_System_NUM])

/* Return -1 on error, 0 on success.
 * PyCapsule_Import will set an exception if there's an error.
 */
static int
import_spam(void)
{
    PySpam_API = (void **)PyCapsule_Import("spam._C_API", 0);
    return (PySpam_API != NULL) ? 0 : -1;
}

#endif

#ifdef __cplusplus
}
#endif

#endif /* !defined(Py_SPAMMODULE_H) */

```

To gain access to the `PySpam_System()` function, the only thing a client module has to do is invoke the `import_spam()` function (more precisely, macro) within its [`mod_exec`](https://docs.python.org/3.14/c-api/module.html#c.Py_mod_exec) function:

[Subject index](INDEX.md) · [Previous source section](providing-a-c-api-for-an-extension-module-and-py-mod-exec.md) · [Next source section](providing-a-c-api-for-an-extension-module-pyobject.md) · [Owning section and setup](providing-a-c-api-for-an-extension-module-and-py-mod-exec.md)

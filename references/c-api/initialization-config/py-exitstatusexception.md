# void Py_ExitStatusException(PyStatus status)

void Py_ExitStatusException(PyStatus status)

When *status* is an exit, invoke `exit(exitcode)`. When *status* is an error, print its error message and quit with a non-zero exit code. Invoke this only when `PyStatus_Exception(status)` is non-zero.

Note

Under the hood, Python relies on macros that populate `PyStatus.func`, while the status-creation functions leave `func` as `NULL`.

Example:

```c
PyStatus alloc(void **ptr, size_t size)
{
    *ptr = PyMem_RawMalloc(size);
    if (*ptr == NULL) {
        return PyStatus_NoMemory();
    }
    return PyStatus_Ok();
}

int main(int argc, char **argv)
{
    void *ptr;
    PyStatus status = alloc(&ptr, 16);
    if (PyStatus_Exception(status)) {
        Py_ExitStatusException(status);
    }
    PyMem_Free(ptr);
    return 0;
}

```

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pystatus-to-pystatus-isexit.md) · [Following source contract](pypreconfig-to-configure-locale.md)

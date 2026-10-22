# PyStatus

### PyStatus

 type PyStatus

A structure that records the status of an initialization function: success, error, or exit.

In the error case, it can keep the name of the C function that produced the error.

Structure fields:

 int exitcode

Exit code. The argument handed to `exit()`.

 const char *err_msg

Error message.

 const char *func

The name of the function that produced an error; may be `NULL`.

Functions to create a status:

 PyStatus PyStatus_Ok(void)

Success.

 PyStatus PyStatus_Error(const char *err_msg)

An initialization error carrying a message.

A non-`NULL` value is required for *err_msg*.

 PyStatus PyStatus_NoMemory(void)

A memory allocation failure (out of memory).

 PyStatus PyStatus_Exit(int exitcode)

Quit Python using the given exit code.

Functions to handle a status:

 int PyStatus_Exception(PyStatus status)

Does the status represent an error or an exit? When true, the exception has to be dealt with, for instance through a `Py_ExitStatusException()` call.

 int PyStatus_IsError(PyStatus status)

Does the result represent an error?

 int PyStatus_IsExit(PyStatus status)

Does the result represent an exit?

[Subject index](INDEX.md) · [Previous source contract](pywidestringlist-to-items.md) · [Following source contract](py-exitstatusexception.md)

# Python 3.11.0 alpha 1 / c api / threads

[bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947): Drop the 4 private trashcan C API functions that survived solely for stable ABI backward compatibility with Python 3.8 and earlier, because the trashcan API could not be used through the limited C API on Python 3.8 and earlier. From Python 3.9 onward, the trashcan API was kept out of the limited C API.

Removed functions:

  - _PyTrash_deposit_object()

  - _PyTrash_destroy_chain()

  - _PyTrash_thread_deposit_object()

  - _PyTrash_thread_destroy_chain()

The trashcan C API could never work through the limited C API, because the old trashcan macros reached straight into [`PyThreadState`](https://docs.python.org/3.14/c-api/threads.html#c.PyThreadState) members such as `_tstate->trash_delete_nesting`, while under the limited C API the `PyThreadState` structure stays opaque.

The `PyTrash_UNWIND_LEVEL` constant is likewise excluded from the C API.

Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 1 / library / threads and concurrency

[bpo-44434](https://bugs.python.org/issue?@action=redirect&bpo=44434): _thread.start_new_thread() no longer makes a redundant explicit call to PyThread_exit_thread() as a thread exits. On Linux running glibc, pthread_exit() will abort the entire process should dlopen() be unable to open the libgcc_s.so file (for instance an EMFILE error). Victor Stinner wrote the patch.

[bpo-44962](https://bugs.python.org/issue?@action=redirect&bpo=44962): Resolve a race within WeakKeyDictionary, WeakValueDictionary and WeakSet that arose when two threads both tried to finalize the final pending removal. This repairs asyncio.create_task and fixes a data loss within asyncio.run where shutdown_asyncgens does not run

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

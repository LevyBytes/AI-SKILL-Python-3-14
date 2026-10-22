# Python 3.8.0 beta 1 / library / thread interrupt main refrains setting python error status sigint signal either

[bpo-23395](https://bugs.python.org/issue?@action=redirect&bpo=23395): `_thread.interrupt_main()` now refrains from setting the Python error status when the `SIGINT` signal is either ignored or left unhandled by Python.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

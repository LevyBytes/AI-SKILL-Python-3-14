# C Entry Points

### C Entry Points

So that firing DTrace markers stays straightforward, Python’s C API ships several helper functions, one per static marker. Where Python was compiled without DTrace turned on, those helpers are no-ops.

You normally have no reason to invoke them on your own, since Python takes care of that for you.

| C API Function | Static Marker | Notes |
| --- | --- | --- |
| void PyDTrace_LINE(const char *arg0, const char *arg1, int arg2) | `line()` |  |
| void PyDTrace_FUNCTION_ENTRY(const char *arg0, const char *arg1, int arg2) | `function__entry()` |  |
| void PyDTrace_FUNCTION_RETURN(const char *arg0, const char *arg1, int arg2) | `function__return()` |  |
| void PyDTrace_GC_START(int arg0) | `gc__start()` |  |
| void PyDTrace_GC_DONE(Py_ssize_t arg0) | `gc__done()` |  |
| void PyDTrace_INSTANCE_NEW_START(int arg0) | `instance__new__start()` | Not used by Python |
| void PyDTrace_INSTANCE_NEW_DONE(int arg0) | `instance__new__done()` | Not used by Python |
| void PyDTrace_INSTANCE_DELETE_START(int arg0) | `instance__delete__start()` | Not used by Python |
| void PyDTrace_INSTANCE_DELETE_DONE(int arg0) | `instance__delete__done()` | Not used by Python |
| void PyDTrace_IMPORT_FIND_LOAD_START(const char *arg0) | `import__find__load__start()` |  |
| void PyDTrace_IMPORT_FIND_LOAD_DONE(const char *arg0, int arg1) | `import__find__load__done()` |  |
| void PyDTrace_AUDIT(const char *arg0, void *arg1) | `audit()` |  |

[Subject index](INDEX.md) · [Previous source context](available-static-markers.md) · [Following source context](c-probing-checks.md)

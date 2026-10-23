# Audit events table - Section introduction and initial examples

# Audit Events

### Audit events table

Every event raised by [`sys.audit()`](https://docs.python.org/3.14/library/sys.html#sys.audit) or [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) calls across the CPython runtime and the standard library appears in this table. Such calls arrived in 3.8 or later (refer to [**PEP 578**](https://peps.python.org/pep-0578/)).

For details on processing these events, consult [`sys.addaudithook()`](https://docs.python.org/3.14/library/sys.html#sys.addaudithook) and [`PySys_AddAuditHook()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_AddAuditHook).

**CPython implementation detail:** Because this table comes from the CPython documentation, it may not cover events raised by other implementations. Check the documentation specific to your runtime for the events it actually raises.

[Subject index](INDEX.md) · [Continue](audit-events-table-thread.md)

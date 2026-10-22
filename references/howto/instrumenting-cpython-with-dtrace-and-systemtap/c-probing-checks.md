# C Probing Checks

### C Probing Checks

 int PyDTrace_LINE_ENABLED(void)

 int PyDTrace_FUNCTION_ENTRY_ENABLED(void)

 int PyDTrace_FUNCTION_RETURN_ENABLED(void)

 int PyDTrace_GC_START_ENABLED(void)

 int PyDTrace_GC_DONE_ENABLED(void)

 int PyDTrace_INSTANCE_NEW_START_ENABLED(void)

 int PyDTrace_INSTANCE_NEW_DONE_ENABLED(void)

 int PyDTrace_INSTANCE_DELETE_START_ENABLED(void)

 int PyDTrace_INSTANCE_DELETE_DONE_ENABLED(void)

 int PyDTrace_IMPORT_FIND_LOAD_START_ENABLED(void)

 int PyDTrace_IMPORT_FIND_LOAD_DONE_ENABLED(void)

 int PyDTrace_AUDIT_ENABLED(void)

Every invocation of a `PyDTrace` function has to be protected by first calling one of these. That lets Python keep the performance cost low whenever probing is switched off.

Where DTrace was not enabled at build time, these functions are no-ops and hand back `0`.

[Subject index](INDEX.md) · [Previous source context](c-entry-points.md) · [Following source context](systemtap-tapsets.md)

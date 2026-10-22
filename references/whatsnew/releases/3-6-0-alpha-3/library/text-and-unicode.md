# Python 3.6.0 alpha 3 / library / text and unicode

[bpo-22115](https://bugs.python.org/issue?@action=redirect&bpo=22115): The tkinter.Variable class gained the methods trace_add, trace_remove and trace_info. These supersede the older trace_variable, trace, trace_vdelete and trace_vinfo methods, which rely on outdated Tcl commands and may break in later Tcl releases. The legacy tracing methods were repaired too: trace_vdelete() handed a wrong mode no longer breaks tracing, trace_vinfo() reliably hands back a list of string pairs, and tracing under the "u" mode now functions.

[bpo-26754](https://bugs.python.org/issue?@action=redirect&bpo=26754): A handful of functions (compile() and friends) used to take a filename argument given as an iterable of integers. From now on only strings and byte-like objects are permitted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# 14.1. Tab Completion and History Editing

### 14.1. Tab Completion and History Editing

Completing variable and module names is [automatically enabled](https://docs.python.org/3.14/library/site.html#rlcompleter-config) the moment the interpreter starts, so pressing the Tab key triggers the completion function; it consults Python statement names, the local variables in scope, and whatever module names are reachable. With a dotted expression like `string.a`, it evaluates everything up to the trailing `'.'` and then proposes completions drawn from the attributes of whatever object results. Keep in mind that application-defined code may run here if the expression involves an object carrying a [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) method. By default your history is also written out to a file called `.python_history` sitting in your user directory. That history comes back the next time you open an interactive interpreter session.

[Subject index](INDEX.md) · [Previous source section](interactive-input-editing-and-history-substitution.md) · [Following source section](alternatives-to-the-interactive-interpreter.md)

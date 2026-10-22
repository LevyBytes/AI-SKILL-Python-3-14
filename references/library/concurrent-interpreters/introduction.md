# concurrent.interpreters — Introduction

### Introduction

In essence an “interpreter” is the Python runtime’s execution context. Within it lives every bit of state the runtime requires to run a program, the import state and builtins among them. (Every thread — even when only the main thread exists — carries a little extra runtime state beyond the current interpreter, tied to the active exception and the bytecode eval loop.)

Interpreters as an idea and a feature have ridden along with Python since release 2.2, yet the capability was reachable only via the C-API, stayed obscure, and its isolation remained fairly partial right up to release 3.12.

[Subject index](INDEX.md) · [Previous](key-details.md) · [Continue](multiple-interpreters-and-isolation.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)

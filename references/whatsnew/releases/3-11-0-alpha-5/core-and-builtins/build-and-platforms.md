# Python 3.11.0 alpha 5 / core and builtins / build and platforms

[bpo-46329](https://bugs.python.org/issue?@action=redirect&bpo=46329): Most calls now compile down to either two or three bytecodes.

When no named arguments appear, a call expands into a pair of instructions: `PRECALL; CALL`. When named arguments are present, three instructions are emitted: `PRECALL; KW_NAMES; CALL`. Two distinct `PRECALL` forms exist: `PRECALL_FUNTION` together with `PRECALL_METHOD`. That second one is the partner of `LOAD_METHOD`.

Splitting the work between a pre-call step and the call itself opens the door to sharper specialization, and so to stronger performance overall.

Semantics stay exactly the same.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

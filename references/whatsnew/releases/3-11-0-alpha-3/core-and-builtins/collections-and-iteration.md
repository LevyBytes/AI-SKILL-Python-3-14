# Python 3.11.0 alpha 3 / core and builtins / collections and iteration

[bpo-46009](https://bugs.python.org/issue?@action=redirect&bpo=46009): Bring back the behavior seen in 3.9 and prior releases when a non-None value is sent to a freshly started generator. Under 3.9, the generator's state was left untouched by this. With both 3.10.0 and 3.10.1, `gen_func().send(0)` behaves the same as `gen_func().throw(TypeError(...)`, which drains the generator. Starting from 3.10.2, the prior 3.9 semantics were restored.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.11.0 alpha 7 / core and builtins / dis

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Adjust [`STORE_SUBSCR`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_SUBSCR) so an inline cache entry — not its oparg — serves as the adaptive counter.

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Switch `PRECALL` and [`CALL`](https://docs.python.org/3.14/library/dis.html#opcode-CALL) to inline caching, then tear out the internal plumbing that handled the now-unused non-inline caches.

[bpo-47186](https://bugs.python.org/issue?@action=redirect&bpo=47186): Swap out `JUMP_IF_NOT_EG_MATCH` in favor of [`CHECK_EG_MATCH`](https://docs.python.org/3.14/library/dis.html#opcode-CHECK_EG_MATCH) plus a jump.

[bpo-47186](https://bugs.python.org/issue?@action=redirect&bpo=47186): Swap out `JUMP_IF_NOT_EXC_MATCH` in favor of [`CHECK_EXC_MATCH`](https://docs.python.org/3.14/library/dis.html#opcode-CHECK_EXC_MATCH) plus a jump.

[bpo-47120](https://bugs.python.org/issue?@action=redirect&bpo=47120): The absolute-jump opcode [`JUMP_NO_INTERRUPT`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_NO_INTERRUPT) gives way to the relative form [`JUMP_BACKWARD_NO_INTERRUPT`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_BACKWARD_NO_INTERRUPT).

[bpo-47120](https://bugs.python.org/issue?@action=redirect&bpo=47120): Substituted the relative jump [`JUMP_BACKWARD`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_BACKWARD) for `JUMP_ABSOLUTE`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

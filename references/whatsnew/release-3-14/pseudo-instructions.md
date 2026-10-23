# What's new in Python 3.14 / Pseudo-instructions - dis, sys.monitoring

### Pseudo-instructions

- Introduce the `ANNOTATIONS_PLACEHOLDER` pseudo instruction that backs partially executed module-level annotations whose evaluation is deferred. (Contributed by Jelle Zijlstra in [gh-130907](https://github.com/python/cpython/issues/130907).)

- Introduce the `BINARY_OP_EXTEND` pseudo instruction, which runs a guard function paired with a specialization function, both fetched from the inline cache. (Contributed by Irit Katriel in [gh-100239](https://github.com/python/cpython/issues/100239).)

- Introduce three specializations covering [`CALL_KW`](https://docs.python.org/3.14/library/dis.html#opcode-CALL_KW): `CALL_KW_PY` for calls into Python functions, `CALL_KW_BOUND_METHOD` for calls into bound methods, and `CALL_KW_NON_PY` covering everything else. (Contributed by Mark Shannon in [gh-118093](https://github.com/python/cpython/issues/118093).)

- Introduce the [`JUMP_IF_TRUE`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_IF_TRUE) and [`JUMP_IF_FALSE`](https://docs.python.org/3.14/library/dis.html#opcode-JUMP_IF_FALSE) pseudo instructions, branches taken on a condition that leave the stack untouched. The sequence `COPY 1`, `TO_BOOL`, `POP_JUMP_IF_TRUE/FALSE` takes their place. (Contributed by Irit Katriel in [gh-124285](https://github.com/python/cpython/issues/124285).)

- Introduce the `LOAD_CONST_MORTAL` pseudo instruction. (Contributed by Mark Shannon in [gh-128685](https://github.com/python/cpython/issues/128685).)

- Introduce the [`LOAD_CONST_IMMORTAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_CONST_IMMORTAL) pseudo instruction, behaving like `LOAD_CONST` yet running faster for immortal objects. (Contributed by Mark Shannon in [gh-125837](https://github.com/python/cpython/issues/125837).)

- Introduce the [`NOT_TAKEN`](https://docs.python.org/3.14/library/dis.html#opcode-NOT_TAKEN) pseudo instruction, which [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring) employs when logging branch events (for instance [`BRANCH_LEFT`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT)). (Contributed by Mark Shannon in [gh-122548](https://github.com/python/cpython/issues/122548).)

[Subject index](INDEX.md) · [Previous source section](cpython-bytecode-changes.md) · [Next source section](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](summary-release-highlights.md)

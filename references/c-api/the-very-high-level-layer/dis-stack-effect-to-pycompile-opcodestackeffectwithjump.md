# Stack Effects

### Stack Effects

See also

[`dis.stack_effect()`](https://docs.python.org/3.14/library/dis.html#dis.stack_effect)

 PY_INVALID_STACK_EFFECT

A sentinel value standing for an invalid stack effect.

At present this is the same as `INT_MAX`.

Added in version 3.8.

 int PyCompile_OpcodeStackEffect(int opcode, int oparg)

Works out the stack effect of *opcode* when given argument *oparg*.

When it succeeds, the function returns the stack effect; when it fails, it returns `PY_INVALID_STACK_EFFECT`.

Added in version 3.4.

 int PyCompile_OpcodeStackEffectWithJump(int opcode, int oparg, int jump)

Behaves like `PyCompile_OpcodeStackEffect()`, except it leaves out the stack effect of jumping when *jump* is zero.

When *jump* is `0`, the stack effect of jumping is left out, but when *jump* is `1` or `-1`, it is folded in.

When it succeeds, the function returns the stack effect; when it fails, it returns `PY_INVALID_STACK_EFFECT`.

Added in version 3.8.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyrun-anyfile-to-pyrun-interactiveloopflags.md) · [Previous source contract](py-eval-input-to-ast-functiontype.md)

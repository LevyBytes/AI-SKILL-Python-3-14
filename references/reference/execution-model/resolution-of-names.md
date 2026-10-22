# 4.2.2. Resolution of names

### 4.2.2. Resolution of names

A *scope* fixes where a name is visible inside a block. When a local variable is defined within a block, that block falls inside its scope. Where the definition sits in a function block, the scope reaches into any blocks nested inside the defining one — unless one of those nested blocks sets up its own binding for the name.

A name used in a code block gets resolved by way of the nearest enclosing scope. We call the collection of every such scope reachable from a code block the block's *environment*.

Should a name turn up nowhere, a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception gets raised. When the current scope is a function scope and the name denotes a local variable not yet bound to a value at the spot where it is used, an [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) exception gets raised instead. `UnboundLocalError` is a subclass of `NameError`.

Should a name binding operation appear anywhere inside a code block, every use of that name within the block is taken as a reference to the current block. That can produce errors when the name is used in a block before it has been bound. The rule is a subtle one. Python has no declarations and lets name binding operations happen anywhere within a code block. You can work out a code block's local variables by scanning the block's whole text for name binding operations. Refer to [the FAQ entry on UnboundLocalError](https://docs.python.org/3.14/faq/programming.html#faq-unboundlocalerror) for worked examples.

Where a [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) statement appears inside a block, every use of the names it lists refers to the bindings of those names in the top-level namespace. Resolving names in the top-level namespace means searching the global namespace — that is, the namespace of the module that holds the code block — together with the builtins namespace, which is the namespace of the module [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins). The global namespace gets searched first. Failing to find the names there, the search moves on to the builtins namespace. Should the builtins namespace not turn them up either, fresh variables are created in the global namespace. Every use of the listed names must come after the global statement.

The scope of the [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) statement matches that of a name binding operation within the same block. When a free variable's nearest enclosing scope holds a global statement, that free variable is taken to be a global.

What the [`nonlocal`](https://docs.python.org/3.14/reference/simple_stmts.html#nonlocal) statement does is make the corresponding names point at variables already bound in the nearest enclosing function scope. A [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) gets raised at compile time should the supplied name not be present in any enclosing function scope. [Type parameters](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) cannot be rebound with the `nonlocal` statement.

A module's namespace gets created automatically the very first time the module is imported. A script's main module always goes by the name [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__).

In the matter of name resolution, class definition blocks and the arguments to [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) and [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) are special cases. A class definition is an executable statement that is free to use and to define names. Those references obey the ordinary name resolution rules, except that unbound local variables get looked up in the global namespace. The class definition's namespace turns into the attribute dictionary of the class. Names defined inside a class block are scoped to that class block alone; their scope does not reach the code blocks of methods. That covers comprehensions and generator expressions, but it leaves out annotation scopes, which can reach their enclosing class scopes. Consequently, the following will fail:

```python
class A:
    a = 42
    b = list(a + i for i in range(10))

```

However, the following will succeed:

```python
class A:
    type Alias = Nested
    class Nested: pass

print(A.Alias.__value__)  # <type 'A.Nested'>

```

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](binding-of-names.md) · [Previous source section](binding-of-names.md) · [Following source section](annotation-scopes.md)

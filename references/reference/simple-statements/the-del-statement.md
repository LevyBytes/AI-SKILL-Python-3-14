# 7.5. The `del` statement

### 7.5. The `del` statement

```text

del_stmt: "del" target_list
```

Deletion has a recursive definition that closely mirrors the way assignment is defined. Rather than laying it all out exhaustively, what follows are a few pointers.

Deleting a target list recursively deletes each of its targets, proceeding left to right.

Deleting a name strips the binding of that name out of the local or global namespace, hinging on whether the name shows up in a `global` statement inside the same code block. Attempting to delete a name that is unbound raises a [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError) exception.

Deleting attribute references and subscriptions is handed off to the primary object concerned; deleting a slicing is broadly the same as assigning an empty slice of the appropriate type (yet even this hinges on the sliced object).

Changed in version 3.2: Before this, deleting a name out of the local namespace was illegal whenever that name showed up as a free variable inside a nested block.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Previous source section](the-pass-statement.md) · [Following source section](the-return-statement.md)

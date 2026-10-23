# pdb - pdb alias command

You can nest aliases, and they may hold anything you're allowed to type at the pdb prompt. Bear in mind that an alias *can* shadow one of pdb's own built-in commands; the built-in then stays out of reach until you delete the alias. Expansion is applied recursively, but only to the first word of a command line — every remaining word is left untouched.

By way of illustration, here are a pair of handy aliases (particularly worth dropping into your `.pdbrc` file):

```python
# Print instance variables (usage "pi classInst")
alias pi for k in %1.__dict__.keys(): print(f"%1.{k} = {%1.__dict__[k]}")
# Print instance variables in self
alias ps pi self

```

[Subject index](INDEX.md) · [Continue](q.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: pdb alias command](debugger-commands.md) · [Preceding source contract and version conditions](debugger-commands.md)

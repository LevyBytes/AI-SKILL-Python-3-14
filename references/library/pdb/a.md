# pdb / Debugger commands: Debugger argument inspection, expression printing and displays

a(rgs)

Print the arguments of the current function and their current values.

 p expression

Evaluate *expression* in the current context and print its value.

Note

You may also use `print()`, though it is not a debugger command — doing so runs the Python [`print()`](https://docs.python.org/3.14/library/functions.html#print) function.

 pp expression

Behaves like the `p` command, save that *expression*'s value is pretty-printed by way of the [`pprint`](https://docs.python.org/3.14/library/pprint.html#module-pprint) module.

 whatis expression

Print the type of *expression*.

 source expression

Try to get source code of *expression* and display it.

Added in version 3.2.

 display [expression]

Show the value of *expression* whenever it has changed, each time execution stops in the current frame.

Without *expression*, list all display expressions for the current frame.

Note

Because display evaluates *expression* and compares it against the prior evaluation of *expression*, a mutable result may prevent display from noticing the change.

Example:

```python
lst = []
breakpoint()
pass
lst.append(1)
print(lst)

```

Because `lst.append(1)` mutates the evaluation result in place ahead of the comparison, display fails to notice that `lst` changed:

```python
> example.py(3)<module>()
-> pass
(Pdb) display lst
display lst: []
(Pdb) n
> example.py(4)<module>()
-> lst.append(1)
(Pdb) n
> example.py(5)<module>()
-> print(lst)
(Pdb)

```

You can do some tricks with copy mechanism to make it work:

```python
> example.py(3)<module>()
-> pass
(Pdb) display lst[:]
display lst[:]: []
(Pdb) n
> example.py(4)<module>()
-> lst.append(1)
(Pdb) n
> example.py(5)<module>()
-> print(lst)
display lst[:]: [1]  [old: []]
(Pdb)

```

Added in version 3.2.

 undisplay [expression]

Quit showing *expression* in the current frame. When *expression* is omitted, remove every display expression from the current frame.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](s-to-c.md) · [Continue](debugger-commands.md) · [Owning module, declaration or section: pdb](pdb-the-python-debugger.md) · [Owning module, declaration or section: Debugger commands](debugger-commands-section-introduction-and-initial-examples.md)

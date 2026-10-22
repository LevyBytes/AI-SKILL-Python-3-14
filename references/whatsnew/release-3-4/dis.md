# What's New In Python 3.4 / dis — dis

### dis

The functions [`show_code()`](https://docs.python.org/3.14/library/dis.html#dis.show_code), [`dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis), [`distb()`](https://docs.python.org/3.14/library/dis.html#dis.distb), and [`disassemble()`](https://docs.python.org/3.14/library/dis.html#dis.disassemble) will now take a keyword-only *file* argument that steers where their output lands.

The [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module is now constructed around an [`Instruction`](https://docs.python.org/3.14/library/dis.html#dis.Instruction) class offering object oriented access to the specifics of every single bytecode operation.

One new method, [`get_instructions()`](https://docs.python.org/3.14/library/dis.html#dis.get_instructions), yields an iterator that emits the Instruction stream for a supplied chunk of Python code. So you can now author a program that examines and reshapes a bytecode object along lines the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module itself never offered. For instance:

```python
>>> import dis
>>> for instr in dis.get_instructions(lambda x: x + 1):
...     print(instr.opname)
LOAD_FAST
LOAD_CONST
BINARY_ADD
RETURN_VALUE

```

The assorted display tools within the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module have been reworked to lean on these new pieces.

On top of that, a new application-friendly class, [`Bytecode`](https://docs.python.org/3.14/library/dis.html#dis.Bytecode), delivers an object-oriented API for examining bytecode both in human-readable form and by iterating across instructions. The `Bytecode` constructor accepts the very arguments that [`get_instructions()`](https://docs.python.org/3.14/library/dis.html#dis.get_instructions) accepts (plus an optional *current_offset*), and you can iterate the resulting object to yield [`Instruction`](https://docs.python.org/3.14/library/dis.html#dis.Instruction) objects. It additionally carries a [`dis`](https://docs.python.org/3.14/library/dis.html#dis.Bytecode.dis) method, the same as invoking [`dis`](https://docs.python.org/3.14/library/dis.html#dis.dis) on the constructor argument yet handed back as a multi-line string:

```python
>>> bytecode = dis.Bytecode(lambda x: x + 1, current_offset=3)
>>> for instr in bytecode:
...     print('{} ({})'.format(instr.opname, instr.opcode))
LOAD_FAST (124)
LOAD_CONST (100)
BINARY_ADD (23)
RETURN_VALUE (83)
>>> bytecode.dis().splitlines()
['  1           0 LOAD_FAST                0 (x)',
 '      -->     3 LOAD_CONST               1 (1)',
 '              6 BINARY_ADD',
 '              7 RETURN_VALUE']

```

[`Bytecode`](https://docs.python.org/3.14/library/dis.html#dis.Bytecode) further carries a class method, [`from_traceback()`](https://docs.python.org/3.14/library/dis.html#dis.Bytecode.from_traceback), letting you work over a traceback (that is, `print(Bytecode.from_traceback(tb).dis())` matches `distb(tb)`).

(Work by Nick Coghlan, Ryan Kelly and Thomas Kluyver landed under [bpo-11816](https://bugs.python.org/issue?@action=redirect&bpo=11816), with Claudiu Popa contributing via [bpo-17916](https://bugs.python.org/issue?@action=redirect&bpo=17916).)

A new function, [`stack_effect()`](https://docs.python.org/3.14/library/dis.html#dis.stack_effect), works out how a given opcode and argument shift the Python stack ? data you cannot otherwise reach. (Contributed by Larry Hastings in [bpo-19722](https://bugs.python.org/issue?@action=redirect&bpo=19722).)

[Subject index](INDEX.md) · [Previous source section](dbm.md) · [Next source section](doctest.md) · [Release/subject declaration](release-highlights.md)

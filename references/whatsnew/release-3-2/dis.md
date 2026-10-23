# What's New In Python 3.2 / dis - dis

### dis

Two code-inspection functions, [`code_info()`](https://docs.python.org/3.14/library/dis.html#dis.code_info) and [`show_code()`](https://docs.python.org/3.14/library/dis.html#dis.show_code), were added to the [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module. Each yields thorough code object details for a given function, method, source code string or code object. One returns the details as a string while the other prints them:

```python
>>> import dis, random
>>> dis.show_code(random.choice)
Name:              choice
Filename:          /Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/random.py
Argument count:    2
Kw-only arguments: 0
Number of locals:  3
Stack size:        11
Flags:             OPTIMIZED, NEWLOCALS, NOFREE
Constants:
   0: 'Choose a random element from a non-empty sequence.'
   1: 'Cannot choose from an empty sequence'
Names:
   0: _randbelow
   1: len
   2: ValueError
   3: IndexError
Variable names:
   0: self
   1: seq
   2: i

```

On top of that, the [`dis()`](https://docs.python.org/3.14/library/dis.html#dis.dis) function now takes string arguments, letting the familiar idiom `dis(compile(s, '', 'eval'))` collapse down to `dis(s)`:

```python
>>> dis('3*x+1 if x%2==1 else x//2')
  1           0 LOAD_NAME                0 (x)
              3 LOAD_CONST               0 (2)
              6 BINARY_MODULO
              7 LOAD_CONST               1 (1)
             10 COMPARE_OP               2 (==)
             13 POP_JUMP_IF_FALSE       28
             16 LOAD_CONST               2 (3)
             19 LOAD_NAME                0 (x)
             22 BINARY_MULTIPLY
             23 LOAD_CONST               1 (1)
             26 BINARY_ADD
             27 RETURN_VALUE
        >>   28 LOAD_NAME                0 (x)
             31 LOAD_CONST               0 (2)
             34 BINARY_FLOOR_DIVIDE
             35 RETURN_VALUE

```

Put side by side, these additions make poking around CPython’s implementation simpler and let you observe firsthand what the language syntax is doing under-the-hood.

(Contributed by Nick Coghlan in [bpo-9147](https://bugs.python.org/issue?@action=redirect&bpo=9147).)

[Subject index](INDEX.md) · [Previous source section](pydoc.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Next source section](dbm.md)

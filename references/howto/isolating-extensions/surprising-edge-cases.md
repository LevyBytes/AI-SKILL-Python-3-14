# Surprising Edge Cases

### Surprising Edge Cases

Be aware that isolated modules give rise to a few unexpected edge cases. The most striking is that one module object generally won't share its classes and exceptions with the other comparable modules. Picking up the earlier example, observe that `old_binascii.Error` and `binascii.Error` are distinct objects. Within the snippet below, the exception goes *un*caught:

```pycon
>>> old_binascii.Error == binascii.Error
False
>>> try:
...     old_binascii.unhexlify(b'qwertyuiop')
... except binascii.Error:
...     print('boo')
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
binascii.Error: Non-hexadecimal digit found

```

That outcome is the intended one. Observe that pure-Python modules act identically: this is simply part of how Python operates.

The aim is making extension modules safe down at the C level, not making hacks act in an intuitive way. Editing `sys.modules` ?by hand? qualifies as a hack.

[Subject index](INDEX.md) · [Previous source context](isolated-module-objects.md) · [Following source context](managing-global-state.md)

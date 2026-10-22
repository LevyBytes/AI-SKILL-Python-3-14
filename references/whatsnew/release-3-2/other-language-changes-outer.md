# Python 3.2 changes: Numeric string representations and surrounding language changes

- For a float or a complex number, [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) now yields exactly what its [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) yields. The `str()` rendering used to be terser, but that only bred confusion and serves no purpose now that the briefest workable `repr()` is shown by default:

```python
>>> import math
>>> repr(math.pi)
'3.141592653589793'
>>> str(math.pi)
'3.141592653589793'

```

(Proposed and implemented by Mark Dickinson; [bpo-9337](https://bugs.python.org/issue?@action=redirect&bpo=9337).)

- A [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object now carries a [`release()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.release) method and additionally honors the context management protocol. Doing so permits prompt freeing of whatever resources got claimed while a buffer was requested from the underlying object.

```python
>>> with memoryview(b'abcdefgh') as v:
...     print(v.tolist())
[97, 98, 99, 100, 101, 102, 103, 104]

```

(Added by Antoine Pitrou; [bpo-9757](https://bugs.python.org/issue?@action=redirect&bpo=9757).)

- It used to be forbidden to remove a name from the local namespace whenever that name appears as a free variable inside a nested block:

```python
def outer(x):
    def inner():
        return x
    inner()
    del x

```

[Subject index](INDEX.md) · [Previous source section](core-language-changes.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Release/subject declaration](core-language-changes.md) · [Following release/subject continuation](other-language-changes-f.md)

# sys.__stdin__, sys.__stdout__, sys.__stderr__

sys.__stdin__

sys.__stdout__

sys.__stderr__

These objects hold onto what `stdin`, `stderr` and `stdout` were set to when the program began. They come into play during finalization, and can be handy for printing to the genuine standard stream even after the matching `sys.std*` object has been redirected.

They also let you put the real files back to file objects known to work, should those get overwritten by a broken object. The preferred route, though, is to save the prior stream yourself before swapping it out, then restore that saved object.

Note

In certain situations `stdin`, `stdout` and `stderr`, along with the original `__stdin__`, `__stdout__` and `__stderr__` values, may all be `None`. That tends to happen for Windows GUI apps with no console attached and for Python apps launched via **pythonw**.

[API family](INDEX.md) · [sys context index](../INDEX.md).

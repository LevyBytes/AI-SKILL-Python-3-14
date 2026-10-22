# What’s New in Python 2.1 / PEP 208: New Coercion Model

### PEP 208: New Coercion Model

The way numeric coercion happens down at the C level was overhauled substantially. Only the authors of C extensions to Python will feel this, since it grants them greater freedom when crafting extension types that handle numeric operations.

Extension types may now flip the type flag `Py_TPFLAGS_CHECKTYPES` within their `PyTypeObject` structure to declare support for the new coercion model. In those extension types, the numeric slot functions can no longer take for granted that both arguments handed to them share a type; instead they might receive two arguments of unlike types and then carry out their own internal coercion. Should a slot function get a type it can’t deal with, it signals the failure by handing back a reference to the `Py_NotImplemented` singleton value. The other type’s numeric functions then get a turn, in case they can manage the operation; if that other type likewise returns `Py_NotImplemented`, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised. Numeric methods coded in Python can also hand back `Py_NotImplemented`, prompting the interpreter to behave as though the method were absent (perhaps raising a `TypeError`, perhaps reaching for another object’s numeric methods).

See also

[**PEP 208**](https://peps.python.org/pep-0208/) - Reworking the Coercion Model

Coded and authored by Neil Schemenauer, leaning heavily on prior work from Marc-André Lemburg. Consult it to grasp the subtle details of the way numeric operations now get handled at the C level.

[Subject index](INDEX.md) · [Previous source section](pep-217-interactive-display-hook.md) · [Next source section](pep-241-metadata-in-python-packages.md) · [Release/subject declaration](introduction.md)

# -R

-R

Switch on hash randomization. This option only does something when the `PYTHONHASHSEED` environment variable holds a value other than `random`, given that hash randomization is on by default.

In earlier Python releases, this option enables hash randomization, causing the [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) values of str and bytes objects to be "salted" using an unpredictable random value. While those values stay fixed throughout a single Python process, you cannot predict them across separate runs of Python.

The purpose of hash randomization is to guard against a denial-of-service in which deliberately chosen inputs trigger the worst case behavior of building a dict, with *O*(*n*2) complexity. Refer to [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html) for the specifics.

`PYTHONHASHSEED` allows you to set a fixed value for the hash seed secret.

Added in version 3.2.3.

Changed in version 3.7: The option is no longer ignored.

[Subject index](INDEX.md) · [Previous source section](quiet-startup.md) · [Following source section](disable-user-site.md)

# weakref: Weak-reference callbacks and lifetime

__callback__

This read-only attribute hands back whichever callback is presently tied to the weakref. Where no callback exists, or where the weakref's referent has stopped being alive, this attribute reads `None`.

Changed in version 3.4: Introduced the `__callback__` attribute.

[Subject index](INDEX.md) · [Previous](weakref-ref-class.md) · [Continue](weakref-proxy-to-weakref-getweakrefs.md) · [Owning module, declaration or section: weakref](weakref-ref-class.md) · [Owning module, declaration or section: weakref.ref](weakref-ref-class.md)

# inspect — Types and members — Contract: Changed in version 3.5: Add `__qualname__` and `gi_yieldfrom` attributes to generators.

Changed in version 3.5: Add `__qualname__` and `gi_yieldfrom` attributes to generators.

A generator's `__name__` attribute now derives from the function name rather than the code name, and it is now writable.

Changed in version 3.7: Add `cr_origin` attribute to coroutines.

Changed in version 3.10: Add `__builtins__` attribute to functions.

Changed in version 3.11: Add `gi_suspended` attribute to generators.

Changed in version 3.11: Add `cr_suspended` attribute to coroutines.

Changed in version 3.12: Add `ag_suspended` attribute to async generators.

Changed in version 3.14: Add `f_generator` attribute to frames.

[Subject index](INDEX.md) · [Previous](types-and-members-complete-type-attribute-description-table.md) · [Continue](inspect-getmembers-to-inspect-ismethod.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Types and members](types-and-members-section-introduction-and-initial-examples.md)

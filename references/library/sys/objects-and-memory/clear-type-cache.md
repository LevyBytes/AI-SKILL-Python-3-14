# sys._clear_type_cache

sys._clear_type_cache()

Empty the internal type cache. That cache exists to make attribute and method lookups faster. Reach for this function *only* to shed unneeded references while debugging reference leaks.

Treat this function as reserved for internal and specialized use only.

Deprecated since version 3.13: Use the more general `_clear_internal_caches()` function instead.

[API family](INDEX.md) · [sys context index](../INDEX.md).

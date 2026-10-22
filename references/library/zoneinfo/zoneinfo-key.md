# zoneinfo: ZoneInfo alternate constructors, cache invalidation and keys

`*classmethod *ZoneInfo.from_file(*file_obj*, */*, *key=None*)`

Builds a `ZoneInfo` object out of a file-like object that yields bytes (such as a file opened in binary mode or an [`io.BytesIO`](https://docs.python.org/3.14/library/io.html#io.BytesIO) object). In contrast to the primary constructor, this one always produces a fresh object.

The `key` parameter establishes the zone's name where [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) are concerned.

Objects produced through this constructor are unpicklable (refer to pickling).

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised whenever the bytes read out of *file_obj* don't form a valid TZif file.

`*classmethod *ZoneInfo.no_cache(*key*)`

A second constructor that sidesteps the constructor's cache. It behaves just like the primary constructor except that each call hands back a brand-new object. Its likeliest uses are testing or demonstration, although it can also serve to build a system running a different cache invalidation strategy.

Objects produced through this constructor also skip a deserializing process's cache when unpickled.

Caution

This constructor can shift the semantics of your datetimes in unexpected directions; reach for it only when you are certain you need it.

These class methods are on hand as well:

`*classmethod *ZoneInfo.clear_cache(***, *only_keys=None*)`

A method that invalidates the cache on the `ZoneInfo` class. With no arguments supplied, every cache is wiped and the subsequent call to the primary constructor for each key produces a new instance.

Hand an iterable of key names to the `only_keys` parameter and only those listed keys leave the cache. Any keys given to `only_keys` yet absent from the cache are simply passed over.

Warning

Calling this function can shift the semantics of datetimes that rely on `ZoneInfo` in unexpected directions; because it alters module state, the consequences may reach broadly. Use it only when you are sure you need to.

A single attribute belongs to the class:

 ZoneInfo.key

A read-only [attribute](https://docs.python.org/3.14/glossary.html#term-attribute) that gives back the `key` value handed to the constructor, which ought to be a lookup key from the IANA time zone database (`America/New_York`, `Europe/Paris`, or `Asia/Tokyo`, for example).

Where a zone was built from a file without a `key` parameter supplied, this gets set to `None`.

Note

Even though exposing these to end users is a fairly widespread habit, the values are intended as primary keys identifying the zones in question, not necessarily as user-facing elements. Tools such as CLDR (the Unicode Common Locale Data Repository) can turn these keys into friendlier strings.

[Subject index](INDEX.md) · [Previous](zoneinfo-zoneinfo-class.md) · [Continue](string-representations.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md) · [Owning module, declaration or section: zoneinfo.ZoneInfo](zoneinfo-zoneinfo-class.md) · [Owning module, declaration or section: The `ZoneInfo` class](zoneinfo-zoneinfo-class.md)

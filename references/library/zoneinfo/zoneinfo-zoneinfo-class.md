# zoneinfo: ZoneInfo constructor and timezone caching

### The `ZoneInfo` class

`*class *zoneinfo.ZoneInfo(*key*)`

A concrete subclass of [`datetime.tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo) standing for an IANA time zone named by the string `key`. Every call to the primary constructor yields objects that compare as identical; framed differently, so long as no cache invalidation happens via `ZoneInfo.clear_cache()`, this assertion holds for any value of `key`:

```python
a = ZoneInfo(key)
b = ZoneInfo(key)
assert a is b

```

`key` has to take the shape of a relative, normalized POSIX path carrying no up-level references. Hand the constructor a key that doesn't conform and it raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

Should no file match `key`, the constructor raises `ZoneInfoNotFoundError`.

Two alternate constructors come with the `ZoneInfo` class:

[Subject index](INDEX.md) · [Previous](runtime-configuration.md) · [Continue](zoneinfo-key.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)

# zoneinfo — String representations

### String representations

Calling [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) on a `ZoneInfo` object yields a string representation that, by default, leans on the `ZoneInfo.key` attribute (see the usage note in the attribute documentation):

```python
>>> zone = ZoneInfo("Pacific/Kwajalein")
>>> str(zone)
'Pacific/Kwajalein'

>>> when = dt.datetime(2020, 4, 1, 3, 15, tzinfo=zone)
>>> f"{when.isoformat()} [{when.tzinfo}]"
'2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'

```

When an object was built from a file with no `key` parameter given, `str` instead defers to [`repr()`](https://docs.python.org/3.14/library/functions.html#repr). The `repr` of a `ZoneInfo` is implementation-defined and may differ from one version to the next, yet it is guaranteed never to be a valid `ZoneInfo` key.

[Subject index](INDEX.md) · [Previous](zoneinfo-key.md) · [Continue](pickle-serialization.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)

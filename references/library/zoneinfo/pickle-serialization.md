# zoneinfo — Pickle serialization

### Pickle serialization

In place of serializing the entire body of transition data, `ZoneInfo` objects are serialized by key, and any `ZoneInfo` object built from a file (even one where a `key` value was given) cannot be pickled.

How a `ZoneInfo` file behaves hinges on the way it was built:

1.

`ZoneInfo(key)`: Built through the primary constructor, a `ZoneInfo` object serializes by key, and on deserialization the deserializing process turns to the primary constructor, so these are expected to be the same object as other references to that same time zone. Suppose `europe_berlin_pkl` is a string holding a pickle made from `ZoneInfo("Europe/Berlin")`; you would then expect this behavior:

```pycon
>>> a = ZoneInfo("Europe/Berlin")
>>> b = pickle.loads(europe_berlin_pkl)
>>> a is b
True

```

2.

`ZoneInfo.no_cache(key)`: Built from the cache-bypassing constructor, the `ZoneInfo` object likewise serializes by key, but on deserialization the deserializing process reaches for the cache-bypassing constructor. Suppose `europe_berlin_pkl_nc` is a string holding a pickle made from `ZoneInfo.no_cache("Europe/Berlin")`; you would then expect this behavior:

```pycon
>>> a = ZoneInfo("Europe/Berlin")
>>> b = pickle.loads(europe_berlin_pkl_nc)
>>> a is b
False

```

3.

`ZoneInfo.from_file(file_obj, /, key=None)`: Built from a file, the `ZoneInfo` object raises an exception when you try to pickle it. An end user who wants to pickle a `ZoneInfo` built from a file is advised to wrap it in a custom type or supply a custom serialization function — either serializing by key or saving the file object's contents and serializing those.

For this serialization scheme to work, the time zone data for the key in question must be present on both the serializing and the deserializing side, much as references to classes and functions are assumed to exist in both the serializing and the deserializing environments. It further means there is no guarantee of consistent results when you unpickle a `ZoneInfo` that was pickled in an environment carrying a different version of the time zone data.

[Subject index](INDEX.md) · [Previous](string-representations.md) · [Continue](zoneinfo-available-timezones-to-zoneinfo-reset-tzpath.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)

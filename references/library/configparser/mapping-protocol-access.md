# configparser - Mapping Protocol Access

### Mapping Protocol Access

Added in version 3.2.

Mapping protocol access is the umbrella term for the capability that lets your own objects be treated as though they were dictionaries. Where `configparser` is concerned, that mapping interface is realized through the `parser['section']['option']` notation.

Specifically, `parser['section']` yields a proxy onto the section's data held in the parser. So the values aren't duplicated — they're drawn from the underlying parser as needed. More significant still, modifying values via a section proxy genuinely alters them inside the original parser.

The aim is for `configparser` objects to act as much like real dictionaries as they can. That mapping interface is fully realized and conforms to the [`MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping) ABC. A handful of distinctions, though, warrant your attention:

- Out of the box, every key within a section can be reached without regard to case [1]. For example, `for option in parser["section"]` produces only the `optionxform`'ed option key names — lowercased keys by default. Likewise, in a section carrying the key `'a'`, both of these expressions yield `True`:

```python
"a" in parser["section"]
"A" in parser["section"]

```

- Every section carries the `DEFAULTSECT` values too, so calling `.clear()` on a section might not render it visibly empty. The reason is that default values can't be removed from the section (since, strictly speaking, they aren't held there). When a section overrides them, deleting the override brings the default back into view. Attempting to delete a default value produces a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

- The `DEFAULTSECT` cannot be dropped from the parser:

  - attempting to delete it raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError),

  - `parser.clear()` leaves it intact,

  - `parser.popitem()` never returns it.

- With `parser.get(section, option, **kwargs)`, the second argument is **not** a fallback value. That said, the section-level `get()` methods do work with both the mapping protocol and the classic configparser API.

- `parser.items()` aligns with the mapping protocol (handing back a list of *section_name*, *section_proxy* pairs, the DEFAULTSECT included). Yet you can also call this method with arguments: `parser.items(section, raw, vars)`. That second form yields a list of *option*, *value* pairs for the given `section`, every interpolation resolved (unless you pass `raw=True`).

The mapping protocol sits atop the existing legacy API, ensuring that subclasses which override the original interface still keep mappings behaving the way you'd expect.

[Subject index](INDEX.md) · [Previous](configparser-extendedinterpolation-class.md) · [Continue](parser-customization-overview.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)

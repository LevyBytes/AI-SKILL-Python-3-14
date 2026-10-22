# Module-level functions

### Module-level functions

Building a pattern object and calling its methods is not mandatory; the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module additionally offers top-level functions named [`match()`](https://docs.python.org/3.14/library/re.html#re.match), [`search()`](https://docs.python.org/3.14/library/re.html#re.search), [`findall()`](https://docs.python.org/3.14/library/re.html#re.findall), [`sub()`](https://docs.python.org/3.14/library/re.html#re.sub), and the like. Each takes the same arguments as its matching pattern method, with the RE string slipped in as the first argument, and still hands back either `None` or a [match object](https://docs.python.org/3.14/library/re.html#match-objects) instance.

```python
>>> print(re.match(r'From\s+', 'Fromage amk'))
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.Match object; span=(0, 5), match='From '>

```

Behind the scenes, these functions just build a pattern object on your behalf and invoke the right method on it. They additionally tuck the compiled object into a cache, so later calls reusing the same RE skip parsing the pattern over and over.

Should you reach for these module-level functions, or fetch the pattern and call its methods directly? When you use a regex inside a loop, compiling it ahead of time spares a handful of function calls. Away from loops, the built-in cache makes the gap negligible.

[Subject index](INDEX.md) · [Previous source context](findall-finditer-and-raw-string-caveats.md) · [Following source context](compilation-flags.md)

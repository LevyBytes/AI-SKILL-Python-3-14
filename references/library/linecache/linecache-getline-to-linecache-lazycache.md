# linecache — `linecache` — Random access to text lines

## linecache — Random access to text lines

### `linecache` — Random access to text lines

**Source code:** [Lib/linecache.py](https://github.com/python/cpython/tree/3.14/Lib/linecache.py)

---

The `linecache` module lets you fetch any single line out of a Python source file, and internally it tries to optimize — by way of a cache — the usual situation in which many lines come from one file. The [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module draws on it to pull source lines for inclusion in the formatted traceback.

Files are opened through the [`tokenize.open()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.open) function. That function leans on [`tokenize.detect_encoding()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.detect_encoding) to work out the file's encoding; should no encoding token be present, the encoding falls back to UTF-8.

These are the functions the `linecache` module defines:

 linecache.getline(*filename*, *lineno*, *module_globals=None*)

Retrieve line *lineno* out of the file called *filename*. No exception is ever raised by this function — on errors it hands back `''` (and for lines that are located, the closing newline character comes along with them).

When *filename* points at a frozen module (one beginning with `'<frozen '`), the function tries to recover the genuine file name from `module_globals['__file__']`, provided *module_globals* isn't `None`.

Should no file named *filename* turn up, the function looks first for a [**PEP 302**](https://peps.python.org/pep-0302/) `__loader__` within *module_globals*. When such a loader exists and supplies a `get_source` method, that method settles the source lines (and if `get_source()` yields `None`, `''` comes back). Lastly, when *filename* is relative, it gets resolved against the entries on the module search path, `sys.path`.

Changed in version 3.14: Added handling for a *filename* belonging to frozen modules.

 linecache.clearcache()

Empty the cache. Reach for this function once you've finished with lines from files read earlier via `getline()`.

 linecache.checkcache(*filename=None*)

Validate the cache. Turn to this function when files held in the cache might have been altered on disk and you need the refreshed copy. Leave *filename* out and it inspects every entry sitting in the cache.

 linecache.lazycache(*filename*, *module_globals*)

Record just enough about a module that isn't file-based so that its lines can be obtained afterward through `getline()`, even when *module_globals* is `None` at that later point. This defers any I/O until a line is genuinely required, sparing you from holding onto the module globals forever.

Added in version 3.5.

Example:

```python
>>> import linecache
>>> linecache.getline(linecache.__file__, 8)
'import sys\n'

```

[Subject index](INDEX.md)

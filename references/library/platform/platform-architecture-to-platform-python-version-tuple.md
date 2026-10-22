# platform: Platform architecture, operating-system and Python version queries

### Cross platform

 platform.architecture(*executable=sys.executable*, *bits=''*, *linkage=''*)

Interrogates the supplied executable (the Python interpreter binary by default) to gather assorted architecture details.

Hands back a tuple `(bits, linkage)` carrying details about the bit architecture together with the linkage format the executable uses. Each of the two values comes back as a string.

Whatever cannot be worked out is returned just as the parameter presets specify. Should bits be passed as `''`, then `sizeof(pointer)` (or `sizeof(long)` on a Python version < 1.5.2) serves as the gauge of the supported pointer size.

To do the real work, the function leans on the system's `file` command. That command exists across most — perhaps all — Unix platforms and a handful of non-Unix ones, but only when the executable refers to the Python interpreter. Sensible defaults kick in whenever those conditions go unmet.

Note

Under macOS — and conceivably elsewhere — an executable file can be a universal file bundling several architectures together.

For determining the “64-bitness” of the interpreter you are running, a surer route is to read the [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize) attribute:

```python
is_64bits = sys.maxsize > 2**32

```

 platform.machine()

Gives back the machine type, for instance `'AMD64'`. Where the value cannot be worked out, an empty string comes back instead.

What it produces hinges on the platform and can vary in its casing as well as its naming conventions.

 platform.node()

Gives back the computer's network name (which might not be fully qualified!). Where the value cannot be worked out, an empty string comes back instead.

 platform.platform(*aliased=False*, *terse=False*)

Hands back one string that names the underlying platform while packing in as much helpful detail as it can.

The result is meant to be *human readable* instead of something a machine parses. Its appearance can shift from one platform to another, and that is by design.

When *aliased* holds true, the function substitutes aliases for those platforms whose reported system names diverge from their everyday names — so, for example, SunOS shows up as Solaris. This is carried out by the `system_alias()` function.

Turning *terse* on makes the function hand back nothing beyond the bare minimum required to pin down the platform.

Changed in version 3.8: On macOS, the function now consults `mac_ver()` — provided it yields a non-empty release string — to fetch the macOS version in place of the darwin version.

 platform.processor()

Returns the (real) processor name, e.g. `'amdk6'`.

Where the value cannot be worked out, an empty string comes back. Bear in mind that a good many platforms either withhold this detail or just echo the same value `machine()` gives — NetBSD being one such case.

 platform.python_build()

Hands back a tuple `(buildno, builddate)` that reports, as strings, the Python build number alongside its date.

 platform.python_compiler()

Hands back a string that names the compiler with which Python was compiled.

 platform.python_branch()

Hands back a string that names the SCM branch of the Python implementation.

 platform.python_implementation()

Hands back a string that names the Python implementation. The values it can return are ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.

 platform.python_revision()

Hands back a string that names the SCM revision of the Python implementation.

 platform.python_version()

Hands back the Python version as the string `'major.minor.patchlevel'`.

Keep in mind that, in contrast to Python's `sys.version`, whatever this returns will always carry the patchlevel (defaulting to 0).

 platform.python_version_tuple()

Hands back the Python version as the tuple `(major, minor, patchlevel)` whose members are strings.

Keep in mind that, in contrast to Python's `sys.version`, whatever this returns will always carry the patchlevel (defaulting to `'0'`).

[Subject index](INDEX.md) · [Previous](platform-access-to-underlying-platform-s-identifying-data.md) · [Continue](platform-release-to-platform-invalidate-caches.md) · [Owning module, declaration or section: platform](platform-access-to-underlying-platform-s-identifying-data.md)

# subprocess — `subprocess` — Subprocess management

### `subprocess` — Subprocess management

**Source code:** [Lib/subprocess.py](https://github.com/python/cpython/tree/3.14/Lib/subprocess.py)

---

With the `subprocess` module you can launch fresh processes, attach to their input/output/error pipes, and read back the codes they return when they finish. The module is meant to supersede a number of legacy modules and helpers:

```python
os.system
os.spawn*

```

The sections that follow explain how `subprocess` substitutes for each of these older modules and helpers.

See also

[**PEP 324**](https://peps.python.org/pep-0324/) – PEP proposing the subprocess module

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not Android, not iOS, not WASI.

There is no support for this module on [mobile platforms](https://docs.python.org/3.14/library/intro.html#mobile-availability) or on [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability).

[Subject index](INDEX.md) · [Continue](subprocess-run.md)

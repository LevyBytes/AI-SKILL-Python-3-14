# wave`wave` - Read and write WAV files

# Wave

### `wave` - Read and write WAV files

**Source code:** [Lib/wave.py](https://github.com/python/cpython/tree/3.14/Lib/wave.py)

---

A handy way to work with the Waveform Audio “WAVE” (or “WAV”) file format is offered by the `wave` module. It handles only wave files encoded as uncompressed PCM.

Changed in version 3.12: Reading `WAVE_FORMAT_EXTENSIBLE` headers became possible, as long as the extended format happens to be `KSDATAFORMAT_SUBTYPE_PCM`.

One function and one exception are exposed by the `wave` module:

 wave.open(*file*, *mode=None*)

When *file* is given as a string, the file with that name is opened; otherwise it's used directly as a file-like object. Acceptable values for *mode* are:

`'rb'`

Reading only.

`'wb'`

Writing only.

Be aware that combined read/write WAV files aren't permitted.

Passing a *mode* of `'rb'` hands back a `Wave_read` object, whereas `'wb'` hands back a `Wave_write` object. Should *mode* be left out while *file* is supplied as a file-like object, the value of `file.mode` serves as the fallback for *mode*.

When a file-like object is what you supply, the wave object leaves it open after its `close()` method runs; closing that file object is then up to the caller.

You can employ `open()` inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. Once the `with` block finishes, whichever applies of `Wave_read.close()` or `Wave_write.close()` gets invoked.

Changed in version 3.4: Unseekable files gained support.

 *exception *wave.Error

The error thrown whenever an operation can't proceed because it breaks the WAV specification or runs into a shortcoming of the implementation.

[Subject index](INDEX.md) · [Continue](wave-wave-read-class.md)

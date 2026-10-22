# wave.Wave_read: `close()`, `getnchannels()`, `getsampwidth()`, `getframerate()`, `getnframes()`, `getcomptype()`, `getcompname()`, `getparams()`, `readframes()`, `rewind()`, `getmarkers()`, `getmark()`, `setpos()`, `tell()`

close()

Shut the stream when `wave` was the one that opened it, leaving the instance no longer usable. It runs on its own when the object is collected.

 getnchannels()

Gives back how many audio channels there are (`1` for mono, `2` for stereo).

 getsampwidth()

Gives back the sample width measured in bytes.

 getframerate()

Gives back the sampling frequency.

 getnframes()

Gives back how many audio frames there are.

 getcomptype()

Gives back the compression type (`'NONE'` being the lone supported one).

 getcompname()

A reader-friendly form of `getcomptype()`. Typically `'not compressed'` lines up with `'NONE'`.

 getparams()

Gives back a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, matching what the `get*()` methods return.

 readframes(*n*)

Reads then returns no more than *n* audio frames, packaged as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object.

 rewind()

Move the file pointer back to where the audio stream starts.

The next pair of methods exists purely for compatibility with the legacy `aifc` module and serve no real purpose.

 getmarkers()

Returns `None`.

Deprecated since version 3.13, will be removed in version 3.15: It survived solely to stay compatible with the `aifc` module, which was dropped from Python 3.13.

 getmark(*id*)

Raise an error.

Deprecated since version 3.13, will be removed in version 3.15: It survived solely to stay compatible with the `aifc` module, which was dropped from Python 3.13.

The pair of methods that follow share a notion of “position” that is consistent across the two but otherwise hinges on the implementation.

 setpos(*pos*)

Move the file pointer to the position you give.

 tell()

Hand back where the file pointer currently sits.

[Subject index](INDEX.md) · [Previous](wave-wave-read-class.md) · [Continue](wave-wave-write-class.md) · [Owning module, declaration or section: wave](wave-open-to-wave-error.md) · [Owning module, declaration or section: wave.Wave_read](wave-wave-read-class.md) · [Owning module, declaration or section: Wave_read Objects](wave-wave-read-class.md)

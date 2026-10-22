# codecs: Codec lookup, registry and encoded stream wrappers

codecs.getencoder(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its encoder function.

Should the encoding prove unresolvable, a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised.

 codecs.getdecoder(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its decoder function.

Should the encoding prove unresolvable, a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised.

 codecs.getincrementalencoder(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its incremental encoder class or factory function.

A [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised should the encoding be unresolvable or should that codec lack an incremental encoder.

 codecs.getincrementaldecoder(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its incremental decoder class or factory function.

A [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised should the encoding be unresolvable or should that codec lack an incremental decoder.

 codecs.getreader(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its `StreamReader` class or factory function.

Should the encoding prove unresolvable, a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised.

 codecs.getwriter(*encoding*)

Resolve the codec tied to the supplied encoding and hand back its `StreamWriter` class or factory function.

Should the encoding prove unresolvable, a [`LookupError`](https://docs.python.org/3.14/library/exceptions.html#LookupError) is raised.

To make custom codecs available, register an appropriate codec search function:

 codecs.register(*search_function*, */*)

Register a codec search function. A search function should accept a single argument — the encoding name given entirely in lowercase letters with hyphens and spaces swapped for underscores — and hand back a `CodecInfo` object. Whenever a search function fails to resolve the requested encoding, it ought to return `None`.

Changed in version 3.9: Hyphens and spaces are converted to underscore.

 codecs.unregister(*search_function*, */*)

Remove a codec search function from the registry and flush the registry’s cache. When the given search function was never registered, the call is a no-op.

Added in version 3.10.

The built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) plus the companion [`io`](https://docs.python.org/3.14/library/io.html#module-io) module remain the suggested way to handle encoded text files; even so, this module adds further helper functions and classes that let you reach a broader assortment of codecs when dealing with binary files:

 codecs.open(*filename*, *mode='r'*, *encoding=None*, *errors='strict'*, *buffering=-1*)

Open an encoded file under the supplied *mode* and yield a `StreamReaderWriter` instance that handles encoding/decoding transparently. When *mode* is left out it falls back to `'r'`, which opens the file for reading.

Note

Whenever *encoding* is something other than `None`, the underlying encoded files are always opened in binary mode. Neither reads nor writes perform any automatic `'\n'` conversion. The *mode* argument may be any binary mode that the built-in `open()` function accepts; the `'b'` is appended for you.

*encoding* names the encoding to apply to the file. Any encoding that encodes to and decodes from bytes is permitted, and which data types the file methods accept hinges on the codec in play.

You may pass *errors* to set the error handling. It defaults to `'strict'`, which makes a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) be raised when an encoding error happens.

*buffering* carries the same meaning that it does for the built-in `open()` function. Its default of -1 selects the default buffer size.

Changed in version 3.11: The `'U'` mode has been removed.

Deprecated since version 3.14: `codecs.open()` has been superseded by `open()`.

 codecs.EncodedFile(*file*, *data_encoding*, *file_encoding=None*, *errors='strict'*)

Return a `StreamRecoder` instance — a wrapped form of *file* that handles transparent transcoding. Closing the wrapper closes the original file too.

Whatever is written to the wrapper is first decoded according to the supplied *data_encoding* and then written to the underlying file as bytes via *file_encoding*. In the other direction, bytes read out of the underlying file are decoded according to *file_encoding*, and that result is re-encoded with *data_encoding*.

When *file_encoding* is omitted, it falls back to *data_encoding*.

You may pass *errors* to set the error handling. It defaults to `'strict'`, which makes [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) be raised when an encoding error happens.

[Subject index](INDEX.md) · [Previous](codecs-codecinfo-class.md) · [Continue](codecs-iterencode-to-codecs-bom-utf32-le.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md)

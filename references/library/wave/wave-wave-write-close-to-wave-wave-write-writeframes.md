# wave.Wave_write: WAVE output parameters, frame writing and closure

close()

Confirm *nframes* is right and close the file when `wave` opened it. The method fires when the object is collected. Should the output stream be unseekable and *nframes* fail to match how many frames were truly written, an exception is raised.

 setnchannels(*n*)

Specify how many channels there are.

 getnchannels()

Give back how many channels there are.

 setsampwidth(*n*)

Set the sample width to *n* bytes.

 getsampwidth()

Give back the sample width in bytes.

 setframerate(*n*)

Set the frame rate to *n*.

Changed in version 3.2: When this method receives a non-integral input, that value is rounded to the closest whole number.

 getframerate()

Give back the frame rate.

 setnframes(*n*)

Set the number of frames to *n*. Should the count of frames actually written turn out different, this gets adjusted afterward (and that adjustment throws an error when the output stream cannot be seeked).

 getnframes()

Give back the tally of audio frames written up to now.

 setcomptype(*type*, *name*)

Establish the compression type along with its description. For now `NONE` is the sole compression type accepted, which signifies no compression.

 getcomptype()

Give back the compression type (`'NONE'`).

 getcompname()

Give back the reader-friendly name of the compression type.

 setparams(*tuple*)

The *tuple* ought to be `(nchannels, sampwidth, framerate, nframes, comptype, compname)`, holding values acceptable to the `set*()` methods. It sets every parameter.

 getparams()

Give back a [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) `(nchannels, sampwidth, framerate, nframes, comptype, compname)` carrying the present output parameters.

 tell()

Give back the current spot in the file, subject to the same caveat noted for the `Wave_read.tell()` and `Wave_read.setpos()` methods.

 writeframesraw(*data*)

Write audio frames while leaving *nframes* uncorrected.

Changed in version 3.4: Every [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now taken.

 writeframes(*data*)

Write audio frames and confirm *nframes* is right. An error is raised if the output stream can't be seeked and the running total of frames written after *data* goes out doesn't equal the previously set *nframes* value.

Changed in version 3.4: Every [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object) is now taken.

Bear in mind that adjusting any parameters once you've called `writeframes()` or `writeframesraw()` is not allowed, and trying anyway raises `wave.Error`.

[Subject index](INDEX.md) · [Previous](wave-wave-write-class.md) · [Owning module, declaration or section: wave](wave-open-to-wave-error.md) · [Owning module, declaration or section: wave.Wave_write](wave-wave-write-class.md) · [Owning module, declaration or section: Wave_write Objects](wave-wave-write-class.md)

# wave: `wave.Wave_write`

### Wave_write Objects

 *class *wave.Wave_write

Write a WAV file.

Wave_write objects, the kind `open()` returns.

When the output stream is seekable, the `wave` header gets revised on its own to match how many frames were really written. With an unseekable stream, however, the *nframes* value has to be right by the time the first frame data goes out. You can secure a correct *nframes* either by invoking `setnframes()` or `setparams()` with the eventual frame count ahead of the `close()` call and then writing the frame data via `writeframesraw()`, or by handing every bit of frame data to `writeframes()` at once. Taking the second route, `writeframes()` works out the frame count from the data and sets *nframes* to suit before the frame data is written.

Changed in version 3.4: Unseekable files gained support.

The methods available on Wave_write objects are:

[Subject index](INDEX.md) · [Previous](wave-wave-read-close-to-wave-wave-read-tell.md) · [Continue](wave-wave-write-close-to-wave-wave-write-writeframes.md) · [Owning module, declaration or section: wave](wave-open-to-wave-error.md)

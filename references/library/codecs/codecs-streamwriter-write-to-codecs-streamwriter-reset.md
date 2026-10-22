# codecs.StreamWriter: `write()`, `writelines()`, `reset()`

write(*object*)

Writes the encoded form of the object's contents out to the stream.

 writelines(*list*)

Writes the joined-together iterable of strings to the stream (potentially by leaning on the `write()` method). Endless or extremely large iterables aren't handled. This method is unsupported by the standard bytes-to-bytes codecs.

 reset()

Clears the codec buffers that retain internal state.

Invoking this method ought to guarantee that the output's data sits in a tidy state, ready for fresh new data to be appended without rescanning the entire stream to rebuild state.

Beyond the methods listed above, the `StreamWriter` is also required to inherit every other method and attribute from the stream beneath it.

[Subject index](INDEX.md) · [Previous](codecs-streamwriter-class.md) · [Continue](codecs-streamreader-class.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: codecs.StreamWriter](codecs-streamwriter-class.md) · [Owning module, declaration or section: StreamWriter Objects](codecs-streamwriter-class.md)

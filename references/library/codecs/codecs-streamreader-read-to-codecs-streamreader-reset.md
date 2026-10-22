# codecs.StreamReader: `read()`, `readline()`, `readlines()`, `reset()`

read(*size=-1*, *chars=-1*, *firstline=False*)

Decodes data drawn from the stream and gives back the object that results.

The *chars* argument states how many decoded code points or bytes should come back. The `read()` method never hands back more data than was asked for, though it may deliver less when not enough is on hand.

The *size* argument states the rough upper bound on encoded bytes or code points to pull in for decoding. The decoder is free to tweak this value however it sees fit. A default of -1 signals that it should read and decode everything possible. The point of this parameter is to keep enormous files from being decoded in a single pass.

The *firstline* flag signals that returning just the first line would suffice when decoding errors crop up on subsequent lines.

The method ought to follow a greedy read approach, meaning it should pull in as much data as the encoding's rules and the supplied size permit; for example, if optional encoding endings or state markers happen to be on the stream, those should be consumed as well.

 readline(*size=None*, *keepends=True*)

Read a single line off the input stream and hand back its decoded data.

When *size* is supplied, it's forwarded as the size argument to the stream's `read()` method.

When *keepends* is false, line-endings get trimmed off the returned lines.

 readlines(*sizehint=None*, *keepends=True*)

Read every line on hand from the input stream and hand them back as a list of lines.

The codec's `decode()` method drives how line-endings are handled, and they appear in the list entries whenever *keepends* is true.

When *sizehint* is supplied, it's forwarded as the *size* argument to the stream's `read()` method.

 reset()

Clears the codec buffers that retain internal state.

Be aware that the stream should not be repositioned. The chief purpose of this method is to allow recovery after decoding errors.

Beyond the methods listed above, the `StreamReader` is also required to inherit every other method and attribute from the stream beneath it.

[Subject index](INDEX.md) · [Previous](codecs-streamreader-class.md) · [Continue](codecs-streamreaderwriter-class.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: codecs.StreamReader](codecs-streamreader-class.md) · [Owning module, declaration or section: StreamReader Objects](codecs-streamreader-class.md)

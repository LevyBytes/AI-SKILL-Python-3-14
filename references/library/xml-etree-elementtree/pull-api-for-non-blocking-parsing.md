# xml.etree.ElementTree - Pull API for non-blocking parsing

### Pull API for non-blocking parsing

The majority of this module's parsing routines insist on the entire document being consumed before any result comes back. Although you can supply data to an `XMLParser` piece by piece, that mechanism is a push API invoking methods on a callback target - an approach that is too low-level and awkward for the typical case. At times what someone genuinely needs is incremental XML parsing free of blocking operations, all while keeping the comfort of fully built `Element` objects.

For this task the strongest option is `XMLPullParser`. Rather than performing a blocking read to acquire the XML data, it accepts data step by step through `XMLPullParser.feed()` calls. You retrieve the parsed XML elements by invoking `XMLPullParser.read_events()`. The following illustrates this:

```python
>>> parser = ET.XMLPullParser(['start', 'end'])
>>> parser.feed('<mytag>sometext')
>>> list(parser.read_events())
[('start', <Element 'mytag' at 0x7fa66db2be58>)]
>>> parser.feed(' more text</mytag>')
>>> for event, elem in parser.read_events():
...     print(event)
...     print(elem.tag, 'text=', elem.text)
...
end
mytag text= sometext more text

```

A natural scenario is software running without blocking, where the XML arrives over a socket or is pulled bit by bit off some storage medium. Under those conditions, reads that block cannot be tolerated.

Owing to all that flexibility, `XMLPullParser` can feel cumbersome for plainer situations. Should blocking on the read of XML data not trouble your program yet you still want incremental parsing, consider `iterparse()` instead. It comes in handy when a sizable XML document is being read and you'd rather not keep the whole thing resident in memory.

When you want *immediate* feedback delivered through events, invoking the `XMLPullParser.flush()` method can cut down the delay; be sure to review the associated security notes.

[Subject index](INDEX.md) · [Previous](parsing-xml.md) · [Continue](finding-interesting-elements.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)

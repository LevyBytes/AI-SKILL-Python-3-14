# XMLPullParser events and parse errors

A pull-style parser designed for use in code that must not block. On the feeding side its API resembles `XMLParser`, yet rather than invoking a callback target, `XMLPullParser` accumulates a private queue of parse events that the caller pulls from on demand. The *events* argument names which kinds to surface. Recognized values are the strings `"start"`, `"end"`, `"comment"`, `"pi"`, `"start-ns"` and `"end-ns"`, where the two “ns” variants expose namespace declaration details. When *events* is left unset, the parser yields `"end"` notifications alone.

 feed(*data*)

Hand the supplied bytes over to the parser for processing.

 flush()

Forces the parser to process data that was fed earlier but not yet consumed, a handy way to obtain quicker results — notably when running against Expat >=2.6.0. Internally, `flush()` momentarily switches off Expat's reparse deferral (should it be active at the time) and kicks off a fresh parse. Be aware that turning reparse deferral off carries security implications; consult [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled) for the specifics.

Keep in mind that, as a security patch, `flush()` was also carried back into several earlier CPython builds. When your program has to run under many different Python releases, probe whether `flush()` exists by way of [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) first.

Added in version 3.13.

 close()

Tell the parser that no more input will arrive. In contrast to `XMLParser.close()`, the return value here is invariably [`None`](https://docs.python.org/3.14/library/constants.html#None). Should any events remain unread at close time, you can still pull them out via `read_events()`.

 read_events()

Hand back an iterator covering whatever events have turned up in the input given to the parser so far. What it produces are `(event, elem)` tuples, in which *event* holds a string naming the event kind (for instance `"end"`) and *elem* is the `Element` that was met, or some alternative context value per the list below.

- `start`, `end`: the Element being processed.

- `comment`, `pi`: the comment or processing instruction at hand

- `start-ns`: a `(prefix, uri)` tuple that identifies the namespace mapping just declared.

- `end-ns`: [`None`](https://docs.python.org/3.14/library/constants.html#None) (a later release could alter this)

Any event already handed out by an earlier `read_events()` invocation won't appear a second time. Because an event leaves the internal queue precisely at the moment the iterator surfaces it, having several consumers walk iterators from `read_events()` side by side leads to results you cannot rely on.

Note

At the instant a “start” event fires, all `XMLPullParser` promises is that the opening tag's “>” has been read; thus the attributes are populated, while whatever sits in the text and tail attributes is still undetermined. That uncertainty extends to the element's children, which may already exist or may not.

When a completely filled-in element is what you require, watch for “end” events in its place.

Added in version 3.4.

Changed in version 3.8: support for the `comment` and `pi` events arrived.

### Exceptions

 *class *xml.etree.ElementTree.ParseError

An XML parsing failure, thrown by this module's assorted parse routines whenever parsing breaks down. Converting one of these exception instances to a string gives you a readable error description. On top of that, the instance exposes these attributes:

 code

A numeric code reported by the expat parser. Refer to the [`xml.parsers.expat`](https://docs.python.org/3.14/library/pyexpat.html#module-xml.parsers.expat) documentation, which enumerates each error code along with what it signifies.

 position

A pair of *line*, *column* values pinpointing the spot at which the error arose.

Footnotes

[Subject index](INDEX.md)

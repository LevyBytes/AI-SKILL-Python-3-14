# email.message.Message: `walk()`

walk()

A general-purpose generator, `walk()` lets you step through every part and subpart within a message object tree, visiting them in depth-first order. The usual pattern puts `walk()` to work as the iterator driving a `for` loop, with each pass handing you the next subpart.

The snippet below walks a multipart message structure and prints the MIME type of every part it touches:

```pycon
>>> for part in msg.walk():
...     print(part.get_content_type())
multipart/report
text/plain
message/delivery-status
text/plain
text/plain
message/rfc822
text/plain

```

For any part whose `is_multipart()` yields `True`, `walk` steps into its subparts — and that holds even when `msg.get_content_maintype() == 'multipart'` happens to yield `False`. Our example makes this visible once we bring in the `_structure` debug helper function:

```pycon
>>> for part in msg.walk():
...     print(part.get_content_maintype() == 'multipart',
...           part.is_multipart())
True True
False False
False True
False False
False False
False True
False False
>>> _structure(msg)
multipart/report
    text/plain
    message/delivery-status
        text/plain
        text/plain
    message/rfc822
        text/plain

```

Notice that the `message` parts here are not `multiparts` themselves, yet subparts live inside them all the same. With `is_multipart()` reporting `True`, `walk` dives down into those subparts.

Beyond that, `Message` objects may optionally carry two instance attributes that come into play while producing the plain text form of a MIME message.

 preamble

A MIME document’s layout leaves room for some text sitting between the empty line that closes the headers and the opening multipart boundary string. As a rule that text stays hidden inside a MIME-aware mail reader, lying as it does beyond the usual MIME armor. Pull up the message’s raw text, though, or open it in a reader that knows nothing of MIME, and the text can surface.

It is the *preamble* attribute that stores this leading extra-armor text on MIME documents. Should the [`Parser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.Parser) come across text after the headers but ahead of the first boundary string, it stashes that text in the message’s *preamble* attribute. Later, while the [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) emits the plain text form of a MIME message and notices the message has a *preamble* attribute, it lays that text down in the gap between the headers and the first boundary. Turn to [`email.parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) and [`email.generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) for the particulars.

Bear in mind that a message object carrying no preamble leaves the *preamble* attribute set to `None`.

 epilogue

Operating just like the *preamble* attribute, the *epilogue* attribute differs only in holding the text found between the final boundary and where the message ends.

There is no need to assign the empty string to the epilogue for the [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) to emit a trailing newline at the file’s end.

 defects

Every problem encountered while parsing this message is collected into the list held by the *defects* attribute. A thorough rundown of the parsing defects you might encounter lives in [`email.errors`](https://docs.python.org/3.14/library/email.errors.html#module-email.errors).

[Subject index](INDEX.md) · [Previous](legacy-message-parameters-and-content-disposition.md) · [Owning module, declaration or section: email.message.Message](email-message-message-class.md)

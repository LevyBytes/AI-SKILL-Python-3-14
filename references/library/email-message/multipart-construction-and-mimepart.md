# EmailMessage multipart construction and MIMEPart

Invoke the *content_manager*'s [`set_content()`](https://docs.python.org/3.14/library/email.contentmanager.html#email.contentmanager.ContentManager.set_content) method, handing it self as the message object and forwarding whatever further positional or keyword arguments you have as extra arguments. Where *content_manager* goes unspecified, fall back on the `content_manager` that the current [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) names.

`make_related(*boundary=None*)`

Turn a message that is not yet `multipart` into a `multipart/related` one, relocating whatever *Content-* headers and payload already exist into a freshly made first part of the `multipart`. Supplying *boundary* makes that the boundary string for the multipart; leave it out and the boundary gets generated on its own once it becomes necessary (when the message is serialized, say).

`make_alternative(*boundary=None*)`

Take either a non-`multipart` message or a `multipart/related` one and recast it as `multipart/alternative`, shifting any present *Content-* headers along with the payload into a newly created first part of the `multipart`. When you pass *boundary*, it serves as the multipart's boundary string; otherwise the boundary is built automatically at the moment it is wanted (for instance, during message serialization).

`make_mixed(*boundary=None*)`

Promote a non-`multipart`, a `multipart/related`, or a `multipart-alternative` to `multipart/mixed`, carrying any current *Content-* headers and the payload over into a brand-new first part of the `multipart`. Should *boundary* be given, that becomes the boundary string used in the multipart; if not, the boundary is produced automatically the instant it is required (such as when the message is serialized).

`add_related(**args*, *content_manager=None*, ***kw*)`

When the message happens to be a `multipart/related`, build a fresh message object, feed every argument through to its `set_content()` method, and then [`attach()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) the result onto the `multipart`. Where the message is instead a non-`multipart`, run `make_related()` first and carry on just as described. For a `multipart` of any other kind, throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Leaving *content_manager* unspecified means the `content_manager` named by the current [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) is used. Should the part you add lack a *Content-Disposition* header, one is supplied carrying the value `inline`.

`add_alternative(**args*, *content_manager=None*, ***kw*)`

Given a message that is a `multipart/alternative`, make a new message object, route all the arguments into its `set_content()` method, and [`attach()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) it to the `multipart`. If what you have is a non-`multipart` or a `multipart/related`, invoke `make_alternative()` beforehand and then go on exactly as above. A `multipart` of some other variety prompts a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) to be raised. With *content_manager* left out, the `content_manager` that the current [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) specifies takes over.

`add_attachment(**args*, *content_manager=None*, ***kw*)`

Where the message is a `multipart/mixed`, spin up a new message object, deliver all the arguments to its `set_content()` method, and [`attach()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.attach) it onto the `multipart`. Should the message be a non-`multipart`, a `multipart/related`, or a `multipart/alternative`, call `make_mixed()` first and then continue in the manner above. When *content_manager* is not given, the `content_manager` from the current [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) applies. If the added part carries no *Content-Disposition* header, one with the value `attachment` is attached. You can lean on this method for both outright attachments (*Content-Disposition: attachment*) and `inline` ones (*Content-Disposition: inline*), simply by handing the `content_manager` the right options.

 clear()

Strip away the payload along with every header.

 clear_content()

Drop the payload and every *!Content-* header, while keeping all the remaining headers untouched and in the order they started.

The instance attributes carried by `EmailMessage` objects are these:

 preamble

A MIME document's layout permits a bit of text to sit between the blank line that comes after the headers and the first multipart boundary string. As a rule, a MIME-aware mail reader never shows this text, since it lies beyond the standard MIME armor. That said, it can surface when you look at the message's raw text or open the message in a reader that is not MIME aware.

For MIME documents, that leading extra-armor text is held in the *preamble* attribute. Whenever the [`Parser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.Parser) comes across text sitting after the headers yet ahead of the first boundary string, it stores that text on the message's *preamble* attribute. And when the [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) produces the plain-text rendering of a MIME message and notices a *preamble* attribute on it, it places that text in the space between the headers and the first boundary. Consult [`email.parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) and [`email.generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) for the specifics.

Bear in mind that when the message object carries no preamble, its *preamble* attribute holds `None`.

 epilogue

Working just like the *preamble* attribute, the *epilogue* attribute differs only in that it holds the text falling between the final boundary and the message's end. Much like the `preamble`, this attribute is `None` when no epilog text exists.

 defects

Every problem turned up while parsing this message is gathered into a list held by the *defects* attribute. Refer to [`email.errors`](https://docs.python.org/3.14/library/email.errors.html#module-email.errors) for a thorough rundown of the parsing defects that can occur.

`*class *email.message.MIMEPart(*policy=default*)`

A subpart of a MIME message is what this class stands for. It matches `EmailMessage` in every respect but one: calling `set_content()` adds no *MIME-Version* headers, because sub-parts have no need for *MIME-Version* headers of their own.

Footnotes

[Subject index](INDEX.md)

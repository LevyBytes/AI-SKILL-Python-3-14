# email.parser: `email.parser.BytesFeedParser`

### FeedParser API

Available from the `email.feedparser` module, the `BytesFeedParser` offers an interface suited to chewing through email a chunk at a time — exactly what you want when a message arrives from a source liable to block, such as a socket. You can certainly point `BytesFeedParser` at an email already held whole in a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), string, or file, yet for those situations the `BytesParser` interface often proves handier. Either parser produces the same behaviour and the same output.

Using `BytesFeedParser` is straightforward: build one, keep handing it bytes until you have none left, then close it to collect the root message object. Against messages that obey the standards `BytesFeedParser` is highly precise, and even with malformed input it parses gracefully while reporting what made the message look broken. Any issues it spots are recorded on the message object's [`defects`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.defects) attribute as a list. Consult the [`email.errors`](https://docs.python.org/3.14/library/email.errors.html#module-email.errors) module for the full roster of defects it knows how to detect.

What follows is the `BytesFeedParser` interface:

`*class *email.parser.BytesFeedParser(*_factory=None*, ***, *policy=policy.compat32*)`

Construct a `BytesFeedParser`. The optional *_factory* is a callable taking no arguments; leave it out and the parser draws the [`message_factory`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.message_factory) from the *policy* instead. Each time a fresh message object is required, *_factory* gets invoked.

Pass a *policy* and its rules govern how the message representation gets shaped. Omit it and the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32) policy applies, preserving the behaviour of the email package as it stood in Python 3.2 and supplying [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) as the factory by default. Every other policy hands you [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) instead for the default *_factory*. The [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) documentation spells out everything else *policy* governs.

Note: **The policy keyword should always be specified**; a coming Python release will switch the default over to [`email.policy.default`](https://docs.python.org/3.14/library/email.policy.html#email.policy.default).

Added in version 3.2.

Changed in version 3.3: Added the *policy* keyword.

Changed in version 3.6: *_factory* defaults to the policy `message_factory`.

[Subject index](INDEX.md) · [Previous](email-parser-parsing-email-messages.md) · [Continue](incremental-byte-parser-feed-and-close.md) · [Owning module, declaration or section: email.parser](email-parser-parsing-email-messages.md)

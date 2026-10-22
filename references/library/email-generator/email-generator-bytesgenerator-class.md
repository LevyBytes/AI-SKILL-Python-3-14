# email.generator: `email.generator.BytesGenerator`

# Email.Generator

### `email.generator`: Generating MIME documents

**Source code:** [Lib/email/generator.py](https://github.com/python/cpython/tree/3.14/Lib/email/generator.py)

---

A frequent need is producing the flat, serialized form of the email that a message object structure stands for. That step is unavoidable when you intend to hand your message off through [`smtplib.SMTP.sendmail()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.sendmail) or echo it to the console. Turning a message object structure into a serialized form is precisely what the generator classes handle.

Just like the [`email.parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) module, nothing confines you to the supplied generator — rolling your own is always an option. Still, the supplied one already produces standards-compliant output for most email, copes equally well with MIME and non-MIME messages, and is built so that its byte-level parsing and generation undo each other, provided both sides share the same non-transforming [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy). Put differently, reading a serialized byte stream through the [`BytesParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.BytesParser) class and then re-emitting it with `BytesGenerator` ought to give output matching the original input [1]. (Conversely, running the generator over an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) you built in code can alter that `EmailMessage` object as defaults get supplied.)

You can lean on the `Generator` class to flatten a message into a text serialized form rather than a binary one, but because Unicode has no direct way to hold binary data, the message must be reshaped into something built solely from ASCII characters — done with the usual email RFC Content Transfer Encoding methods that prepare messages for travel across channels which are not “8 bit clean”.

So that SMIME-signed messages can be processed reproducibly, `Generator` switches off header folding for any message part whose type is `multipart/signed`, along with every subpart beneath it.

 *class *email.generator.BytesGenerator(*outfp*, *mangle_from_=None*, *maxheaderlen=None*, ***, *policy=None*)

Hands back a `BytesGenerator` object that sends whatever message you give its `flatten()` method, plus any surrogateescape-encoded text you give its `write()` method, into the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) *outfp*. That *outfp* has to offer a `write` method capable of taking binary data.

When the optional *mangle_from_* is `True`, a `>` character is prepended to every body line beginning with the literal `"From "` — that is, `From` trailed by a space right at a line's start. The default for *mangle_from_* comes from the *policy*'s [`mangle_from_`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.mangle_from_) setting, which is `True` under the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) policy and `False` everywhere else. The point of *mangle_from_* is storing messages in Unix mbox format (consult [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) and [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)).

Should *maxheaderlen* hold a value other than `None`, header lines exceeding *maxheaderlen* get refolded; a value of `0` means no header is rewrapped at all. With *manheaderlen* left at `None` (the default), headers and the rest of the message lines are wrapped per the *policy* settings.

When *policy* is given, that policy steers message generation. When *policy* is `None` (the default), generation follows the policy tied to the [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) or [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) object handed to `flatten`. Look to [`email.policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) for the full account of what *policy* governs.

Added in version 3.2.

Changed in version 3.3: The *policy* keyword was introduced.

Changed in version 3.6: By default, the *mangle_from_* and *maxheaderlen* parameters now take their cue from the policy.

[Subject index](INDEX.md) · [Continue](byte-generator-flattening-and-output.md)

# email.generator: `email.generator.Generator`, `flatten()`, `clone()`, `write()`

*class *email.generator.Generator(*outfp*, *mangle_from_=None*, *maxheaderlen=None*, ***, *policy=None*)

Yields a `Generator` object that pushes whatever message reaches its `flatten()` method, and whatever text reaches its `write()` method, into the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-like-object) *outfp*. The *outfp* must furnish a `write` method that takes string data.

Setting the optional *mangle_from_* to `True` causes a `>` character to be inserted ahead of each body line that opens with the literal `"From "` — meaning `From` immediately trailed by a space at the line's start. Its default tracks the *policy*'s [`mangle_from_`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.mangle_from_) setting: `True` for the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) policy, `False` otherwise. You'd want *mangle_from_* when messages live in Unix mbox format (refer to [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) and [WHY THE CONTENT-LENGTH FORMAT IS BAD](https://www.jwz.org/doc/content-length.html)).

Give *maxheaderlen* any value besides `None` and header lines running past *maxheaderlen* are refolded; supply `0` and no headers get rewrapped. Leave *manheaderlen* at `None` (its default) and the headers plus other message lines are wrapped following the *policy* settings.

Name a *policy* and that policy directs how the message is generated. Leave *policy* as `None` (the default) and the work is steered by the policy attached to whichever [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) or [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) object you passed to `flatten`. Consult [`email.policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) for what falls under *policy*'s control.

Changed in version 3.3: A *policy* keyword was added.

Changed in version 3.6: The *mangle_from_* and *maxheaderlen* parameters default, as of this release, to honoring the policy.

 flatten(*msg*, *unixfrom=False*, *linesep=None*)

Emits the textual rendering of the message object structure rooted at *msg* to the output file that was designated when the `Generator` instance was built.

Where the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) option [`cte_type`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.cte_type) holds `8bit`, the message is produced just as though the option read `7bit` instead. (That fallback is necessary because strings have no means of holding non-ASCII bytes.) High-bit bytes are converted where needed through an ASCII-compatible *Content-Transfer-Encoding*. Concretely, parts bearing a non-ASCII *Content-Transfer-Encoding* (*Content-Transfer-Encoding: 8bit*) are remade into an ASCII compatible *Content-Transfer-Encoding*, and non-ASCII header bytes that break the RFC are encoded under the MIME `unknown-8bit` character set, which brings them back into RFC-compliance.

Turn *unixfrom* to `True` and the Unix-mailbox-format envelope header delimiter (see [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox)) is written out in front of the root message object's first [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) header. Should the root object carry no envelope header, a standard one is invented. Its default value is `False`. Keep in mind that an envelope header is never printed for subparts.

Hand *linesep* anything but `None` and it serves as the separator dividing every line of the flattened message. With *linesep* at `None` (the default), the *policy*'s configured value is used.

Changed in version 3.2: Re-encoding of `8bit` message bodies became supported, alongside the *linesep* argument.

 clone(*fp*)

Yields a self-contained clone of this `Generator` instance sharing all the same options, with *fp* taking over as the new *outfp*.

 write(*s*)

Sends *s* to the *write* method of the *outfp* that reached the `Generator`'s constructor. This exposes barely enough of a file-like API that `Generator` instances will work inside the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function.

For convenience, [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) supplies the [`as_string()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.as_string) method and `str(aMessage)` (also called [`__str__()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.__str__)), which ease producing a formatted string form of a message object. Fuller specifics appear in [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message).

The `email.generator` module additionally offers a subclass, `DecodedGenerator`, that behaves like the `Generator` base class apart from how it treats non-*text* parts: rather than serializing them, it stands them in within the output stream using a string built from a template populated with details about the part.

[Subject index](INDEX.md) · [Previous](byte-generator-flattening-and-output.md) · [Continue](email-generator-decodedgenerator-class.md) · [Owning module, declaration or section: email.generator](email-generator-bytesgenerator-class.md)

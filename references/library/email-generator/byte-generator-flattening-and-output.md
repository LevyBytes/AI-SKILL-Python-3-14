# email.generator.BytesGenerator: `flatten()`, `clone()`, `write()`

flatten(*msg*, *unixfrom=False*, *linesep=None*)

Writes the textual rendering of the message object structure whose root is *msg* into the output file that was named when the `BytesGenerator` instance got created.

When the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) option [`cte_type`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.cte_type) sits at `8bit` (its default), every untouched header from the originally parsed message is copied straight through, any high-bit bytes reproduced exactly as they were, and the non-ASCII *Content-Transfer-Encoding* of any body part that carries one is left intact. When `cte_type` is `7bit` instead, high-bit bytes are converted as required by way of an ASCII-compatible *Content-Transfer-Encoding*. In concrete terms, parts whose *Content-Transfer-Encoding* is non-ASCII (*Content-Transfer-Encoding: 8bit*) become an ASCII compatible *Content-Transfer-Encoding*, while RFC-invalid non-ASCII header bytes are encoded with the MIME `unknown-8bit` character set so they end up RFC-compliant.

With *unixfrom* set to `True`, the envelope header delimiter that the Unix mailbox format uses (see [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox)) is emitted ahead of the root message object's first [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) header. Where the root object lacks an envelope header, a standard one is fabricated. This defaults to `False`. Bear in mind that subparts never have an envelope header printed for them.

When *linesep* is something other than `None`, it becomes the separator placed between all lines of the flattened message. When *linesep* is `None` (the default), the value drawn from the *policy* applies.

 clone(*fp*)

Hands back a standalone clone of this `BytesGenerator` instance carrying the very same option settings, with *fp* serving as the fresh *outfp*.

 write(*s*)

Runs *s* through the `ASCII` codec together with the `surrogateescape` error handler, then forwards the result to the *write* method of the *outfp* that was supplied to the `BytesGenerator`'s constructor.

For convenience, [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) offers the [`as_bytes()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.as_bytes) method and `bytes(aMessage)` (otherwise known as [`__bytes__()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.__bytes__)), which make building a serialized binary form of a message object easier. Further specifics live in [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message).

Since strings have no way to carry binary data, the `Generator` class is obliged to recast any binary content in a message it flattens into an ASCII compatible shape, accomplished by switching it to an ASCII compatible *Content-Transfer_Encoding*. Borrowing the email RFCs' vocabulary, picture `Generator` as serializing onto an I/O stream that isn't “8 bit clean”. The upshot is that the majority of applications should prefer `BytesGenerator` over `Generator`.

[Subject index](INDEX.md) · [Previous](email-generator-bytesgenerator-class.md) · [Continue](text-generator-class-and-output.md) · [Owning module, declaration or section: email.generator](email-generator-bytesgenerator-class.md) · [Owning module, declaration or section: email.generator.BytesGenerator](email-generator-bytesgenerator-class.md)

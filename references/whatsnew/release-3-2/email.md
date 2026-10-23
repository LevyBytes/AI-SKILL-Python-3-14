# What's New In Python 3.2 / email - email, email.compat32-message, email.generator, email.parser, smtplib

### email

Through the wide-ranging work of R. David Murray, the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package is now largely usable in Python 3. The trouble stemmed from emails generally being read and held as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) rather than [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) text, and they can carry several encodings inside one email. Therefore the email package needed extending so it could parse and produce email messages in bytes form.

- Fresh functions [`message_from_bytes()`](https://docs.python.org/3.14/library/email.parser.html#email.message_from_bytes) and [`message_from_binary_file()`](https://docs.python.org/3.14/library/email.parser.html#email.message_from_binary_file), plus new classes [`BytesFeedParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.BytesFeedParser) and [`BytesParser`](https://docs.python.org/3.14/library/email.parser.html#email.parser.BytesParser), make it possible to parse binary message data into model objects.

- When the model is fed bytes input, [`get_payload()`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload) defaults to decoding a message body whose *Content-Transfer-Encoding* is *8bit*, using the charset named in the MIME headers, and hands back the resulting string.

- When the model is fed bytes input, [`Generator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.Generator) rewrites message bodies whose *Content-Transfer-Encoding* is *8bit* so they instead carry a *7bit* *Content-Transfer-Encoding*.

Any headers bearing unencoded non-ASCII bytes are treated as [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html)-encoded with the *unknown-8bit* character set.

- A fresh class [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator) emits bytes as its output, holding onto any untouched non-ASCII data that appeared in the input from which the model was built, message bodies with a *Content-Transfer-Encoding* of *8bit* included.

- The [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) [`SMTP`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP) class will now take a byte string for the *msg* argument given to the [`sendmail()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.sendmail) method, and a fresh method, [`send_message()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.send_message), takes a [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) object and may optionally pull the *from_addr* and *to_addrs* addresses straight from that object.

(Proposed and implemented by R. David Murray, [bpo-4661](https://bugs.python.org/issue?@action=redirect&bpo=4661) and [bpo-10321](https://bugs.python.org/issue?@action=redirect&bpo=10321).)

[Subject index](INDEX.md) · [Previous source section](new-improved-and-deprecated-modules.md) · [Next source section](elementtree.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)

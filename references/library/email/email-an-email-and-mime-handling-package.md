# email`email` - An email and MIME handling package

### `email` - An email and MIME handling package

**Source code:** [Lib/email/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/email/__init__.py)

---

The `email` package serves as a library for working with email messages. It is deliberately *not* built to push email messages out to SMTP ([**RFC 2821**](https://datatracker.ietf.org/doc/html/rfc2821.html)), NNTP, or any other servers — that job belongs to modules like [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib). Aiming for the highest RFC compliance it can manage, the `email` package backs [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) and [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html), along with the MIME-oriented RFCs [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html), [**RFC 2046**](https://datatracker.ietf.org/doc/html/rfc2046.html), [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html), [**RFC 2183**](https://datatracker.ietf.org/doc/html/rfc2183.html), and [**RFC 2231**](https://datatracker.ietf.org/doc/html/rfc2231.html).

At a high level, the email package breaks down into three principal components, together with a fourth one that governs how the others behave.

At the heart of the package sits an “object model” that stands in for email messages. Most of an application’s dealings with the package go through the object model interface laid out in the [`message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) sub-module. Through this API an application can interrogate an existing email, assemble a fresh one, or insert and strip out email subcomponents that themselves rely on the very same object model interface. In other words, mirroring how email messages and their MIME subcomponents are organized, the email object model takes the form of a tree of objects, each one exposing the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) API.

The package’s remaining two principal components are the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) and the [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator). Handed the serialized form of an email message — a byte stream — the parser builds it into a tree of [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) objects. The generator goes the other direction, taking an `EmailMessage` and reducing it back to a serialized byte stream. (Text-character streams are something the parser and generator can cope with too, but going that route is advised against, since it is all too simple to wind up with messages that turn out invalid for one reason or another.)

Steering everything is the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) module. A `policy` object is tied to every [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage), every [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator), and every [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser), dictating how each one acts. In most cases an application has to name the policy only at the point an `EmailMessage` comes into being — whether by instantiating an `EmailMessage` outright for a brand-new email or by feeding an input stream through a `parser`. That policy can still be swapped at serialization time via a `generator`, though. So you might, for instance, read a plain email message off disk and then write it out under standard SMTP settings as you dispatch it to an email server.

As much as it can, the email package keeps the particulars of the assorted governing RFCs out of the application’s view. In principle the application ought to be free to regard an email message as an orderly tree of unicode text and binary attachments, never minding how those get encoded once serialized. Real-world use, though, frequently demands at least passing familiarity with some of the rules that shape MIME messages and their layout — above all the labels and meaning of the MIME “content types” and the way they mark out multipart documents. By and large only the more involved applications will need that understanding, and even there it tends to concern just the top-level structure rather than the fine points of how those structures get encoded. Because MIME content types crop up everywhere in today’s internet software (email being only part of it), plenty of programmers will already find the idea familiar.

What the `email` package can do is laid out across the sections that follow. The starting point is the [`message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) object model — the interface an application leans on most — after which come the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) and [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) components. From there the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) controls round out the discussion of the library’s core components.

The three sections after that deal with the exceptions the package can throw and the defects — departures from the RFCs — that the [`parser`](https://docs.python.org/3.14/library/email.parser.html#module-email.parser) is able to flag. Following them, the [`headerregistry`](https://docs.python.org/3.14/library/email.headerregistry.html#module-email.headerregistry) and [`contentmanager`](https://docs.python.org/3.14/library/email.contentmanager.html#module-email.contentmanager) sub-components get their turn; they supply tooling for finer-grained work on headers and payloads, in that order. Each of these two components offers capabilities geared toward reading and writing non-trivial messages, and each also spells out its extensibility APIs, of interest to more advanced applications.

After all of that comes a collection of examples that exercise the core pieces of the APIs introduced in the earlier sections.

Everything described so far makes up the email package’s modern, unicode-friendly API. The sections still to come, opening with the [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) class, document the older [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) API, which engages far more directly with the particulars of how email messages are encoded. Unlike the modern one, the `compat32` API does *not* shield the application from the RFC particulars, yet for applications obliged to work at that depth it can prove a handy toolset. This material likewise applies to applications that lean on the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) API for the sake of backward compatibility.

Changed in version 3.6: The documentation was restructured and rewritten to put the new [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage)/[`EmailPolicy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy) API front and center.

Contents of the `email` package documentation:

- [`email.message`: Representing an email message](https://docs.python.org/3.14/library/email.message.html)
- [`email.parser`: Parsing email messages](https://docs.python.org/3.14/library/email.parser.html)
  - [FeedParser API](https://docs.python.org/3.14/library/email.parser.html#feedparser-api)
  - [Parser API](https://docs.python.org/3.14/library/email.parser.html#parser-api)
  - [Additional notes](https://docs.python.org/3.14/library/email.parser.html#additional-notes)

- [`email.generator`: Generating MIME documents](https://docs.python.org/3.14/library/email.generator.html)
- [`email.policy`: Policy Objects](https://docs.python.org/3.14/library/email.policy.html)
- [`email.errors`: Exception and Defect classes](https://docs.python.org/3.14/library/email.errors.html)
- [`email.headerregistry`: Custom Header Objects](https://docs.python.org/3.14/library/email.headerregistry.html)
- [`email.contentmanager`: Managing MIME Content](https://docs.python.org/3.14/library/email.contentmanager.html)
  - [Content Manager Instances](https://docs.python.org/3.14/library/email.contentmanager.html#content-manager-instances)

- [`email`: Examples](https://docs.python.org/3.14/library/email.examples.html)

Legacy API:

- [`email.message.Message`: Representing an email message using the `compat32` API](https://docs.python.org/3.14/library/email.compat32-message.html)
- [`email.mime`: Creating email and MIME objects from scratch](https://docs.python.org/3.14/library/email.mime.html)
- [`email.header`: Internationalized headers](https://docs.python.org/3.14/library/email.header.html)
- [`email.charset`: Representing character sets](https://docs.python.org/3.14/library/email.charset.html)
- [`email.encoders`: Encoders](https://docs.python.org/3.14/library/email.encoders.html)
- [`email.utils`: Miscellaneous utilities](https://docs.python.org/3.14/library/email.utils.html)
- [`email.iterators`: Iterators](https://docs.python.org/3.14/library/email.iterators.html)

See also

Module [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib)

SMTP (Simple Mail Transport Protocol) client

Module [`poplib`](https://docs.python.org/3.14/library/poplib.html#module-poplib)

POP (Post Office Protocol) client

Module [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib)

IMAP (Internet Message Access Protocol) client

Module [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox)

Utilities for building, reading, and maintaining on-disk message collections across a range of standard formats.

[Subject index](INDEX.md) · [Previous](an-email-and-mime-handling-package.md) · [Continue](../email-iterators/message-body-and-structure-iteration.md)

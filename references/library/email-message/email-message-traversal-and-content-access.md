# email.message.EmailMessage: `walk()`, `get_body()`, `iter_attachments()`, `iter_parts()`, `get_content()`, `set_content()`

walk()

The `walk()` method is a versatile generator you can use to step through every part and subpart of a message object tree, in depth-first traversal order. Typically you employ `walk()` as the iterator within a `for` loop; each pass returns the next subpart.

Below is an example that prints the MIME type of each part within a multipart message structure:

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

`walk` steps through the subparts of any part for which `is_multipart()` yields `True`, even when `msg.get_content_maintype() == 'multipart'` may yield `False`. Our example demonstrates this by drawing on the `_structure` debug helper function:

```pycon
>>> from email.iterators import _structure
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

Here the `message` parts are not `multiparts`, yet they do hold subparts. `is_multipart()` yields `True` and `walk` descends into the subparts.

 get_body(*preferencelist=('related', 'html', 'plain')*)

Yield the MIME part that stands as the best candidate to serve as the “body” of the message.

*preferencelist* has to be a sequence of strings drawn from the set `related`, `html`, and `plain`, and it conveys the order of preference for the content type of the part returned.

Begin the search for candidate matches at the object on which `get_body` was invoked.

When `related` is left out of *preferencelist*, treat the root part (or a subpart of the root part) of any related encountered as a candidate provided the (sub-)part fits a preference.

Upon meeting a `multipart/related`, inspect the `start` parameter, and when a part with a matching *Content-ID* is located, weigh only it while seeking candidate matches. Otherwise weigh only the first (default root) part of the `multipart/related`.

When a part carries a *Content-Disposition* header, treat the part as a candidate match only when that header's value is `inline`.

When none of the candidates fits any of the preferences in *preferencelist*, yield `None`.

Notes: (1) For the majority of applications the only *preferencelist* combinations that truly make sense are `('plain',)`, `('html', 'plain')`, and the default `('related', 'html', 'plain')`. (2) Since matching begins at the object on which `get_body` is invoked, calling `get_body` on a `multipart/related` returns the object itself unless *preferencelist* carries a non-default value. (3) Messages (or message parts) that omit a *Content-Type* or whose *Content-Type* header is invalid are handled as though they are of type `text/plain`, which can sometimes make `get_body` yield surprising results.

 iter_attachments()

Yield an iterator over every immediate sub-part of the message that is not a candidate “body” part. Put differently, pass over the initial occurrence of each of `text/plain`, `text/html`, `multipart/related`, or `multipart/alternative` (except where an explicit *Content-Disposition: attachment* flags them as attachments), then yield whatever parts remain. Applied straight to a `multipart/related`, yield an iterator over all the related parts barring the root part (that is, the part pointed to by the `start` parameter, or the first part when there is no `start` parameter or the `start` parameter fails to match the *Content-ID* of any of the parts). Applied straight to a `multipart/alternative` or a non-`multipart`, yield an empty iterator.

 iter_parts()

Yield an iterator over every immediate sub-part of the message, which is empty for a non-`multipart`. (Refer also to `walk()`.)

 get_content(**args*, *content_manager=None*, ***kw*)

Invoke the [`get_content()`](https://docs.python.org/3.14/library/email.contentmanager.html#email.contentmanager.ContentManager.get_content) method of the *content_manager*, handing self in as the message object, and forwarding any further arguments or keywords as extra arguments. When *content_manager* is left unspecified, use the `content_manager` named by the current [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy).

 set_content(**args*, *content_manager=None*, ***kw*)

[Subject index](INDEX.md) · [Previous](email-message-parameters-and-disposition.md) · [Owning module, declaration or section: email.message](email-message-emailmessage-class.md) · [Owning module, declaration or section: email.message.EmailMessage](email-message-emailmessage-class.md)

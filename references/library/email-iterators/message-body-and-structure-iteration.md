# email.iterators — `email.iterators`: Iterators

## email.iterators: Iterators

### `email.iterators`: Iterators

**Source code:** [Lib/email/iterators.py](https://github.com/python/cpython/tree/3.14/Lib/email/iterators.py)

---

Walking a message object tree is reasonably straightforward thanks to the [`Message.walk`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.walk) method. On top of that, the `email.iterators` module offers a few handy higher-level ways to iterate across message object trees.

 email.iterators.body_line_iterator(*msg*, *decode=False*)

This steps through every payload across all of *msg*’s subparts, handing back the string payloads one line at a time. Subpart headers are bypassed, as is any subpart whose payload is not a Python string. It behaves roughly like pulling the message’s flat text form out of a file with [`readline()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.readline) while passing over all the headers in between.

The optional *decode* argument is handed straight along to [`Message.get_payload`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message.get_payload).

 email.iterators.typed_subpart_iterator(*msg*, *maintype='text'*, *subtype=None*)

This walks through each of *msg*’s subparts and yields back only the ones whose MIME type lines up with the *maintype* and *subtype* you gave.

Keep in mind that *subtype* may be left out; when it is, subpart MIME type matching considers the main type alone. *maintype* is likewise optional and falls back to *text*.

So, with nothing specified, `typed_subpart_iterator()` yields every subpart carrying a MIME type of *text/**.

The function below was introduced as a handy aid for debugging. It is *not* meant to count as part of the package’s supported public interface.

 email.iterators._structure(*msg*, *fp=None*, *level=0*, *include_default=False*)

Writes out an indented rendering of the content types making up the message object structure. As an illustration:

```pycon
>>> msg = email.message_from_file(somefile)
>>> _structure(msg)
multipart/mixed
    text/plain
    text/plain
    multipart/digest
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
        message/rfc822
            text/plain
    text/plain

```

The optional *fp* is a file-like object that receives the printed output, and it has to work with Python’s [`print()`](https://docs.python.org/3.14/library/functions.html#print) function. *level* serves an internal purpose. When *include_default* is true, the default type gets printed as well.

[Subject index](INDEX.md) · [Owning module, declaration or section: email](../email/email-an-email-and-mime-handling-package.md)

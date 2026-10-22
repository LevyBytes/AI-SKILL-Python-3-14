# email.policy: `email.policy.Policy`, `clone()`, `handle_defect()`, `register_defect()`, `header_max_count()`

*class *email.policy.Policy(***kw*)

Here is the [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) underlying every policy class. It supplies default implementations for a pair of trivial methods, plus the implementation of the immutability property, the `clone()` method, and the constructor semantics.

You may pass assorted keyword arguments to a policy class constructor. The permitted arguments are whatever non-method properties exist on this class, together with any further non-method properties belonging to the concrete class. Supplying a value in the constructor overrides the default value of the matching attribute.

The following properties are defined by this class, so values for each of these may be supplied to the constructor of any policy class:

 max_line_length

The longest a line in the serialized output may be, excluding the end of line character(s). The default is 78, in keeping with [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html). Setting this to `0` or [`None`](https://docs.python.org/3.14/library/constants.html#None) means no line wrapping should occur whatsoever.

 linesep

The string used to end lines within serialized output. It defaults to `\n`, since that is Python’s own internal end-of-line discipline, even though the RFCs call for `\r\n`.

 cte_type

Governs which kinds of Content Transfer Encodings may be used or are mandatory. The available values are:

| `7bit` | every byte of data has to stay “7 bit clean” (ASCII-only). Wherever that requires it, the data gets encoded by way of either quoted-printable or base64 encoding. |
| --- | --- |
| `8bit` | there is no restriction forcing the data to be 7 bit clean. Header data must still stay ASCII-only and will thus be encoded (consult `fold_binary()` together with `utf8` further down for the exceptions), though body parts are free to apply the `8bit` CTE. |

Setting `cte_type` to `8bit` is only effective with `BytesGenerator`, never `Generator`, given that strings are unable to hold binary data. Where a `Generator` runs under a policy declaring `cte_type=8bit`, it behaves as though `cte_type` were `7bit`.

 raise_on_defect

When [`True`](https://docs.python.org/3.14/library/constants.html#True), every defect that turns up is raised as an error. When [`False`](https://docs.python.org/3.14/library/constants.html#False) (the default), defects instead go to the `register_defect()` method.

 mangle_from_

When [`True`](https://docs.python.org/3.14/library/constants.html#True), any body line beginning with *“From “* is escaped by placing a `>` ahead of it. This parameter comes into play while a generator is serializing the message. Default: [`False`](https://docs.python.org/3.14/library/constants.html#False).

Added in version 3.5.

 message_factory

A factory function used to build a fresh empty message object. The parser uses it while assembling messages. It defaults to `None`, which causes [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) to be used.

Added in version 3.6.

 verify_generated_headers

When `True` (the default), rather than emitting a header that is folded or delimited badly — to the point that it would parse as several headers or fuse with neighboring data — the generator raises [`HeaderWriteError`](https://docs.python.org/3.14/library/email.errors.html#email.errors.HeaderWriteError). Headers like that can come from custom header classes or from defects in the `email` module.

Since this is a security feature, it defaults to `True` even under the `Compat32` policy. To get the backwards compatible, though unsafe, behavior, you must set it to `False` deliberately.

Added in version 3.13.

The `Policy` method below is meant to be invoked by code that uses the email library to build policy instances carrying custom settings:

 clone(***kw*)

Hand back a new `Policy` instance whose attributes carry the same values as the present instance, save for any attributes assigned fresh values by the keyword arguments.

The rest of the `Policy` methods get invoked by the email package’s own code and are not meant to be invoked by an application that uses the email package. Every one of these methods must be implemented by a custom policy.

 handle_defect(*obj*, *defect*)

Deal with a *defect* discovered on *obj*. Whenever the email package invokes this method, *defect* is guaranteed to be a subclass of [`MessageDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.MessageDefect).

The default implementation inspects the `raise_on_defect` flag. Where it is `True`, *defect* gets raised as an exception. Where it is `False` (the default), both *obj* and *defect* are handed to `register_defect()`.

 register_defect(*obj*, *defect*)

Record a *defect* against *obj*. Within the email package, *defect* will invariably be a subclass of [`MessageDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.MessageDefect).

The default implementation invokes the `append` method belonging to the `defects` attribute of *obj*. By the time the email package invokes `handle_defect`, *obj* will ordinarily carry a `defects` attribute that owns an `append` method. Custom object types employed with the email package (such as custom `Message` objects) ought to expose such an attribute too; otherwise, defects in parsed messages will trigger unexpected errors.

 header_max_count(*name*)

Hand back the largest permitted count of headers named *name*.

Invoked whenever a header is added to an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) or [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) object. Should the returned value be neither `0` nor `None`, and the count of existing headers with the name *name* already meets or exceeds that returned value, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Given that `Message.__setitem__` defaults to appending the value onto the list of headers, duplicate headers can sprout unintentionally with ease. This method lets particular headers be capped on how many copies of that header may be added to a `Message` programmatically. (That cap is ignored by the parser, which will dutifully emit as many headers as the message being parsed contains.)

The default implementation hands back `None` for every header name.

[Subject index](INDEX.md) · [Previous](email-policy-policy-objects.md) · [Continue](base-policy-header-parsing-and-folding.md) · [Owning module, declaration or section: email.policy](email-policy-policy-objects.md)

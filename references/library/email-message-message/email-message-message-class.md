# email.message.Message: `email.message.Message`

### `email.message.Message`: Representing an email message using the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.compat32) API

The `Message` class closely resembles the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class, but it lacks the methods that the latter class introduces, and a few of its other methods behave somewhat differently by default. A handful of methods documented here are also available on the `EmailMessage` class, but you should avoid them except when maintaining legacy code.

Apart from that, both classes share the same design and underlying philosophy.

The behavior covered here applies under the policy that is the default for `Message`, namely [`Compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32). Should you intend to adopt a different policy, the [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) class is the one you ought to choose instead.

Every email message is made up of *headers* together with a *payload*. The headers follow [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) conventions for names and values, with a colon dividing each field name from its value. That colon belongs to neither the field name nor the field value. As for the payload, it can be plain text, a binary object, or a structured collection of sub-messages, each carrying its own headers along with its own payload. A message signals the latter kind of payload by carrying a MIME type like *multipart/** or *message/rfc822*.

The mental model a `Message` object presents is an ordered dictionary of headers, augmented with extra methods that reach specialized data within the headers, reach the payload, build a serialized form of the message, and recursively traverse the object tree. Keep in mind that although repeated headers are allowed, you have to reach them through dedicated methods.

Indexing into the `Message` pseudo-dictionary uses the header names, all of which must be ASCII. The dictionary's values are strings expected to hold only ASCII characters; non-ASCII input gets some special treatment, though that treatment isn't always correct. Headers keep their original case when stored and returned, yet field-name matching ignores case. A lone envelope header may also be present, referred to as the *Unix-From* header or the `From_` header. For straightforward message objects the *payload* is a string or bytes, whereas for MIME container documents (such as *multipart/** and *message/rfc822*) it is a list of `Message` objects.

These are the methods belonging to the `Message` class:

 *class *email.message.Message(*policy=compat32*)

When *policy* is given (it has to be an instance of one of the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) classes), the rules it defines govern how the message representation is updated and serialized. Leaving *policy* unset selects the [`compat32`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32) policy, which preserves backward compatibility with the email package as shipped in Python 3.2. The `policy` documentation has further details.

Changed in version 3.3: The *policy* keyword argument was added.

[Subject index](INDEX.md) · [Continue](legacy-message-serialization-and-payload-access.md)

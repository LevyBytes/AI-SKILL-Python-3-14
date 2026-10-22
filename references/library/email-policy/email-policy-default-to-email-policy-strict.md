# email.policy: `email.policy.default`, `email.policy.SMTP`, `email.policy.SMTPUTF8`, `email.policy.HTTP`, `email.policy.strict`

email.policy.default

An `EmailPolicy` instance with every default left as-is. This policy applies the standard Python `\n` line endings in place of the RFC-correct `\r\n`.

 email.policy.SMTP

Fitted for serializing messages in conformance with the email RFCs. Like `default`, only with `linesep` set to `\r\n`, which is RFC compliant.

 email.policy.SMTPUTF8

Identical to `SMTP` save that `utf8` is `True`. Handy for serializing messages into a message store without resorting to encoded words in the headers. It should be used for SMTP transmission only when the sender or recipient addresses carry non-ASCII characters (the [`smtplib.SMTP.send_message()`](https://docs.python.org/3.14/library/smtplib.html#smtplib.SMTP.send_message) method takes care of this on its own).

 email.policy.HTTP

Fitted for serializing headers with for use in HTTP traffic. Like `SMTP` save that `max_line_length` is set to `None` (unlimited).

 email.policy.strict

A convenience instance. Identical to `default` save that `raise_on_defect` is set to `True`. This lets any policy be turned strict by writing:

```python
somepolicy + policy.strict

```

Under all of these `EmailPolicies`, the email package’s effective API departs from the Python 3.2 API in the ways below:

- Assigning a header on a [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) leads to that header being parsed and a header object being built.

- Retrieving a header value off a [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) leads to that header being parsed and a header object being built and returned.

- Every header object, along with any header that gets refolded on account of the policy settings, is folded by an algorithm that fully implements the RFC folding algorithms, including grasping where encoded words are required and allowed.

[Subject index](INDEX.md) · [Previous](email-policy-class-and-header-folding.md) · [Owning module, declaration or section: email.policy](email-policy-policy-objects.md) · [Required continuation of the source contract](email-policy-compat32-class-to-email-policy-compat32.md)

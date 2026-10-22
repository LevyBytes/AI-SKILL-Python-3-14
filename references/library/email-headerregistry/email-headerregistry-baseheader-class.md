# email.headerregistry — `email.headerregistry`: Custom Header Objects

# Email.Headerregistry

### `email.headerregistry`: Custom Header Objects

**Source code:** [Lib/email/headerregistry.py](https://github.com/python/cpython/tree/3.14/Lib/email/headerregistry.py)

---

Added in version 3.6: [1]

Each header is modeled by a tailored subclass of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). Which specific class stands in for a particular header is decided by the [`header_factory`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.header_factory) belonging to the [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) active at the moment the headers come into being. What this section describes is the specific `header_factory` that the email package supplies for working with [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) compliant email messages; it both furnishes tailored header objects across the various header types and gives applications an extension hook for registering custom header types of their own.

Whenever you work with any policy object descended from [`EmailPolicy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy), every header is built by `HeaderRegistry` and carries `BaseHeader` as its final base class. On top of that, each header class gains a further base class chosen according to the header’s type. Numerous headers, for instance, take `UnstructuredHeader` as that second base class. The specialized second class assigned to a header is decided from the header’s name through a lookup table held inside the `HeaderRegistry`. The ordinary application program never sees any of this machinery, though interfaces do exist so that more elaborate applications can adjust the default behavior.

The sections that follow begin by covering the header base classes alongside their attributes, then move on to the API for altering how `HeaderRegistry` behaves, and close with the support classes that model the data extracted from structured headers.

 *class *email.headerregistry.BaseHeader(*name*, *value*)

The [`header_factory`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.header_factory) call hands *name* and *value* onward to `BaseHeader`. Whatever string a header object evaluates to is the *value* decoded in full to unicode.

The read-only properties declared by this base class are:

[Subject index](INDEX.md) · [Continue](email-headerregistry-baseheader-fold.md)

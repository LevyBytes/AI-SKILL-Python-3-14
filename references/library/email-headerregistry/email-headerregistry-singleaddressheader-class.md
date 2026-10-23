# email.headerregistry`email.headerregistry`: Custom Header Objects

*class *email.headerregistry.SingleAddressHeader

A subclass of `AddressHeader` that tacks on one further attribute:

 address

The lone address that the header value encodes. Should the header value in fact carry more than a single address (which under the default [`policy`](https://docs.python.org/3.14/library/email.policy.html#module-email.policy) would break the RFC), reading this attribute yields a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

A good many of the classes above come in a `Unique` flavor too (`UniqueUnstructuredHeader`, say). The sole distinction is that the `Unique` flavor sets `max_count` to 1.

[Subject index](INDEX.md) · [Previous](email-headerregistry-addressheader-class.md) · [Continue](email-headerregistry-mimeversionheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

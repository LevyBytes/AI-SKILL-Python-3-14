# email.headerregistry — `email.headerregistry`: Custom Header Objects

*class *email.headerregistry.AddressHeader

Among structured header types, address headers rank among the most intricate. The `AddressHeader` class offers a generic interface onto any address header.

The extra attributes this header type adds are:

 groups

A tuple of `Group` objects that encode the addresses and groups present in the header value. Any address standing outside a group shows up in this list as a single-address `Groups` whose `display_name` is `None`.

 addresses

A tuple of `Address` objects that encode every individual address taken from the header value. Where the header value holds groups, the individual addresses belonging to a group are placed into the list at the spot where that group sits in the value (meaning the address list is “flattened” down to a one dimensional list).

In the header’s `decoded` value, all encoded words have been decoded to unicode. [`idna`](https://docs.python.org/3.14/library/codecs.html#module-encodings.idna) encoded domain names are likewise decoded to unicode. The `decoded` value is produced by [joining](https://docs.python.org/3.14/library/stdtypes.html#meth-str-join) the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) values of the items in the `groups` attribute using `', '`.

To set the value of an address header you may pass a list mixing `Address` and `Group` objects however you like. `Group` objects with a `display_name` of `None` are read as single addresses, which lets you copy an address list with its groups preserved by reusing the list taken from the source header’s `groups` attribute.

[Subject index](INDEX.md) · [Previous](email-headerregistry-dateheader-class.md) · [Continue](email-headerregistry-singleaddressheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

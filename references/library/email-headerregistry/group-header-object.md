# email.headerregistry — `email.headerregistry`: Custom Header Objects

*class *email.headerregistry.Group(*display_name=None*, *addresses=None*)

The class that models an address group. An address group generally takes the form:

```python
display_name: [address-list];

```

To make handling address lists that blend groups and lone addresses easier, a `Group` can additionally stand for single addresses outside any group: set *display_name* to `None` and supply a list holding just that one address as *addresses*.

 display_name

The group’s `display_name`. When it is `None` and `addresses` holds exactly one `Address`, the `Group` stands for a single address that belongs to no group.

 addresses

A possibly empty tuple of `Address` objects standing for the addresses within the group.

 __str__()

A `Group`’s `str` value is formatted per [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html), yet without any Content Transfer Encoding applied to non-ASCII characters. When `display_name` is none and the `addresses` list holds a single `Address`, the `str` value matches the `str` of that one `Address`.

Footnotes

[Subject index](INDEX.md) · [Previous](address-header-object.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

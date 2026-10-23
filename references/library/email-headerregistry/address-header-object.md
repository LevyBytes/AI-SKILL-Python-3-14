# email.headerregistry`email.headerregistry`: Custom Header Objects

*class *email.headerregistry.Address(*display_name=''*, *username=''*, *domain=''*, *addr_spec=None*)

The class that models an email address. An address generally takes the form:

```python
[display_name] <username@domain>

```

or:

```python
username@domain

```

in which every part has to satisfy particular syntax rules that [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) sets out.

For convenience, *addr_spec* may be given in place of *username* and *domain*, and when it is, *username* and *domain* get parsed out of the *addr_spec*. An *addr_spec* has to be a string quoted correctly per the RFC; otherwise `Address` throws an error. Unicode characters are permitted and get properly encoded on serialization. That said, the RFCs forbid unicode within the username portion of the address.

 display_name

The address’s display name portion, where present, stripped of all quoting. When the address carries no display name, this attribute comes out as an empty string.

 username

The address’s `username` portion, stripped of all quoting.

 domain

The address’s `domain` portion.

 addr_spec

The address’s `username@domain` portion, quoted properly so it works as a bare address (the second form depicted above). You cannot mutate this attribute.

 __str__()

The object’s `str` value is the address quoted by the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) rules, yet without any Content Transfer Encoding applied to non-ASCII characters.

So that SMTP ([**RFC 5321**](https://datatracker.ietf.org/doc/html/rfc5321.html)) is supported, `Address` covers one special case: when `username` and `domain` are each the empty string (or `None`), the string value of the `Address` becomes `<>`.

[Subject index](INDEX.md) · [Previous](header-registry-type-mapping-and-construction.md) · [Continue](group-header-object.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

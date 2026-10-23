# email.headerregistry`email.headerregistry`: Custom Header Objects

*class *email.headerregistry.MIMEVersionHeader

Truly just one valid value exists for the *MIME-Version* header, namely `1.0`. As a hedge against the future, this header class accommodates other valid version numbers. When a version number holds a value valid per [**RFC 2045**](https://datatracker.ietf.org/doc/html/rfc2045.html), the header object carries non-`None` values for these attributes:

 version

The version number rendered as a string, stripped of any whitespace and/or comments.

 major

The major version number given as an integer

 minor

The minor version number given as an integer

[Subject index](INDEX.md) · [Previous](email-headerregistry-singleaddressheader-class.md) · [Continue](email-headerregistry-parameterizedmimeheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

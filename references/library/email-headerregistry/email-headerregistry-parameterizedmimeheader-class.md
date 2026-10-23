# email.headerregistry`email.headerregistry`: Custom Header Objects

*class *email.headerregistry.ParameterizedMIMEHeader

Every MIME header opens with the ‘Content-’ prefix. A given header has a particular value, covered under that header’s class. Some are also able to accept a list of extra parameters that share a common format. This class acts as the base for all the MIME headers that accept parameters.

 params

A dictionary that maps parameter names onto parameter values.

[Subject index](INDEX.md) · [Previous](email-headerregistry-mimeversionheader-class.md) · [Continue](email-headerregistry-contenttypeheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

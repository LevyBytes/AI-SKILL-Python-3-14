# email.headerregistry — `email.headerregistry`: Custom Header Objects

*class *email.headerregistry.HeaderRegistry(*base_class=BaseHeader*, *default_class=UnstructuredHeader*, *use_default_map=True*)

This is the factory that [`EmailPolicy`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy) employs by default. `HeaderRegistry` assembles the class used to create a header instance on the fly, drawing on *base_class* together with a specialized class pulled from a registry it maintains. Whenever a particular header name is absent from the registry, the class named by *default_class* serves as the specialized class. Whenever *use_default_map* is `True` (its default), the registry receives a copy of the standard header-name-to-class mapping at initialization time. *base_class* is invariably the final class in the generated class’s [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) list.

The default mappings come out as:

>

subject:

UniqueUnstructuredHeader

date:

UniqueDateHeader

resent-date:

DateHeader

orig-date:

UniqueDateHeader

sender:

UniqueSingleAddressHeader

resent-sender:

SingleAddressHeader

to:

UniqueAddressHeader

resent-to:

AddressHeader

cc:

UniqueAddressHeader

resent-cc:

AddressHeader

bcc:

UniqueAddressHeader

resent-bcc:

AddressHeader

from:

UniqueAddressHeader

resent-from:

AddressHeader

reply-to:

UniqueAddressHeader

mime-version:

MIMEVersionHeader

content-type:

ContentTypeHeader

content-disposition:

ContentDispositionHeader

content-transfer-encoding:

ContentTransferEncodingHeader

message-id:

MessageIDHeader

`HeaderRegistry` exposes these methods:

[Subject index](INDEX.md) · [Previous](email-headerregistry-contenttransferencodingheader-class.md) · [Continue](header-registry-type-mapping-and-construction.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md)

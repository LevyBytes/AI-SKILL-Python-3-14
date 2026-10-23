# email.headerregistry`email.headerregistry`: Custom Header Objects

map_to_type(*self*, *name*, *cls*)

*name* identifies the header being mapped. The registry stores it folded to lower case. *cls* is the specialized class that, paired with *base_class*, builds the class used to instantiate headers matching *name*.

 __getitem__(*name*)

Build and hand back a class suited to creating a *name* header.

 __call__(*name*, *value*)

Fetches the specialized header tied to *name* from the registry (falling back to *default_class* when *name* is missing from the registry), combines it with *base_class* to form a class, invokes that constructed class’s constructor while forwarding the identical argument list, and at last returns the class instance thus produced.

The classes listed next are the ones used to model data parsed out of structured headers; broadly speaking, an application program can use them to assemble structured values for assignment to particular headers.

[Subject index](INDEX.md) · [Previous](email-headerregistry-headerregistry-class.md) · [Continue](address-header-object.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md) · [Owning module, declaration or section: email.headerregistry.HeaderRegistry](email-headerregistry-headerregistry-class.md)

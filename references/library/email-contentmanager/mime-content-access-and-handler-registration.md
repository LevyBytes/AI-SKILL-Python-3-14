# email.contentmanager.ContentManager: `get_content()`, `set_content()`, `add_get_handler()`, `add_set_handler()`

get_content(*msg*, **args*, ***kw*)

Resolve a handler function from the `mimetype` of *msg* (described just below), invoke it while forwarding every argument, and hand back whatever it returns. The handler is assumed to pull the payload out of *msg* and yield an object that captures details about the data it extracted.

The handler is located by consulting these registry keys in turn, halting at the first match:

- the text form of the complete MIME type (`maintype/subtype`)

- the text form of the `maintype` alone

- the empty string

Should none of those keys map to a handler, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised carrying the full MIME type.

 set_content(*msg*, *obj*, **args*, ***kw*)

When the `maintype` equals `multipart`, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised; otherwise a handler function is selected from the type of *obj* (covered in the paragraph that follows), [`clear_content()`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage.clear_content) is invoked on the *msg*, and the handler runs with all arguments forwarded. The handler is presumed to convert *obj* and place it into *msg*, perhaps altering *msg* in further ways too, such as attaching assorted MIME headers that record what is needed to interpret the stored data.

To pick the handler, take the type of *obj* (`typ = type(obj)`) and search these registry keys in sequence, stopping at the first hit:

- the type on its own (`typ`)

- the type’s fully qualified name (`typ.__module__ + '.' + typ.__qualname__`).

- the type’s [`qualname`](https://docs.python.org/3.14/reference/datamodel.html#type.__qualname__) (`typ.__qualname__`)

- the type’s [`name`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) (`typ.__name__`).

When none of those produce a match, run the entire sequence of checks again against every type in the [MRO](https://docs.python.org/3.14/glossary.html#term-MRO) ([`typ.__mro__`](https://docs.python.org/3.14/reference/datamodel.html#type.__mro__)). As a last resort, when no key has yielded a handler, look for one registered under the key `None`. With no handler available for `None`, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised carrying the fully qualified name of the type.

A *MIME-Version* header is also inserted when one is absent (see as well [`MIMEPart`](https://docs.python.org/3.14/library/email.message.html#email.message.MIMEPart)).

 add_get_handler(*key*, *handler*)

Register the function *handler* to serve as the handler bound to *key*. The allowable values of *key* are described under `get_content()`.

 add_set_handler(*typekey*, *handler*)

Register *handler* as the function invoked whenever an object whose type matches *typekey* is handed to `set_content()`. The allowable values of *typekey* are described under `set_content()`.

[Subject index](INDEX.md) · [Previous](email-contentmanager-contentmanager-class.md) · [Continue](raw-mime-content-manager.md) · [Owning module, declaration or section: email.contentmanager](email-contentmanager-contentmanager-class.md) · [Owning module, declaration or section: email.contentmanager.ContentManager](email-contentmanager-contentmanager-class.md)

# wsgiref.headers.Headers: `get_all()`, `add_header()`

get_all(*name*)

Hand back a list of every value belonging to the named header.

The list returned keeps the order in which the values surfaced in the original header list or were appended to this instance, and it may hold duplicates. Fields that were deleted and re-inserted always land at the end of the header list. When no fields carry the supplied name, an empty list is returned.

 add_header(*name*, *value*, ***_params*)

Append a header (which may be multi-valued), with optional MIME parameters given through keyword arguments.

*name* identifies the header field being added. MIME parameters for the header field can be set via keyword arguments. Every parameter has to be a string or `None`. Because dashes can’t appear in Python identifiers yet many MIME parameter names contain dashes, underscores in parameter names get turned into dashes. A string parameter value is appended to the header value parameters as `name="value"`. A value of `None` causes only the parameter name to be appended. (That covers MIME parameters that lack a value.) Example usage:

```python
h.add_header('content-disposition', 'attachment', filename='bud.gif')

```

That call appends a header resembling the following:

```python
Content-Disposition: attachment; filename="bud.gif"

```

Changed in version 3.5: *headers* parameter is optional.

[Subject index](INDEX.md) · [Previous](wsgiref-headers-headers-class.md) · [Continue](../wsgiref-simple-server/wsgi-server-factory-and-demo-application.md) · [Owning module, declaration or section: wsgiref.headers](wsgiref-headers-headers-class.md) · [Owning module, declaration or section: wsgiref.headers.Headers](wsgiref-headers-headers-class.md)

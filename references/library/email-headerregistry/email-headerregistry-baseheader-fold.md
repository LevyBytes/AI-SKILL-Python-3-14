# email.headerregistry`email.headerregistry`: Custom Header Objects

name

The header’s name (everything in the field ahead of the ‘:’). It matches precisely what was handed to the [`header_factory`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.header_factory) call as *name*, so the original case stays intact.

 defects

A tuple of [`HeaderDefect`](https://docs.python.org/3.14/library/email.errors.html#email.errors.HeaderDefect) instances that flag any RFC compliance trouble noticed while parsing. The email package aims to catch compliance issues thoroughly. The [`errors`](https://docs.python.org/3.14/library/email.errors.html#module-email.errors) module goes over the kinds of defects that might be reported.

 max_count

The greatest count of headers of this kind permitted to share the same `name`. Setting it to `None` signifies no limit. On `BaseHeader` this attribute holds `None`; specialized header classes are anticipated to replace that value where appropriate.

`BaseHeader` further exposes the method below, which the email library code invokes and which application programs ordinarily should not call:

 fold(***, *policy*)

Hand back a string holding [`linesep`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.linesep) characters wherever they are needed to fold the header properly per *policy*. A [`cte_type`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.cte_type) of `8bit` is handled as though it were `7bit`, because headers cannot carry arbitrary binary data. Should [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) be `False`, non-ASCII data gets [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoded.

On its own, `BaseHeader` cannot build a header object. What it lays down is a protocol that every specialized header collaborates with to produce the header object. In particular, `BaseHeader` insists that the specialized class supply a [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) named `parse`. The call takes this shape:

```python
parse(string, kwds)

```

`kwds` is a dictionary that arrives with a single pre-set key, `defects`. That `defects` entry starts as an empty list. The parse method ought to add any defects it spots to this list. By the time it returns, the `kwds` dictionary *must* hold values for at minimum the keys `decoded`, `defects` and `parse_tree`. `decoded` ought to be the header’s string value (meaning the header value decoded fully to unicode). `parse_tree` receives the parse tree produced from parsing the header. The parse method ought to expect that *string* might hold content-transfer-encoded parts, yet it must also deal properly with every valid unicode character so that it can handle un-encoded header values.

Following that, `BaseHeader`’s `__new__` constructs the header instance and runs its `init` method. A specialized class needs to furnish an `init` method only when it wants to set attributes beyond the ones `BaseHeader` already supplies. An `init` method of that sort ought to resemble this:

```python
def init(self, /, *args, **kw):
    self._myattr = kw.pop('myattr')
    super().init(*args, **kw)

```

In other words, whatever extras the specialized class deposited into the `kwds` dictionary ought to be pulled out and dealt with, while what is left in `kw` (and `args`) is forwarded to the `BaseHeader` `init` method.

[Subject index](INDEX.md) · [Previous](email-headerregistry-baseheader-class.md) · [Continue](email-headerregistry-unstructuredheader-class.md) · [Owning module, declaration or section: email.headerregistry](email-headerregistry-baseheader-class.md) · [Owning module, declaration or section: email.headerregistry.BaseHeader](email-headerregistry-baseheader-class.md)

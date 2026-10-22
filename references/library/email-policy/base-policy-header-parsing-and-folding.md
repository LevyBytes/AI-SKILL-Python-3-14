# email.policy.Policy: `header_source_parse()`, `header_store_parse()`, `header_fetch_parse()`, `fold()`, `fold_binary()`

header_source_parse(*sourcelines*)

The email package invokes this method with a list of strings, every string ending in the line separation characters present in the source under parsing. The opening line carries the field header name plus the separator. Every bit of whitespace in the source is kept. The method ought to hand back the `(name, value)` tuple meant to be stored in the `Message` to stand for the parsed header.

Where an implementation wants to stay compatible with the email package’s existing policies, *name* should be the case preserved name (every character up to the ‘`:`’ separator), whereas *value* should be the unfolded value (with all line separator characters dropped, but whitespace left intact), trimmed of leading whitespace.

*sourcelines* may hold surrogateescaped binary data.

There is no default implementation

 header_store_parse(*name*, *value*)

The email package invokes this method using the name and value handed in by the application program when that program is altering a `Message` programmatically (rather than a `Message` produced by a parser). The method ought to hand back the `(name, value)` tuple meant to be stored in the `Message` to stand for the header.

Where an implementation wants to stay compatible with the email package’s existing policies, both the *name* and the *value* should be strings or string subclasses that leave the content of the passed in arguments untouched.

There is no default implementation

 header_fetch_parse(*name*, *value*)

The email package invokes this method using the *name* and *value* presently held in the `Message` when the application program requests that header, and whatever the method returns is what gets handed back to the application as the value of the header being fetched. Bear in mind there may be more than one header bearing the same name stored within the `Message`; the method receives the particular name and value of the header bound to be returned to the application.

*value* may hold surrogateescaped binary data. The value the method returns should contain no surrogateescaped binary data.

There is no default implementation

 fold(*name*, *value*)

The email package invokes this method using the *name* and *value* presently held in the `Message` for a given header. The method ought to hand back a string that renders that header “folded” properly (per the policy settings), assembling the *name* together with the *value* and inserting `linesep` characters where appropriate. Consult [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) for a treatment of the rules covering the folding of email headers.

*value* may hold surrogateescaped binary data. The string the method returns should contain no surrogateescaped binary data.

 fold_binary(*name*, *value*)

Identical to `fold()`, except that the value returned should be a bytes object instead of a string.

*value* may hold surrogateescaped binary data. That data may be turned back into binary data within the returned bytes object.

[Subject index](INDEX.md) · [Previous](base-policy-settings-and-header-limits.md) · [Continue](email-policy-class-and-header-folding.md) · [Owning module, declaration or section: email.policy](email-policy-policy-objects.md) · [Owning module, declaration or section: email.policy.Policy](base-policy-settings-and-header-limits.md)

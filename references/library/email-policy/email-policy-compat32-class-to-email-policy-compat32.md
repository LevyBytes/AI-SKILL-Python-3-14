# email.policy.EmailPolicy header behavior and Compat32

Seen from the application side, what this amounts to is that every header you pull from an [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) comes back as a header object carrying additional attributes, where its string form is the header's fully decoded unicode text. In the same way, you can set a header to a fresh value, or build a brand-new header, by supplying a unicode string, and the policy handles turning that unicode string into the proper RFC encoded representation.

Documentation of these header objects, along with the attributes they carry, lives in [`headerregistry`](https://docs.python.org/3.14/library/email.headerregistry.html#module-email.headerregistry).

 *class *email.policy.Compat32(***kw*)

This is the concrete `Policy` that supplies backward compatibility. Its behavior mirrors how the email package acted in Python 3.2. Within the `policy` module there is also a ready-made instance of this class named `compat32`, which serves as the default policy. As a result, out of the box the email package keeps things compatible with Python 3.2.

For the attributes listed below, the values diverge from what the `Policy` default sets:

 mangle_from_

The default is `True`.

Below are the concrete versions this class supplies for the abstract methods declared on `Policy`:

 header_source_parse(*sourcelines*)

Everything preceding the ‘`:`’ is read off as the name and handed back untouched. To work out the value, leading whitespace is trimmed from what remains of the first line, every line after that is concatenated, and any carriage-return or linefeed characters at the end are removed.

 header_store_parse(*name*, *value*)

Both the name and the value come back exactly as supplied.

 header_fetch_parse(*name*, *value*)

Should the value hold binary data, it gets turned into a [`Header`](https://docs.python.org/3.14/library/email.header.html#email.header.Header) object via the `unknown-8bit` charset. If not, it passes straight through unchanged.

 fold(*name*, *value*)

Folding of headers relies on the [`Header`](https://docs.python.org/3.14/library/email.header.html#email.header.Header) folding algorithm; it keeps whatever line breaks already sit in the value and caps every produced line at `max_line_length`. Any non-ASCII binary data gets CTE encoded with the `unknown-8bit` charset.

 fold_binary(*name*, *value*)

Here too the [`Header`](https://docs.python.org/3.14/library/email.header.html#email.header.Header) folding algorithm does the folding, retaining the line breaks already present in the value and limiting each output line to `max_line_length`. When `cte_type` equals `7bit`, non-ascii binary data is CTE encoded through the `unknown-8bit` charset. If it is not, the header from the original source is kept as-is, complete with its current line breaks and whatever (RFC invalid) binary data it might carry.

 email.policy.compat32

A `Compat32` instance that delivers backward compatibility, matching how the email package behaved back in Python 3.2.

Note

Avoid applying the `compat32` policy to [`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage) objects; reserve it solely for serializing messages that were themselves built under the `compat32` policy.

Footnotes

[Subject index](INDEX.md) · [Owning API and preceding source contract](email-policy-class-and-header-folding.md) · [Owning API and preceding source contract](email-policy-default-to-email-policy-strict.md) · [Preceding source contract and version conditions](email-policy-default-to-email-policy-strict.md)

# netrc - netrc Objects

### netrc Objects

A `netrc` instance has the following methods:

 netrc.authenticators(*host*)

Hand back the authenticators for *host* as a 3-tuple `(login, account, password)`. Where the netrc file held no record for that host, the tuple tied to the ‘default’ record is given instead. Lacking both a host match and a default record, `None` is returned.

 netrc.__repr__()

Emit the class's data as a string laid out like a netrc file. (Comments get dropped along the way, and the ordering of entries may shift.)

Instances of `netrc` have public instance variables:

 netrc.hosts

A dictionary keying host names to their `(login, account, password)` tuples. Should a ‘default’ entry exist, it appears under a pseudo-host carrying that name.

 netrc.macros

A dictionary that keys macro names to lists of strings.

[Subject index](INDEX.md) · [Previous](netrc-netrc-class-to-netrc-netrcparseerror.md) · [Continue](../nis/nis-interface-to-sun-s-nis-yellow-pages.md) · [Owning module, declaration or section: netrc](netrc-netrc-class-to-netrc-netrcparseerror.md)

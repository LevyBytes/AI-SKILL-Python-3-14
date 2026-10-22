# uuid: `uuid.RESERVED_MICROSOFT`, `uuid.RESERVED_FUTURE`, `uuid.NIL`, `uuid.MAX`

uuid.RESERVED_MICROSOFT

Reserved for Microsoft compatibility.

 uuid.RESERVED_FUTURE

Reserved for future definition.

The special Nil and Max UUID values are defined by the `uuid` module as follows:

 uuid.NIL

A distinctive form of UUID whose 128 bits are all specified to be zero, in keeping with [**RFC 9562,5.9**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.9).

Added in version 3.14.

 uuid.MAX

A distinctive form of UUID whose 128 bits are all specified to be one, in keeping with [**RFC 9562,5.10**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.10).

Added in version 3.14.

See also

[**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html) - A Universally Unique IDentifier (UUID) URN Namespace

This specification lays out a Uniform Resource Name namespace for UUIDs, spells out the internal format of UUIDs, and describes ways of generating them.

[Subject index](INDEX.md) · [Previous](uuid-getnode-to-uuid-rfc-4122.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: uuid](uuid-safeuuid-class.md)

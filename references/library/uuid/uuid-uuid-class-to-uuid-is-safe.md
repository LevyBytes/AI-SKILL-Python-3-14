# uuid: `uuid.UUID`, `UUID.bytes`, `UUID.bytes_le`, `UUID.fields`, `UUID.hex`, `UUID.int`, `UUID.urn`, `UUID.variant`, `UUID.version`, `UUID.is_safe`

`*class *uuid.UUID(*hex=None*, *bytes=None*, *bytes_le=None*, *fields=None*, *int=None*, *version=None*, ***, *is_safe=SafeUUID.unknown*)`

Builds a UUID from any of: a string of 32 hexadecimal digits; a 16-byte string in big-endian order passed as the *bytes* argument; a 16-byte string in little-endian order passed as the *bytes_le* argument; a tuple of six integers (32-bit *time_low*, 16-bit *time_mid*, 16-bit *time_hi_version*, 8-bit *clock_seq_hi_variant*, 8-bit *clock_seq_low*, 48-bit *node*) passed as the *fields* argument; or one 128-bit integer passed as the *int* argument. Where a string of hex digits is supplied, curly braces, hyphens, and a URN prefix may each be left out. To illustrate, the expressions below all produce the very same UUID:

```python
UUID('{12345678-1234-5678-1234-567812345678}')
UUID('12345678123456781234567812345678')
UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
UUID(bytes=b'\x12\x34\x56\x78'*4)
UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
              b'\x12\x34\x56\x78\x12\x34\x56\x78')
UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
UUID(int=0x12345678123456781234567812345678)

```

Precisely one of *hex*, *bytes*, *bytes_le*, *fields*, or *int* has to be supplied. The *version* argument is optional; when present, it sets the resulting UUID's variant and version number per [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html), overriding bits within the given *hex*, *bytes*, *bytes_le*, *fields*, or *int*.

UUID objects get compared through their `UUID.int` attributes. Comparing one against a non-UUID object brings about a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

`str(uuid)` hands back a string shaped as `12345678-1234-5678-1234-567812345678`, whose 32 hexadecimal digits stand for the UUID.

The read-only attributes carried by `UUID` instances are these:

 UUID.bytes

The UUID rendered as a 16-byte string (holding the six integer fields in big-endian byte order).

 UUID.bytes_le

The UUID rendered as a 16-byte string (with *time_low*, *time_mid*, and *time_hi_version* held in little-endian byte order).

 UUID.fields

A tuple gathering the UUID's six integer fields, which are likewise reachable as six separate attributes plus two derived ones:

| Field | Meaning |
| --- | --- |
| UUID.time_low | The UUID's leading 32 bits. Bears on version 1 alone. |
| UUID.time_mid | The 16 bits that follow in the UUID. Applies to version 1 only. |
| UUID.time_hi_version | The subsequent 16 bits of the UUID. Meaningful for version 1 alone. |
| UUID.clock_seq_hi_variant | The next 8 bits within the UUID. Pertinent to versions 1 and 6 only. |
| UUID.clock_seq_low | The following 8 bits of the UUID. Relevant solely to versions 1 and 6. |
| UUID.node | The UUID's final 48 bits. Tied to version 1 alone. |
| UUID.time | The 60-bit timestamp expressed as a tally of 100-nanosecond intervals reckoned from the Gregorian epoch (1582-10-15 00:00:00) for versions 1 and 6, or the 48-bit timestamp in milliseconds reckoned from the Unix epoch (1970-01-01 00:00:00) for version 7. |
| UUID.clock_seq | The 14-bit sequence number. Concerns versions 1 and 6 only. |

 UUID.hex

The UUID as a 32-character lowercase hexadecimal string.

 UUID.int

The UUID as a 128-bit integer.

 UUID.urn

The UUID as a URN as specified in [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html).

 UUID.variant

The UUID variant, the thing that dictates the UUID's internal layout. It takes one of the constants `RESERVED_NCS`, `RFC_4122`, `RESERVED_MICROSOFT`, or `RESERVED_FUTURE`.

 UUID.version

The UUID version number (running 1 through 8, and meaningful solely where the variant is `RFC_4122`).

Changed in version 3.14: Added UUID versions 6, 7 and 8.

 UUID.is_safe

A `SafeUUID` enumeration value reporting whether the platform produced the UUID in a multiprocessing-safe manner.

Added in version 3.7.

These are the functions the `uuid` module defines:

[Subject index](INDEX.md) · [Previous](uuid-uuid-objects-according-to-rfc-9562.md) · [Continue](uuid-getnode-to-uuid-rfc-4122.md) · [Owning module, declaration or section: uuid](uuid-safeuuid-class.md)

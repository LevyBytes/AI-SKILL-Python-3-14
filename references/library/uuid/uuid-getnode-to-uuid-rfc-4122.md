# uuid: UUID generation, namespace and variant selection

uuid.getnode()

Fetches the hardware address as a 48-bit positive integer. On its very first run it may fire up a separate program, which can be rather slow. Should every attempt to obtain the hardware address come up empty, a random 48-bit number is picked with the multicast bit (the least significant bit of the first octet) set to 1, in keeping with the recommendation in [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html). By "hardware address" we mean a network interface's MAC address. On a machine sporting several network interfaces, universally administered MAC addresses (those where the second least significant bit of the first octet is *unset*) get the nod over locally administered ones, though no further ordering is promised.

Changed in version 3.7: Universally administered MAC addresses take priority over locally administered ones, the former carrying a guarantee of global uniqueness that the latter lack.

 uuid.uuid1(*node=None*, *clock_seq=None*)

Produces a UUID out of a host ID, a sequence number, and the current time, following [**RFC 9562,5.1**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.1).

Where *node* goes unspecified, `getnode()` serves to fetch the hardware address as a 48-bit positive integer. Where a sequence number *clock_seq* goes unspecified, a pseudo-random 14-bit positive integer is produced.

Should *node* or *clock_seq* run past their allotted bit count, only their least significant bits are retained.

 uuid.uuid3(*namespace*, *name*)

Produces a UUID drawn from the MD5 hash of a namespace identifier (itself a UUID) together with a name (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, or a string slated for UTF-8 encoding), in line with [**RFC 9562,5.3**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.3).

 uuid.uuid4()

Produces a random UUID by a cryptographically-secure method, following [**RFC 9562,5.4**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.4).

 uuid.uuid5(*namespace*, *name*)

Produces a UUID drawn from the SHA-1 hash of a namespace identifier (itself a UUID) together with a name (a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, or a string slated for UTF-8 encoding), in line with [**RFC 9562,5.5**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.5).

 uuid.uuid6(*node=None*, *clock_seq=None*)

Produces a UUID out of a sequence number and the current time, following [**RFC 9562,5.6**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.6).

It stands as an alternative to `uuid1()` that betters database locality.

When *node* is left out, the hardware address is fetched via `getnode()` as a 48-bit positive integer. When the sequence number *clock_seq* is left out, a pseudo-random 14-bit positive integer gets created.

If either *node* or *clock_seq* overshoots its allotted bit count, only the least significant bits survive.

Added in version 3.14.

 uuid.uuid7()

Produces a time-based UUID, following [**RFC 9562,5.7**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.7).

So as to stay portable across platforms without sub-millisecond precision, the UUIDs this function turns out carry a 48-bit timestamp and lean on a 42-bit counter to keep monotonicity intact inside any one millisecond.

Added in version 3.14.

 uuid.uuid8(*a=None*, *b=None*, *c=None*)

Produces a pseudo-random UUID, following [**RFC 9562,5.8**](https://datatracker.ietf.org/doc/html/rfc9562.html#section-5.8).

When given, the parameters *a*, *b* and *c* are taken to be positive integers of 48, 12 and 62 bits in turn. Run past their allotted bit count and only their least significant bits stay; any argument left out is replaced by a pseudo-random integer of suitable size.

Out of the box, *a*, *b* and *c* don't come from a cryptographically secure pseudo-random number generator (CSPRNG). Reach for `uuid4()` whenever a UUID has to serve in a security-sensitive setting.

Added in version 3.14.

For use alongside `uuid3()` or `uuid5()`, the `uuid` module defines these namespace identifiers.

 uuid.NAMESPACE_DNS

Pick this namespace and the *name* string stands for a fully qualified domain name.

 uuid.NAMESPACE_URL

Pick this namespace and the *name* string stands for a URL.

 uuid.NAMESPACE_OID

Pick this namespace and the *name* string stands for an ISO OID.

 uuid.NAMESPACE_X500

Pick this namespace and the *name* string stands for an X.500 DN in DER or a text output format.

For the possible values of the `variant` attribute, the `uuid` module defines these constants:

 uuid.RESERVED_NCS

Reserved for NCS compatibility.

 uuid.RFC_4122

Denotes the UUID layout set out in [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html). This constant lingers for backward compatibility, even though [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html) has since been superseded by [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html).

[Subject index](INDEX.md) · [Previous](uuid-uuid-class-to-uuid-is-safe.md) · [Continue](uuid-reserved-microsoft-to-uuid-max.md) · [Owning module, declaration or section: uuid](uuid-safeuuid-class.md)

# uuid: `uuid.SafeUUID`

## uuid - UUID objects according to RFC 9562

### `uuid` - UUID objects according to [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html)

**Source code:** [Lib/uuid.py](https://github.com/python/cpython/tree/3.14/Lib/uuid.py)

---

What this module gives you is immutable `UUID` objects (the `UUID` class) along with functions that produce UUIDs matching a particular UUID version as laid down in [**RFC 9562**](https://datatracker.ietf.org/doc/html/rfc9562.html) (which takes over from [**RFC 4122**](https://datatracker.ietf.org/doc/html/rfc4122.html)) — for instance, `uuid1()` for UUID version 1, `uuid3()` for UUID version 3, and onward. Bear in mind that UUID version 2 is left out on purpose, falling outside the RFC's scope.

When a unique ID is all you're after, calling `uuid1()` or `uuid4()` is likely your best bet. Be aware that `uuid1()` can erode privacy, given that the UUID it builds carries the computer's network address. A random UUID comes from `uuid4()`.

According to what the underlying platform supports, `uuid1()` might or might not give back a "safe" UUID. A safe UUID is one produced through synchronization methods that keep any two processes from landing on the same UUID. Every `UUID` instance carries an `is_safe` attribute that conveys whatever is known about the UUID's safety, by way of this enumeration:

 *class *uuid.SafeUUID

Added in version 3.7.

[Subject index](INDEX.md) · [Continue](uuid-uuid-objects-according-to-rfc-9562.md)

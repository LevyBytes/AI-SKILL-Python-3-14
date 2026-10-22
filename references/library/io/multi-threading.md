# io — Multi-threading

### Multi-threading

`FileIO` objects are thread-safe to whatever degree the operating system calls they wrap (such as *[read(2)](https://manpages.debian.org/read(2))* under Unix) are themselves thread-safe.

Binary buffered objects (instances of `BufferedReader`, `BufferedWriter`, `BufferedRandom` and `BufferedRWPair`) guard their internal structures with a lock; calling them concurrently from several threads is therefore safe.

`TextIOWrapper` objects are not thread-safe.

[Subject index](INDEX.md) · [Previous](text-i-o.md) · [Continue](reentrancy.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)

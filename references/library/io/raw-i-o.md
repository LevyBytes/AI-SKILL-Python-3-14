# io — Raw I/O

### Raw I/O

Raw I/O (which also goes by *unbuffered I/O*) typically serves as a low-level component underneath binary and text streams; directly handling a raw stream from your own code is seldom worthwhile. Even so, you can produce a raw stream by opening a file in binary mode and turning buffering off:

```python
f = open("myfile.jpg", "rb", buffering=0)

```

Full coverage of the raw stream API appears in the docs of `RawIOBase`.

Warning

Being a low-level interface, raw I/O generally requires you to inspect the return values from its methods and retry explicitly so that an operation runs to completion. As an example, `write()` hands back the count of bytes written, which can fall short of the count of bytes supplied (a partial write). Higher-level I/O objects such as Binary I/O and Text I/O take care of retrying for you.

[Subject index](INDEX.md) · [Previous](binary-i-o.md) · [Continue](text-encoding.md) · [Owning module, declaration or section: io](io-core-tools-for-working-with-streams.md)

# Platform Considerations

### Platform Considerations

ABI stability rests not on Python alone but also on the compiler in use, the lower-level libraries, and the compiler options. For Stable ABI purposes, those details constitute a “platform”. They generally come down to the OS type and the processor architecture

Making sure every Python version on a given platform is built so the Stable ABI stays intact rests with each individual distributor of Python. That holds for the Windows and macOS releases from `python.org` and from many third-party distributors.

[Subject index](INDEX.md) · [Previous source contract](limited-api-caveats.md) · [Following source contract](INDEX.md)

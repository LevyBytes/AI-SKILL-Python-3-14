# Create Config

### Create Config

 struct PyInitConfig

An opaque type that holds the settings driving Python initialization.

 PyInitConfig *PyInitConfig_Create(void)

Build a fresh initialization configuration seeded with the Isolated Configuration defaults.

Releasing it is done through `PyInitConfig_Free()`.

When memory allocation fails, `NULL` comes back.

 void PyInitConfig_Free(PyInitConfig *config)

Release the memory held by the *config* initialization configuration.

When *config* is `NULL`, nothing happens.

[Subject index](INDEX.md) · [Previous source contract](example.md) · [Following source contract](pyinitconfig-geterror-to-pyinitconfig-getexitcode.md)

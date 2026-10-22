# Module Initialization

### Module Initialization

An extension module has to declare outright that it can operate with the GIL turned off; absent that declaration, importing it triggers a warning and switches the GIL back on while the program runs.

A module can announce GIL-free compatibility through one of two mechanisms, and which one applies hinges on whether it relies on multi-phase or single-phase initialization.

[Subject index](INDEX.md) · [Previous source context](identifying-the-free-threaded-build-in-c.md) · [Following source context](multi-phase-initialization.md)

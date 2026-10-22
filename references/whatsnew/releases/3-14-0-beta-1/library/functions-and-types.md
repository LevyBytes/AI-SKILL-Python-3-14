# Python 3.14.0 beta 1 / library / functions and types

[gh-129965](https://github.com/python/cpython/issues/129965): Register MIME types covering `.7z`, `.apk`, `.deb`, `.glb`, `.gltf`, `.gz`, `.m4v`, `.php`, `.rar`, `.rpm`, `.stl` and `.wmv`. Patch by Hugo van Kemenade.

[gh-132451](https://github.com/python/cpython/issues/132451): The CLI for the PDB debugger will now take a `-p PID` argument so you can attach to a process already running. That process has to be executing the identical Python version as the one PDB itself runs on.

[gh-120220](https://github.com/python/cpython/issues/120220): The `trace_variable()`, `trace_vdelete()` and `trace_vinfo()` methods of `tkinter.Variable` are now deprecated. Reach for `trace_add()`, `trace_remove()` and `trace_info()` in their place.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

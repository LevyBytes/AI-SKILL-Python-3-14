# 7.1.4. Binary extension modules

### 7.1.4. Binary extension modules

A distinguishing trait of iOS is that distribution via the App Store places strict demands on how an application is packaged. Among those demands is one that dictates the way binary extension modules ship.

Per the iOS App Store, *every* binary module within an iOS app has to be a dynamic library wrapped in a framework carrying suitable metadata and placed in the packaged app's `Frameworks` folder. Each framework holds exactly one binary, and no runnable binary content may sit outside the `Frameworks` folder.

That requirement clashes with how Python normally ships binaries, since Python permits a binary extension module to load from anywhere on `sys.path`. So that App Store rules are honored, an iOS project has to post-process each Python package, turning `.so` binary modules into separate self-contained frameworks complete with proper metadata and signing. The guide for adding Python to your project describes how to carry out that post-processing.

So Python can locate the relocated binaries, the initial `.so` file present on `sys.path` gives way to a `.fwork` file. That `.fwork` is a text file recording where the framework binary sits relative to the app bundle. So the framework can map back to its starting point, it must include a `.origin` file holding the `.fwork` file's location relative to the app bundle.

Take, for instance, an import like `from foo.bar import _whiz`, in which `_whiz` comes from the binary module `sources/foo/bar/_whiz.abi3.so`, where `sources` is the entry registered on `sys.path`, relative to the application bundle. That module *must* ship as `Frameworks/foo.bar._whiz.framework/foo.bar._whiz` (the framework name being built from the module's complete import path), accompanied by an `Info.plist` file inside the `.framework` directory that marks the binary as a framework. At its source location, the `foo.bar._whiz` module appears as a `sources/foo/bar/_whiz.abi3.fwork` marker file whose contents are the path `Frameworks/foo.bar._whiz/foo.bar._whiz`. Additionally, the framework carries `Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin`, whose contents are the path back to the `.fwork` file.

While executing on iOS, the Python interpreter sets up an [`AppleFrameworkLoader`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.AppleFrameworkLoader) capable of reading and importing `.fwork` files. After import, the binary module's `__file__` attribute points to where the `.fwork` file lives. Yet the loaded module's [`ModuleSpec`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec) gives the `origin` as the binary's spot inside the framework folder.

[Subject index](INDEX.md) · [Previous source section](standard-library-availability.md) · [Following source section](compiler-stub-binaries.md)

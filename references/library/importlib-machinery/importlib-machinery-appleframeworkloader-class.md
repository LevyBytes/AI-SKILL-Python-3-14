# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.AppleFrameworkLoader(*name*, *path*)

A specialization of `importlib.machinery.ExtensionFileLoader` capable of loading extension modules packaged in Framework format.

To stay compatible with the iOS App Store, *all* binary modules within an iOS app have to be dynamic libraries, each held inside a framework carrying the right metadata and placed in the packaged app's `Frameworks` folder. A framework may hold only one binary, and no executable binary content may sit outside the Frameworks folder.

To satisfy that constraint, on iOS the binaries for extension modules are *not* shipped as `.so` files on `sys.path`; instead each becomes its own standalone framework. So these frameworks can be discovered, the loader is bound to the `.fwork` file extension, where a `.fwork` file stands in at the binary's former location on `sys.path`. Inside the `.fwork` file is the path of the real binary within the `Frameworks` folder, expressed relative to the app bundle. So that a framework-packaged binary can be traced back to where it started, the framework should hold a `.origin` file naming the location of the `.fwork` file, again relative to the app bundle.

Take, for instance, the import `from foo.bar import _whiz`, in which `_whiz` is built from the binary module `sources/foo/bar/_whiz.abi3.so`, where `sources` is the location registered on `sys.path` relative to the application bundle. That module *must* ship as `Frameworks/foo.bar._whiz.framework/foo.bar._whiz` (the framework name being assembled from the module's complete import path), accompanied by an `Info.plist` file inside the `.framework` directory marking the binary as a framework. At its original location the `foo.bar._whiz` module would be stood in for by a `sources/foo/bar/_whiz.abi3.fwork` marker file holding the path `Frameworks/foo.bar._whiz/foo.bar._whiz`. The framework would additionally hold `Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin`, holding the path to the `.fwork` file.

Once a module has been loaded through this loader, the module's `__file__` will report the location of the `.fwork` file. That lets code treat a module's `__file__` as a reference point for walking the file system. The spec origin, however, will point at the location of the *actual* binary inside the `.framework` folder.

It falls to the Xcode project that builds the app to turn any `.so` files, wherever they sit within the `PYTHONPATH`, into frameworks under the `Frameworks` folder (which means trimming the extension off the module file, adding the framework metadata, and signing the produced framework), as well as generating the `.fwork` and `.origin` files. Typically this happens through a build step in the Xcode project; consult the iOS documentation for guidance on assembling that build step.

Added in version 3.13.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): iOS.

 name

Name of the module the loader supports.

 path

Path to the `.fwork` file for the extension module.

[Subject index](INDEX.md) · [Previous](importlib-machinery-modulespec-class.md) · [Continue](../importlib-util/importlib-util-magic-number-to-importlib-util-find-spec.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)

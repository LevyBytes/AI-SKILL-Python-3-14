# 7.1.5. Compiler stub binaries

### 7.1.5. Compiler stub binaries

Rather than surfacing dedicated compilers for iOS, Xcode relies on an `xcrun` script that maps to a complete compiler path (for instance, `xcrun --sdk iphoneos clang` yields the `clang` meant for an iPhone device). Leaning on that script, however, brings two complications:

- What `xcrun` emits carries machine-specific paths, which yields a sysconfig module that can't be shared across users; and

- It produces `CC`/`CPP`/`LD`/`AR` definitions containing spaces. A great deal of C ecosystem tooling presumes a command line can be split at its first space to recover the path to the compiler executable; with `xcrun` that presumption breaks down.

So that these complications are sidestepped, Python supplied stubs standing in for these tools. The stubs are shell-script wrappers around the underlying `xcrun` tools, shipped within a `bin` folder distributed beside the compiled iOS framework. Being relocatable, these scripts will always map to the correct local system paths. Shipping these scripts inside the bin folder that travels with a framework makes the `sysconfig` module's contents genuinely useful when end-users want to compile their own modules. As you build third-party Python modules for iOS, make sure these stub binaries sit on your path.

[Subject index](INDEX.md) · [Previous source section](binary-extension-modules.md) · [Following source section](tools-for-building-ios-apps.md)

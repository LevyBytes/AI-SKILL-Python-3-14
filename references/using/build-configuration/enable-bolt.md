# --enable-bolt

--enable-bolt

Switch on use of the [BOLT post-link binary optimizer](https://github.com/llvm/llvm-project/tree/main/bolt) (off by default).

Although BOLT belongs to the LLVM project, their binary distributions do not always carry it. The flag depends on `llvm-bolt` and `merge-fdata` both being present.

BOLT remains a relatively young project, so for the moment treat this flag as experimental. Since the tool works on machine code, whether it succeeds hinges on the mix of the build environment + the remaining optimization configure args + the CPU architecture, and not every mix is supported. Under certain scenarios, BOLT releases earlier than LLVM 16 are known to crash BOLT. For BOLT optimization, using LLVM 16 or a newer release is strongly encouraged.

You can define the `BOLT_INSTRUMENT_FLAGS` and `BOLT_APPLY_FLAGS` **configure** variables to replace the default argument set handed to **llvm-bolt** for instrumenting binaries and for applying BOLT data to them, respectively.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous source section](with-lto-full-thin-no-yes.md) · [Following source section](bolt-apply-flags.md)

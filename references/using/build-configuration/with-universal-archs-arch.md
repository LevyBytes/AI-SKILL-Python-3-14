# --with-universal-archs=ARCH

--with-universal-archs=ARCH

State which flavor of universal binary to produce. This option only applies once `--enable-universalsdk` has been set.

Options:

- `universal2` (x86-64 and arm64);

- `32-bit` (PPC and i386);

- `64-bit` (PPC64 and x86-64);

- `3-way` (i386, PPC and x86-64);

- `intel` (i386 and x86-64);

- `intel-32` (i386);

- `intel-64` (x86-64);

- `all` (PPC, i386, PPC64 and x86-64).

Be aware that the values for this configuration item are *not* identical to the identifiers attached to universal binary wheels on macOS. Consult the Python Packaging User Guide for the particulars of the [packaging platform compatibility tags used on macOS](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/#macos)

[Subject index](INDEX.md) · [Previous source section](macos-framework-installation.md) · [Following source section](with-framework-name-framework.md)

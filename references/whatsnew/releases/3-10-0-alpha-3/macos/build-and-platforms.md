# Python 3.10.0 alpha 3 / macos / build and platforms

[bpo-42504](https://bugs.python.org/issue?@action=redirect&bpo=42504): Corrected the build on macOS Big Sur whenever MACOSX_DEPLOYMENT_TARGET=11

[bpo-41116](https://bugs.python.org/issue?@action=redirect&bpo=41116): Make sure distutils.unixxcompiler.find_library_file is able to locate libraries shipped by the system on macOS 11.

[bpo-38443](https://bugs.python.org/issue?@action=redirect&bpo=38443): For the configure script, the `--enable-universalsdk` plus `--with-universal-archs` options now verify that the requested architectures are usable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

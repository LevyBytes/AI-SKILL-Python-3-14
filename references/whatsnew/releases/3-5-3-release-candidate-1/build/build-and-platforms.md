# Python 3.5.3 release candidate 1 / build / build and platforms

[bpo-28676](https://bugs.python.org/issue?@action=redirect&bpo=28676): Kept the missing "getentropy" declaration warning from appearing on macOS. Gareth Rees supplied the patch.

[bpo-29080](https://bugs.python.org/issue?@action=redirect&bpo=29080): Drops the hard dependency on hg.exe out of PCBuild/build.bat

[bpo-28248](https://bugs.python.org/issue?@action=redirect&bpo=28248): Refreshed the Windows build plus the OS X installers so they use OpenSSL 1.0.2j.

[bpo-27983](https://bugs.python.org/issue?@action=redirect&bpo=27983): Turned a missing llvm-profdata tool, which clang needs for PGO linking, into a configure-time error instead of a make-time one whenever --with-optimizations is on. Also strengthened our knack for locating the llvm-profdata tool on MacOS and on certain Linuxes.

[bpo-26359](https://bugs.python.org/issue?@action=redirect&bpo=26359): Added the --with-optimizations configure flag.

[bpo-27453](https://bugs.python.org/issue?@action=redirect&bpo=27453): The CPP invocation within configure has to use CPPFLAGS. Chi Hsuan Yen supplied the patch.

[bpo-27641](https://bugs.python.org/issue?@action=redirect&bpo=27641): The configure script now drops comments into the makefile so the pgen and _freeze_importlib executables avoid being cross-compiled.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

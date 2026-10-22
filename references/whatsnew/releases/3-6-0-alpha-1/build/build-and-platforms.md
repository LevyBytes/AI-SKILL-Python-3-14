# Python 3.6.0 alpha 1 / build / build and platforms

[bpo-25702](https://bugs.python.org/issue?@action=redirect&bpo=25702): A new --with-lto configure switch now turns on link time optimizations while a make profile-opt runs. Certain compilers and toolchains have a reputation for emitting unstable code under LTO, so verify everything carefully before you depend on it. Compared with plain profile-opt, it can yield a few % gain in speed.

[bpo-26079](https://bugs.python.org/issue?@action=redirect&bpo=26079): Corrects the build output folder used for tix-8.4.3.6. Bjoern Thiel contributed the patch.

[bpo-26465](https://bugs.python.org/issue?@action=redirect&bpo=26465): Move the Windows builds onto OpenSSL 1.0.2g.

[bpo-25348](https://bugs.python.org/issue?@action=redirect&bpo=25348): The `--pgo` and `--pgo-job` options were added to `PCbuild\build.bat` so it can build using Profile-Guided Optimization. The former `PCbuild\build_pgo.bat` script has been deleted.

[bpo-25827](https://bugs.python.org/issue?@action=redirect&bpo=25827): `configure` now lets you build with ICC, via a fresh `--with-icc` flag.

[bpo-24986](https://bugs.python.org/issue?@action=redirect&bpo=24986): Python can now be built error-free on Windows even when the external libraries are missing.

[bpo-26465](https://bugs.python.org/issue?@action=redirect&bpo=26465): Have the OS X 10.5+ 32-bit-only installer build against and link to OpenSSL 1.0.2g.

[bpo-26268](https://bugs.python.org/issue?@action=redirect&bpo=26268): Move the Windows builds onto OpenSSL 1.0.2f.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

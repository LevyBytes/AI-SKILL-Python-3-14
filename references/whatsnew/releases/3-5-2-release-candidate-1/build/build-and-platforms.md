# Python 3.5.2 release candidate 1 / build / build and platforms

[bpo-22359](https://bugs.python.org/issue?@action=redirect&bpo=22359): While cross-compiling, the rules that run _freeze_importlib and pgen are now turned off. Output from those programs normally ships alongside the source code anyway and still gets regenerated during a native build. Xavier de Gaye wrote the patch.

[bpo-25702](https://bugs.python.org/issue?@action=redirect&bpo=25702): A new --with-lto configure option now switches on link time optimizations during a make profile-opt build. Because certain compilers and toolchains are known not to emit stable code under LTO, test everything carefully before depending on it. It can deliver a few % gain beyond profile-opt by itself.

[bpo-26079](https://bugs.python.org/issue?@action=redirect&bpo=26079): Corrected the build output folder for tix-8.4.3.6. Bjoern Thiel wrote the patch.

[bpo-26465](https://bugs.python.org/issue?@action=redirect&bpo=26465): The Windows builds were moved to OpenSSL 1.0.2g.

[bpo-25348](https://bugs.python.org/issue?@action=redirect&bpo=25348): Provided `--pgo` and `--pgo-job` arguments for `PCbuild\build.bat` to enable Profile-Guided Optimization builds. The former `PCbuild\build_pgo.bat` script is deprecated now and merely invokes `PCbuild\build.bat --pgo %*`.

[bpo-25827](https://bugs.python.org/issue?@action=redirect&bpo=25827): Building with ICC is now supported by `configure`, via a new `--with-icc` flag.

[bpo-26268](https://bugs.python.org/issue?@action=redirect&bpo=26268): The Windows builds were moved to OpenSSL 1.0.2f.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

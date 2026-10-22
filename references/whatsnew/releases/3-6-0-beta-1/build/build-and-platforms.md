# Python 3.6.0 beta 1 / build / build and platforms

[bpo-27983](https://bugs.python.org/issue?@action=redirect&bpo=27983): When clang drives PGO linking and `--with-optimizations` is on, treat a missing llvm-profdata tool as a configure-time error rather than a make-time one. Also sharpen our ability to locate the llvm-profdata tool on MacOS and some Linuxes.

[bpo-26359](https://bugs.python.org/issue?@action=redirect&bpo=26359): A --with-optimizations flag was added to enable LTO and PGO build support wherever available.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

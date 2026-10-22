# Python 3.7.0 alpha 1 / build / compiler and parser

[bpo-27659](https://bugs.python.org/issue?@action=redirect&bpo=27659): Forbid implicit C function declarations: where feasible, apply `-Werror=implicit-function-declaration` (with GCC and Clang, though it hinges on the compiler version). Chi Hsuan Yen wrote the patch.

[bpo-26851](https://bugs.python.org/issue?@action=redirect&bpo=26851): Configure the Android compilation and link flags.

[bpo-28538](https://bugs.python.org/issue?@action=redirect&bpo=28538): Repair the compilation failure that arises because, while if_nameindex() is present at Android API level 24, the if_nameindex structure is left undefined.

[bpo-20211](https://bugs.python.org/issue?@action=redirect&bpo=20211): Keep both the directory used for installing C header files and the one used for installing object code libraries out of the cross compilation search paths. Thomas Petazzoni wrote the first version of the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

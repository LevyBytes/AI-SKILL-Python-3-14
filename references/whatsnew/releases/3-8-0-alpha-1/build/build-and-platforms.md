# Python 3.8.0 alpha 1 / build / build and platforms

[bpo-35683](https://bugs.python.org/issue?@action=redirect&bpo=35683): Refined the Azure Pipelines build stages, which now confirm layouts properly.

[bpo-35351](https://bugs.python.org/issue?@action=redirect&bpo=35351): With clang plus LTO, the LTO flags are henceforth kept out of CFLAGS used to compile third-party C extensions via distutils.

[bpo-35059](https://bugs.python.org/issue?@action=redirect&bpo=35059): PCbuild: Assign InlineFunctionExpansion the value OnlyExplicitInline (the “/Ob1” option) within pyproject.props under Debug mode so functions tagged inline get expanded. The result should make a Debug-mode Python run somewhat quicker on Windows.

[bpo-33512](https://bugs.python.org/issue?@action=redirect&bpo=33512): The configure check for “long double” was made simpler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

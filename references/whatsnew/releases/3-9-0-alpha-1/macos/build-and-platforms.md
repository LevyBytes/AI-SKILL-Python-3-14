# Python 3.9.0 alpha 1 / macos / build and platforms

[bpo-38117](https://bugs.python.org/issue?@action=redirect&bpo=38117): Updated OpenSSL to 1.1.1d in macOS installer.

[bpo-38089](https://bugs.python.org/issue?@action=redirect&bpo=38089): Bump Azure Pipelines onto the newest VM versions while turning the macOS tests into an optional step

[bpo-34602](https://bugs.python.org/issue?@action=redirect&bpo=34602): Stop calling resource.setrlimit to grow the process stack size limit during execution, which removes test suite failures on macOS. That runtime tweak is unnecessary now that the interpreter ships built with a bigger default stack size.

[bpo-35360](https://bugs.python.org/issue?@action=redirect&bpo=35360): Update macOS installer to use SQLite 3.28.0.

[bpo-34631](https://bugs.python.org/issue?@action=redirect&bpo=34631): Updated OpenSSL to 1.1.1c in macOS installer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

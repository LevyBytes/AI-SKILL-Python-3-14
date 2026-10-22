# 4.11.6. Installing free-threaded binaries

### 4.11.6. Installing free-threaded binaries

Added in version 3.13.

To put in place pre-built binaries with free-threading turned on (see [**PEP 703**](https://peps.python.org/pep-0703/)), choose "Customize installation". On the second page of options sits the "Download free-threaded binaries" checkbox.

 (Figure: ../_images/win_install_freethreaded.png)

Picking this option fetches and installs extra binaries into the very same location as the main Python install. The principal executable goes by `python3.13t.exe`, while the rest of the binaries gain either a `t` suffix or a full ABI suffix. Python source files and the bundled third-party dependencies are shared with the main install.

The free-threaded version registers as an ordinary Python install bearing the tag `3.13t` (with a `-32` or `-arm64` suffix as usual on those platforms). That lets tools find it, and lets the Python install manager handle `py.exe -3.13t`. Be aware that the launcher reads `py.exe -3` (or a `python3` shebang) as "the latest 3.x install", which will favor the free-threaded binaries over the regular ones, whereas `py.exe -3.13` will not. If the short form of the option is what you use, you might rather skip installing the free-threaded binaries for now.

To set the install option from the command line, use `Include_freethreaded=1`. See Installing without downloading for how to download the extra binaries ahead of time for an offline install. The options that bring in debug symbols and binaries cover the free-threaded builds as well.

Free-threaded binaries are also available on nuget.org.

[Subject index](INDEX.md) · [Previous source section](modifying-an-install.md) · [Following source section](../legacy-launcher/python-launcher-for-windows.md)

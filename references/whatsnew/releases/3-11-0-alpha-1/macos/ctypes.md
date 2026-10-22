# Python 3.11.0 alpha 1 / macos / ctypes

[bpo-44689](https://bugs.python.org/issue?@action=redirect&bpo=44689): [`ctypes.util.find_library()`](https://docs.python.org/3.14/library/ctypes.html#ctypes.util.find_library) behaves correctly on macOS 11 Big Sur even where Python was compiled against an older macOS release. Formerly, builds produced on older macOS systems left `find_library` unable to locate macOS system libraries while running on Big Sur, owing to revised storage of system libraries.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

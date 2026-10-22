# Python 3.7.0 alpha 1 / library / memory and lifetimes

[bpo-28275](https://bugs.python.org/issue?@action=redirect&bpo=28275): Closed a potential use-after-free affecting the decompress() routines belonging to both the LZMADecompressor and the BZ2Decompressor classes. John Leitch supplied the original patch.

[bpo-30243](https://bugs.python.org/issue?@action=redirect&bpo=30243): The __init__ methods belonging to _json’s scanner and encoder were dropped, since misuse risked memory leaks or crashes. Both scanner and encoder objects are now fully set up inside their __new__ methods.

[bpo-28638](https://bugs.python.org/issue?@action=redirect&bpo=28638): The implementation approach behind collections.namedtuple() was changed to lean on precomputed methods and thereby cut the reliance on exec() sharply. Consequently the *verbose* parameter together with the *_source* attribute are dropped. The payoffs are 1) a smaller memory footprint for applications that use several named tuples, 2) faster creation of the named tuple class (roughly 4x to 6x, depending on the measurement), and 3) small speed-ups when creating instances via __new__, _make, and _replace. (Jelle Zijlstra is the main patch author, and INADA Naoki, Serhiy Storchaka, and Raymond Hettinger added further improvements.)

[bpo-27778](https://bugs.python.org/issue?@action=redirect&bpo=27778): Repaired a memory leak in os.getrandom() arising when getrandom() is cut short by a signal and the signal handler raises a Python exception.

[bpo-27932](https://bugs.python.org/issue?@action=redirect&bpo=27932): Stopped a memory leak within win32_ver().

- Repaired an UnboundLocalError inside socket._sendfile_use_sendfile.

[bpo-29110](https://bugs.python.org/issue?@action=redirect&bpo=29110): A file object leak in aifc.open(), triggered when the file is passed as a filesystem path yet is not valid AIFF, was corrected. Anthony Zhang contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

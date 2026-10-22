# Python 3.7.0 alpha 1 / library / files and paths

[bpo-27998](https://bugs.python.org/issue?@action=redirect&bpo=27998): Repaired support for bytes paths in os.scandir() under Windows. Eryk Sun authored the patch.

[bpo-19930](https://bugs.python.org/issue?@action=redirect&bpo=19930): For os.makedirs(), the mode argument no longer changes the permission bits on freshly created intermediate-level directories.

[bpo-25455](https://bugs.python.org/issue?@action=redirect&bpo=25455): Crashes in the repr of recursive buffered file-like objects were corrected.

[bpo-28682](https://bugs.python.org/issue?@action=redirect&bpo=28682): Bytes paths are now handled by os.fwalk().

[bpo-29623](https://bugs.python.org/issue?@action=redirect&bpo=29623): A path-like object may now serve as a single argument to ConfigParser.read(). David Ellis contributed the patch.

[bpo-30177](https://bugs.python.org/issue?@action=redirect&bpo=30177): path.resolve(strict=False) stopped truncating the path at the first element absent from the filesystem. Antoine Pietri authored the patch.

[bpo-29998](https://bugs.python.org/issue?@action=redirect&bpo=29998): When ImportError is pickled and copied, its name and path attributes are now retained.

[bpo-10030](https://bugs.python.org/issue?@action=redirect&bpo=10030): Reading encrypted ZIP files was made twice as fast.

[bpo-25996](https://bugs.python.org/issue?@action=redirect&bpo=25996): On Unix, os.scandir() gained support for file descriptors. By relying on os.scandir(), os.fwalk() now runs twice as fast.

[bpo-25803](https://bugs.python.org/issue?@action=redirect&bpo=25803): Spurious errors from Path.mkdir(exist_ok=True) are now avoided when the OS prioritizes errors like EACCES ahead of EEXIST.

[bpo-19717](https://bugs.python.org/issue?@action=redirect&bpo=19717): Path.resolve() now succeeds even for paths that are absent. Vajrasky Kok submitted this patch

[bpo-29416](https://bugs.python.org/issue?@action=redirect&bpo=29416): An endless loop inside pathlib.Path.mkdir is now prevented

[bpo-28847](https://bugs.python.org/issue?@action=redirect&bpo=28847): The dbm.dumb backend can read read-only files now and will skip writing the index file whenever nothing changed. Whenever the index file goes missing and has to be rebuilt under the ‘r’ and ‘w’ modes, a deprecation warning fires (this becomes an error in upcoming Python releases).

[bpo-30897](https://bugs.python.org/issue?@action=redirect&bpo=30897): `pathlib.Path` objects now carry an `is_mount()` method (implemented on POSIX only). It parallels `os.path.ismount(p)`. Cooper Ry Lees wrote the patch.

[bpo-31281](https://bugs.python.org/issue?@action=redirect&bpo=31281): Repair `fileinput.FileInput(files, inplace=True)` whenever `files` holds `pathlib.Path` objects.

[bpo-30038](https://bugs.python.org/issue?@action=redirect&bpo=30038): A race between delivery of a signal and the wakeup file descriptor is now resolved. Nathaniel Smith wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

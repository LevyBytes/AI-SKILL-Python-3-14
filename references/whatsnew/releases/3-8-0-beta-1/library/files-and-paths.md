# Python 3.8.0 beta 1 / library / files and paths

[bpo-24538](https://bugs.python.org/issue?@action=redirect&bpo=24538): Inside `shutil.copystat()`, extended file attributes are copied ahead of the file permissions, because such attributes can only be applied to the destination while it remains writeable.

[bpo-35721](https://bugs.python.org/issue?@action=redirect&bpo=35721): Plugs file-descriptor leaks in `asyncio.SelectorEventLoop.subprocess_exec()` that happened when `Popen` failed under a `stdin=subprocess.PIPE` invocation. Niklas Fiekas supplied the patch.

[bpo-12639](https://bugs.python.org/issue?@action=redirect&bpo=12639): `msilib.Directory.start_component()` will no longer break when *keyfile* differs from `None`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

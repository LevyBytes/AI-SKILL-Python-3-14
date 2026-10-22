# Python 3.8.0 alpha 1 / library / files and paths

[bpo-32410](https://bugs.python.org/issue?@action=redirect&bpo=32410): Steered clear of blocking on file IO inside the sendfile fallback code

[bpo-31715](https://bugs.python.org/issue?@action=redirect&bpo=31715): The `.mjs` file extension is now associated with the `application/javascript` MIME Type.

[bpo-31047](https://bugs.python.org/issue?@action=redirect&bpo=31047): Corrected `ntpath.abspath` for invalid paths on windows. Franz Woellert wrote the patch.

[bpo-30693](https://bugs.python.org/issue?@action=redirect&bpo=30693): The TarFile class now walks directories in a reproducible fashion.

[bpo-30693](https://bugs.python.org/issue?@action=redirect&bpo=30693): The ZipFile class now walks directories in a reproducible fashion.

[bpo-32622](https://bugs.python.org/issue?@action=redirect&bpo=32622): Add a native, fast sendfile path for the Windows proactor event loop.

[bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537): subprocess.Popen now relies on an ExitStack internally to tidy up pipe file handles. Ordinary operation behaves the same as before. Should closing any single handle ever raise, the remaining handles are now closed rather than leaked. (patch by Giampaolo Rodola)

[bpo-21060](https://bugs.python.org/issue?@action=redirect&bpo=21060): Reword the confusing setup.py upload message from "No dist file created in earlier command" into the clearer "Must create and upload files in one command".

[bpo-16965](https://bugs.python.org/issue?@action=redirect&bpo=16965): The 2to3 `execfile` fixer opens the target file using mode `'rb'` now. Zackery Spytz contributed the patch.

[bpo-28441](https://bugs.python.org/issue?@action=redirect&bpo=28441): Under Cygwin and MinGW, `sys.executable` now always carries the complete filename in its path, the `.exe` suffix included (except when it is a symbolic link).

[bpo-34758](https://bugs.python.org/issue?@action=redirect&bpo=34758): The .wasm -> application/wasm mapping was added to the recognized file types and content type headers

[bpo-34097](https://bugs.python.org/issue?@action=redirect&bpo=34097): With a new `strict_timestamps` parameter, ZipFile can archive files dated before 1980-01-01 or after 2107-12-31, at the price of clamping the timestamp to the boundary value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

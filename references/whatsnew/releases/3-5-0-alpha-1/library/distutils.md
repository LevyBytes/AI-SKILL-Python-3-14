# Python 3.5.0 alpha 1 / library / distutils

[bpo-21722](https://bugs.python.org/issue?@action=redirect&bpo=21722): The distutils ?upload? command now returns a non-zero exit code whenever the upload fails. Martin Dengler wrote the patch.

[bpo-10510](https://bugs.python.org/issue?@action=redirect&bpo=10510): The distutils register and upload methods now emit HTML standards compliant CRLF line endings.

[bpo-5309](https://bugs.python.org/issue?@action=redirect&bpo=5309): The distutils' build and build_ext commands now take a `-j` option that turns on parallel building of extension modules.

[bpo-23063](https://bugs.python.org/issue?@action=redirect&bpo=23063): For the distutils' check command, reST parsing of code or code-block directives was corrected.

[bpo-11599](https://bugs.python.org/issue?@action=redirect&bpo=11599): Should an external command (for instance a compiler) fail, distutils now writes out the entire command line rather than only the command name, provided the DISTUTILS_DEBUG environment variable is set.

[bpo-4931](https://bugs.python.org/issue?@action=redirect&bpo=4931): No longer will distutils emit the unhelpful “error: None” messages. distutils.util.grok_environment_error remains but is doc-deprecated.

[bpo-8876](https://bugs.python.org/issue?@action=redirect&bpo=8876): When hard linking fails, distutils now falls back to copying the files. This permits use on special filesystems like VirtualBox shared folders.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

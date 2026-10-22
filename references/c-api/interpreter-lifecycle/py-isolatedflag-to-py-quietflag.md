# interpreter lifecycle C API: `Py_IsolatedFlag`, `Py_LegacyWindowsFSEncodingFlag`, `Py_LegacyWindowsStdioFlag`, `Py_NoSiteFlag`, `Py_NoUserSiteDirectory`, `Py_OptimizeFlag`, `Py_QuietFlag`

int Py_IsolatedFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.isolated`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.isolated) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Run Python under isolated mode. Under isolated mode, [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) excludes both the script's own directory and the user's site-packages directory.

Set by the [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) option.

Added in version 3.4.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_LegacyWindowsFSEncodingFlag

Retained only for backward compatibility: prefer assigning [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

When this flag is non-zero, the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) switches to the `mbcs` encoding paired with the `replace` error handler, rather than UTF-8 with the `surrogatepass` error handler.

Becomes `1` whenever the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable holds a non-empty string.

Consult [**PEP 529**](https://peps.python.org/pep-0529/) for further details.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_LegacyWindowsStdioFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.legacy_windows_stdio) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

When this flag is non-zero, [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO) is used in place of `io._WindowsConsoleIO` for the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) standard streams.

Becomes `1` whenever the [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO) environment variable holds a non-empty string.

Consult [**PEP 528**](https://peps.python.org/pep-0528/) for further details.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_NoSiteFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.site_import`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.site_import) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Suppress importing the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module along with the site-dependent adjustments to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) it would otherwise perform. Those adjustments are also suppressed if `site` is imported explicitly afterward (invoke [`site.main()`](https://docs.python.org/3.14/library/site.html#site.main) should you want them applied).

Set by the [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) option.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_NoUserSiteDirectory

Retained only for backward compatibility: prefer assigning [`PyConfig.user_site_directory`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.user_site_directory) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Keep the [`user site-packages directory`](https://docs.python.org/3.14/library/site.html#site.USER_SITE) out of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

Set by the [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) and [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) options, and the [`PYTHONNOUSERSITE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNOUSERSITE) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_OptimizeFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.optimization_level`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.optimization_level) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Set by the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) option and the [`PYTHONOPTIMIZE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONOPTIMIZE) environment variable.

Deprecated since version 3.12, will be removed in version 3.15.

 int Py_QuietFlag

Retained only for backward compatibility: prefer assigning [`PyConfig.quiet`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.quiet) instead, see [Python Initialization Configuration](https://docs.python.org/3.14/c-api/init_config.html#init-config).

Suppress the copyright and version banners even when running interactively.

Set by the [`-q`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-q) option.

Added in version 3.2.

Deprecated since version 3.12, will be removed in version 3.15.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-byteswarningflag-to-py-interactiveflag.md) · [Following source contract](py-unbufferedstdioflag-to-py-verboseflag.md)

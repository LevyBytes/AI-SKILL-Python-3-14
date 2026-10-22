# initialization config C API: Standard-stream buffering and C stdio setup

int buffered_stdio

When this is `0` while `configure_c_stdio` is non-zero, buffering is turned off for the C streams stdout and stderr.

Assigned `0` by the [`-u`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-u) command line option together with the [`PYTHONUNBUFFERED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUNBUFFERED) environment variable.

stdin is opened in buffered mode at all times.

Default: `1`.

 int bytes_warning

When this is `1`, a warning is raised on comparing [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) against [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), or on comparing `bytes` against [`int`](https://docs.python.org/3.14/library/functions.html#int).

At `2` or above, a [`BytesWarning`](https://docs.python.org/3.14/library/exceptions.html#BytesWarning) exception is raised in those same situations.

Incremented by the [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) command line option.

Default: `0`.

 int warn_default_encoding

When non-zero, an [`EncodingWarning`](https://docs.python.org/3.14/library/exceptions.html#EncodingWarning) warning is produced wherever [`io.TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) falls back on its default encoding. Consult [Opt-in EncodingWarning](https://docs.python.org/3.14/library/io.html#io-encoding-warning) for the particulars.

Default: `0`.

Added in version 3.10.

 int code_debug_ranges

When this is `0`, the end line and column mappings are no longer embedded in code objects. It additionally turns off traceback carets pointing at specific error locations.

Assigned `0` by the [`PYTHONNODEBUGRANGES`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNODEBUGRANGES) environment variable as well as by the [`-X no_debug_ranges`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option.

Default: `1`.

Added in version 3.11.

 wchar_t *check_hash_pycs_mode

Governs how hash-based `.pyc` files are validated: it holds the value of the [`--check-hash-based-pycs`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-check-hash-based-pycs) command line option.

Valid values:

- `L"always"`: Hash the source file for invalidation no matter what the 'check_source' flag holds.

- `L"never"`: Treat hash-based pycs as always valid.

- `L"default"`: Let the 'check_source' flag inside the hash-based pycs decide invalidation.

Default: `L"default"`.

See also [**PEP 552**](https://peps.python.org/pep-0552/) "Deterministic pycs".

 int configure_c_stdio

When non-zero, the C standard streams are configured:

- Under Windows, binary mode (`O_BINARY`) is applied to stdin, stdout and stderr.

- Where `buffered_stdio` is zero, buffering of the stdin, stdout and stderr streams is turned off.

- Where `interactive` is non-zero, stream buffering is switched on for stdin and stdout (stdout alone on Windows).

Default: `1` in Python config, `0` in isolated config.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-to-pyconfig-parse-argv.md) · [Previous source contract](pyconfig-use-environment-to-base-prefix.md) · [Following source contract](dev-mode-to-faulthandler.md)

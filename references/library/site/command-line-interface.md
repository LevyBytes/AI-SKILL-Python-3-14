# site - Command-line interface

### Command-line interface

From the command line, the `site` module likewise offers a means to fetch the user directories:

```shell
$ python -m site --user-site
/home/user/.local/lib/python3.11/site-packages

```

Run with no arguments, it writes the contents of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) to standard output, then the `USER_BASE` value along with whether that directory exists, then the equivalent details for `USER_SITE`, and lastly the `ENABLE_USER_SITE` value.

 --user-base

Emit the path leading to the user base directory.

 --user-site

Emit the path leading to the user site-packages directory.

Supplying both options causes user base and user site to be emitted (invariably in that sequence), divided by [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep).

Whenever an option is supplied, the script exits with one of the following codes: `0` when the user site-packages directory is enabled, `1` when the user disabled it, `2` when it is off for security reasons or by an administrator, and anything above 2 when an error arises.

See also

- [**PEP 370**](https://peps.python.org/pep-0370/) – Per user site-packages directory

- [The initialization of the sys.path module search path](https://docs.python.org/3.14/library/sys_path_init.html#sys-path-init) – The initialization of [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

[Subject index](INDEX.md) · [Previous](site-prefixes-to-site-getusersitepackages.md) · [Continue](../smtpd/smtpd-smtp-server.md) · [Owning module, declaration or section: site](site-site-specific-configuration-hook.md)

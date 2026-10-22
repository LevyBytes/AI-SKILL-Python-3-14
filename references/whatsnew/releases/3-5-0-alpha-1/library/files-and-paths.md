# Python 3.5.0 alpha 1 / library / files and paths

[bpo-22165](https://bugs.python.org/issue?@action=redirect&bpo=22165): File names that cannot be decoded are now handled by SimpleHTTPRequestHandler.

[bpo-17923](https://bugs.python.org/issue?@action=redirect&bpo=17923): On AIX, glob() patterns that end in a slash will no longer match anything that isn't a directory. Delhallt's patch served as the basis.

[bpo-14099](https://bugs.python.org/issue?@action=redirect&bpo=14099): ZipFile.open() stops reopening the underlying file. The objects ZipFile.open() hands back can now work independently of the ZipFile, even when that ZipFile was built by passing a file-like object as the constructor's first argument.

[bpo-22966](https://bugs.python.org/issue?@action=redirect&bpo=22966): The __pycache__ pyc file name collision was fixed for the case where pyc_compile compiles a source file whose name carries several dots.

[bpo-21101](https://bugs.python.org/issue?@action=redirect&bpo=21101): Got rid of duplicate hashing inside the C acceleration path for collections.Counter().

[bpo-21127](https://bugs.python.org/issue?@action=redirect&bpo=21127): It is now possible to build Path objects out of str subclass instances, for example `numpy.str_`.

[bpo-21766](https://bugs.python.org/issue?@action=redirect&bpo=21766): A security hole in CGIHTTPServer was closed by URL-unquoting paths before a CGI script is looked for at that location.

[bpo-11709](https://bugs.python.org/issue?@action=redirect&bpo=11709): The pydoc.help function was fixed so it does not break when sys.stdin is not a valid file.

[bpo-19076](https://bugs.python.org/issue?@action=redirect&bpo=19076): The superfluous ?file? argument is no longer passed to self.error().

[bpo-20639](https://bugs.python.org/issue?@action=redirect&bpo=20639): Invoking Path.with_suffix(??) now lets you strip the suffix once more. July Tikhonov wrote the patch.

[bpo-21714](https://bugs.python.org/issue?@action=redirect&bpo=21714): Building invalid paths via Path.with_name() is now forbidden. Antony Lee contributed the first patch.

[bpo-22054](https://bugs.python.org/issue?@action=redirect&bpo=22054): The pair os.get_blocking() and os.set_blocking() were added to query and change a file descriptor's blocking mode (False when the O_NONBLOCK flag is on, otherwise True). Windows does not provide these functions.

[bpo-15002](https://bugs.python.org/issue?@action=redirect&bpo=15002): The urllib.response object now relies on the _TemporaryFileWrapper (plus _TemporaryFileCloser) machinery. This yields cleaner handling of closing the file descriptor. Christian Theune sent in the patch.

[bpo-21155](https://bugs.python.org/issue?@action=redirect&bpo=21155): Should both path and sock be supplied together, asyncio.EventLoop.create_unix_server() now throws a ValueError.

[bpo-20218](https://bugs.python.org/issue?@action=redirect&bpo=20218): The handy methods read_text/write_text along with read_bytes/ write_bytes were added to pathlib.Path objects.

[bpo-20912](https://bugs.python.org/issue?@action=redirect&bpo=20912): Directories that get added to a ZIP file now carry correct Unix and MS-DOS directory attributes.

[bpo-21866](https://bugs.python.org/issue?@action=redirect&bpo=21866): ZipFile.close() stops writing ZIP64 central directory records whenever allowZip64 is false.

[bpo-14099](https://bugs.python.org/issue?@action=redirect&bpo=14099): Brought back the ability to write ZIP files onto streams that are tellable yet not seekable.

[bpo-19777](https://bugs.python.org/issue?@action=redirect&bpo=19777): Path objects now expose a home() classmethod. Victor Salgado and Mayank Tripathi contributed it.

[bpo-19776](https://bugs.python.org/issue?@action=redirect&bpo=19776): Path objects received an expanduser() method.

[bpo-22759](https://bugs.python.org/issue?@action=redirect&bpo=22759): Query methods on pathlib.Path() (exists(), is_dir(), and so on) now hand back False whenever the backing stat call throws NotADirectoryError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

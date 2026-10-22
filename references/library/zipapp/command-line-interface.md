# zipapp — Command-Line Interface

### Command-Line Interface

Invoked as a program at the command line, it takes the form below:

```shell
$ python -m zipapp source [options]

```

Where *source* names a directory, an archive is built from whatever that *source* directory holds. Where *source* names a file, it ought to be an archive, and it gets copied across to the target archive (or, with the –info option set, its shebang line is shown instead).

These options are recognized:

`-o <output>, --output=<output>`

Send the output to a file called *output*. Leave this option off and the output filename matches the input *source* with `.pyz` tacked on. Pass an explicit name and it’s taken verbatim (so include a `.pyz` extension yourself if you need one).

You must give an output filename when the *source* is an archive (and there, *output* may not equal *source*).

`-p <interpreter>, --python=<interpreter>`

Prepend a `#!` line to the archive that names *interpreter* as the command to run with. On POSIX it additionally marks the archive executable. By default no `#!` line is written and the file is left non-executable.

`-m <mainfn>, --main=<mainfn>`

Place a `__main__.py` file in the archive that runs *mainfn*. The *mainfn* argument is expected to read “pkg.mod:fn”, where “pkg.mod” names a package/module inside the archive and “fn” names a callable within that module. The `__main__.py` file goes on to call it.

`--main` is not allowed while copying an archive.

`-c, --compress`

Shrink the output file by compressing its files with the deflate method. The default leaves files in the archive uncompressed.

`--compress` does nothing when an archive is being copied.

Added in version 3.7.

`--info`

For diagnostic use, print the interpreter baked into the archive. Here every other option is disregarded, and SOURCE has to be an archive rather than a directory.

`-h, --help`

Show a brief usage message, then exit.

[Subject index](INDEX.md) · [Previous](basic-example.md) · [Continue](zipapp-create-archive-to-zipapp-get-interpreter.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)

# tarfile: Archive detection, extraction exceptions and initial member types

tarfile.is_tarfile(*name*)

Hand back [`True`](https://docs.python.org/3.14/library/constants.html#True) when *name* is a tar archive file that the `tarfile` module can read. The *name* argument may be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), file, or file-like object.

Changed in version 3.9: Support for file and file-like objects.

These are the exceptions the `tarfile` module defines:

 *exception *tarfile.TarError

Base class for all `tarfile` exceptions.

 *exception *tarfile.ReadError

Raised whenever a tar archive is opened that either falls outside what the `tarfile` module can handle or is invalid in some way.

 *exception *tarfile.CompressionError

Raised whenever a compression method has no support or when the data cannot be decoded properly.

 *exception *tarfile.StreamError

Raised for the limitations that come with stream-like `TarFile` objects.

 *exception *tarfile.ExtractError

Raised for *non-fatal* errors during `TarFile.extract()`, but solely when `TarFile.errorlevel``== 2`.

 *exception *tarfile.HeaderError

Raised by `TarInfo.frombuf()` whenever the buffer handed to it is invalid.

 *exception *tarfile.FilterError

Base class for members refused by filters.

 tarinfo

Information about the member that the filter refused to extract, as TarInfo.

 *exception *tarfile.AbsolutePathError

Raised to refuse extracting a member with an absolute path.

 *exception *tarfile.OutsideDestinationError

Raised to refuse extracting a member outside the destination directory.

 *exception *tarfile.SpecialFileError

Raised to decline extraction of a special file, for instance a device or pipe.

 *exception *tarfile.AbsoluteLinkError

Raised to refuse extracting a symbolic link with an absolute path.

 *exception *tarfile.LinkOutsideDestinationError

Raised to refuse extracting a symbolic link pointing outside the destination directory.

 *exception *tarfile.LinkFallbackError

Raised to refuse emulating a link (hard or symbolic) by extracting a different archive member, in cases where that member would itself be rejected by the filter location. Whatever exception was raised to reject the substitute member is reachable through `BaseException.__context__`.

Added in version 3.14.

At the module level the following constants are provided:

 tarfile.ENCODING

The character encoding used by default: on Windows it is `'utf-8'`, and elsewhere it is whatever [`sys.getfilesystemencoding()`](https://docs.python.org/3.14/library/sys.html#sys.getfilesystemencoding) hands back.

 tarfile.REGTYPE

 tarfile.AREGTYPE

A regular file `type`.

 tarfile.LNKTYPE

A link (inside tarfile) `type`.

[Subject index](INDEX.md) · [Previous](tarfile-tarfile-class.md) · [Continue](tarfile-symtype-to-tarfile-default-format.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)

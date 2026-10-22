# mimetypes: Filename-to-MIME lookup and encoding maps

# Mimetypes, Mm

## Overview

Covers: mimetypes — Map filenames to MIME types; Multimedia Services.

## mimetypes — Map filenames to MIME types

### `mimetypes` — Map filenames to MIME types

**Source code:** [Lib/mimetypes.py](https://github.com/python/cpython/tree/3.14/Lib/mimetypes.py)

---

Translating between a filename or URL and the MIME type tied to its filename extension is the job of the `mimetypes` module. It can go from filename to MIME type and from MIME type back to filename extension, though that reverse direction offers no encoding support.

Alongside a single class, the module ships several convenience functions. Those functions form the usual way to work with the module, yet certain applications may find the class worthwhile too.

What follows are the functions that make up the module's main interface. When the module is still uninitialized, any of them that depend on what `init()` prepares will call `init()` themselves.

 mimetypes.guess_type(*url*, *strict=True*)

Infer a file's type from its filename, path, or URL, supplied through *url*. That URL may be a string or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

What comes back is a tuple `(type, encoding)`, in which *type* is `None` when the type defies guessing (a suffix that's absent or unrecognized), or otherwise a string shaped like `'type/subtype'` that fits a MIME *content-type* header.

*encoding* holds `None` when there is no encoding, or else the name of whatever program did the encoding (for instance **compress** or **gzip**). This encoding belongs in a *Content-Encoding* header, **not** in a *Content-Transfer-Encoding* header. Table-driven mappings govern all of this. Encoding suffixes are matched case sensitively, while type suffixes are checked first case sensitively and then case insensitively.

That optional *strict* argument is a flag governing whether the roster of known MIME types stays confined to the official ones [registered with IANA](https://www.iana.org/assignments/media-types/media-types.xhtml). Even so, how this module behaves hinges in part on the host operating system. Identification is possible only for file types the OS knows about or that have been explicitly registered in Python's internal database. With *strict* set to `True` (its default), nothing beyond the IANA types is honored; with *strict* set to `False`, a handful of extra non-standard yet widely used MIME types come into play as well.

Changed in version 3.8: Support arrived for *url* taking the form of a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.13: Handing in a file path in place of a URL is now soft deprecated. Turn to `guess_file_type()` instead.

 mimetypes.guess_file_type(*path*, ***, *strict=True*)

Work out a file's type from its path, provided via *path*. It mirrors the `guess_type()` function but takes a path rather than a URL. The path may be a string, a bytes object, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Added in version 3.13.

 mimetypes.guess_all_extensions(*type*, *strict=True*)

Work out the extensions for a file from its MIME type, supplied as *type*. The result is a list of strings naming every possible filename extension, the leading dot (`'.'`) included. There's no promise these extensions were ever tied to a specific data stream, but `guess_type()` and `guess_file_type()` would map them to the MIME type *type*.

The optional *strict* argument carries the very same sense it does for the `guess_type()` function.

 mimetypes.guess_extension(*type*, *strict=True*)

Work out a single extension for a file from its MIME type, supplied as *type*. The result is one string holding a filename extension, the leading dot (`'.'`) included. That extension carries no guarantee of having been linked to a particular data stream, yet `guess_type()` and `guess_file_type()` would map it to the MIME type *type*. Where no extension can be inferred for *type*, the result is `None`.

Here too the optional *strict* argument means exactly what it means for the `guess_type()` function.

A few more functions and data items exist for steering how the module behaves.

 mimetypes.init(*files=None*)

Set up the internal data structures. When provided, *files* has to be a sequence of file names meant to extend the default type map. When left out, the file names come from `knownfiles`, and on Windows the present registry settings are read in. Any file listed in *files* or `knownfiles` outranks those listed ahead of it. You are free to call `init()` more than once.

Handing *files* an empty list keeps the system defaults from taking effect, leaving only the well-known values drawn from a built-in list.

Should *files* be `None`, the internal data structure is rebuilt from scratch to its original default. The operation is stable, yielding identical results no matter how often you invoke it.

Changed in version 3.2: In prior releases, the Windows registry settings went unread.

 mimetypes.read_mime_types(*filename*)

Read in the type map held in the file *filename*, assuming it exists. What you get back is a dictionary that maps filename extensions — the leading dot (`'.'`) included — onto strings shaped like `'type/subtype'`. When the file *filename* is missing or unreadable, the result is `None`.

 mimetypes.add_type(*type*, *ext*, *strict=True*)

Register a mapping that ties the MIME type *type* to the extension *ext*. Where the extension is already on record, its old type gives way to the new one. Where the type is already on record, the extension joins that type's list of known extensions.

With *strict* set to `True` (the default), the mapping joins the official MIME types; otherwise it joins the non-standard ones.

 mimetypes.inited

A flag telling you whether the global data structures have been initialized. `init()` flips it to `True`.

 mimetypes.knownfiles

A list of the type map file names that are commonly installed. Such files usually go by the name `mime.types`, and different packages drop them in different places.

 mimetypes.suffix_map

A dictionary that maps suffixes onto suffixes. Its purpose is to make encoded files recognizable in cases where one extension stands in for both the encoding and the type. The `.tgz` extension, for instance, maps to `.tar.gz` so the encoding and the type can be told apart.

 mimetypes.encodings_map

A dictionary that maps filename extensions onto encoding types.

[Subject index](INDEX.md) · [Continue](mimetypes-types-map-to-mimetypes-common-types.md)

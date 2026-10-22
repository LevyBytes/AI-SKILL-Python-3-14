# mimetypes.MimeTypes: `guess_extension()`, `guess_type()`, `guess_file_type()`, `guess_all_extensions()`, `read()`, `readfp()`, `read_windows_registry()`, `add_type()`

suffix_map

A dictionary pairing suffixes with suffixes. It exists so that encoded files stay recognizable when a single extension conveys both the encoding and the type at once. As an example, `.tgz` maps over to `.tar.gz`, keeping the encoding and the type distinguishable. At the start it is simply a copy of the module-wide `suffix_map` defined globally.

 encodings_map

A dictionary pairing filename extensions with encoding types. To begin with, it is just a copy of the module-wide `encodings_map` defined globally.

 types_map

A tuple holding two dictionaries that pair filename extensions with MIME types: the first dictionary covers the non-standard types and the second covers the standard ones. Their initial contents come from `common_types` and `types_map`.

 types_map_inv

A tuple holding two dictionaries that pair MIME types with a list of filename extensions: again the first dictionary handles the non-standard types and the second handles the standard ones. They draw their initial values from `common_types` and `types_map`.

 guess_extension(*type*, *strict=True*)

Behaves like the `guess_extension()` function, drawing on the tables kept inside the object.

 guess_type(*url*, *strict=True*)

Works much as the `guess_type()` function does, relying on the tables held within the object.

 guess_file_type(*path*, ***, *strict=True*)

Parallels the `guess_file_type()` function, making use of the tables that live in the object.

Added in version 3.13.

 guess_all_extensions(*type*, *strict=True*)

Functions in the same way as `guess_all_extensions()`, pulling from the tables retained by the object.

 read(*filename*, *strict=True*)

Pull MIME information out of a file called *filename*. The parsing is carried out by `readfp()`.

When *strict* holds `True`, the information goes into the list of standard types; otherwise it lands among the non-standard ones.

 readfp(*fp*, *strict=True*)

Pull MIME type information from an already-open file *fp*. That file has to follow the layout of the standard `mime.types` files.

Where *strict* is `True`, the information is filed under the standard types; failing that, it joins the non-standard types.

 read_windows_registry(*strict=True*)

Pull MIME type information straight from the Windows registry.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Should *strict* be `True`, the information is recorded under the standard types; if not, it goes to the non-standard types.

Added in version 3.2.

 add_type(*type*, *ext*, *strict=True*)

Set up a mapping linking the MIME type *type* with the extension *ext*. A valid extension either opens with a ‘.’ or is empty. If the extension is already on record, the fresh type supplants the previous one. If the type is already on record, the extension gets appended to that type's known extensions.

Where *strict* equals `True` (the default), the mapping is filed with the official MIME types; in other cases, with the non-standard ones.

Deprecated since version 3.14, will be removed in version 3.16: Extensions that are invalid and lack a dot will trigger a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) in Python 3.16.

[Subject index](INDEX.md) · [Previous](mimetypes-mimetypes-class.md) · [Continue](command-line-usage.md) · [Owning module, declaration or section: mimetypes](mimetypes-guess-type-to-mimetypes-encodings-map.md) · [Owning module, declaration or section: mimetypes.MimeTypes](mimetypes-mimetypes-class.md) · [Owning module, declaration or section: MimeTypes objects](mimetypes-mimetypes-class.md)

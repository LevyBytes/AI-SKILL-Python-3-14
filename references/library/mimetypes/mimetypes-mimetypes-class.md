# mimetypes: `mimetypes.MimeTypes`

### MimeTypes objects

For applications that might need several MIME-type databases at once, the `MimeTypes` class can come in handy; the interface it presents resembles that of the `mimetypes` module.

 *class *mimetypes.MimeTypes(*filenames=()*, *strict=True*)

A MIME-types database is what this class stands for. Out of the box it reaches the very database the rest of the module uses. That starting database is a copy of the module's own, and you can grow it by pulling more `mime.types`-style files in through the `read()` or `readfp()` methods. Should you not want the default data, you may also wipe the mapping dictionaries before loading anything new.

By way of the optional *filenames* parameter, you can have extra files stacked “on top” of the default database.

[Subject index](INDEX.md) · [Previous](mimetypes-types-map-to-mimetypes-common-types.md) · [Continue](mime-extension-lookup-and-type-registration.md) · [Owning module, declaration or section: mimetypes](mimetypes-guess-type-to-mimetypes-encodings-map.md)

# zipfile / Work with ZIP archives: `zipfile.ZipInfo`, `_for_archive()`

*class *zipfile.ZipInfo(*filename='NoName'*, *date_time=(1980, 1, 1, 0, 0, 0)*)

Class that holds details about an individual archive member. The `getinfo()` and `infolist()` methods of `ZipFile` objects hand back instances of this class. Typically people working with the `zipfile` module won't construct these themselves and instead rely on the ones the module supplies. Here *filename* is the complete name of the archive member, while *date_time* is a six-field tuple recording when the file was last modified; those fields appear in the ZipInfo objects section.

Changed in version 3.13: A public `compress_level` attribute now surfaces what used to be the protected `_compresslevel`. For backward compatibility, the earlier protected name still functions, exposed as a property.

 _for_archive(*archive*)

Settle the date_time, compression, and external-attribute values to the sensible defaults that `ZipFile.writestr()` relies on.

Returns self for chaining.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous](zipfile-pyzipfile-class.md) · [Continue](zipfile-is-zipfile-to-zipfile-zip-zstandard.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md)

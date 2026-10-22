# zipimport: `zipimport.zipimporter`

### zipimporter Objects

The class responsible for importing ZIP files is `zipimporter`.

 *class *zipimport.zipimporter(*archivepath*)

Builds a fresh zipimporter instance. The *archivepath* has to name either a ZIP file or some specific location inside one. To illustrate, an *archivepath* set to `foo/bar.zip/lib` searches for modules within the `lib` directory that sits inside the ZIP file `foo/bar.zip` (assuming such a directory is present).

Should *archivepath* fail to reference a valid ZIP archive, `ZipImportError` is thrown.

Changed in version 3.12: The `find_loader()` and `find_module()` methods, marked deprecated back in 3.10, have now been dropped — reach for `find_spec()` in their place.

[Subject index](INDEX.md) · [Previous](zipimport-zipimporterror.md) · [Continue](zip-importer-module-creation-and-caches.md) · [Owning module, declaration or section: zipimport](zipimport-zipimporterror.md)

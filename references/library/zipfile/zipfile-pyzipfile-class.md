# zipfile: `zipfile.PyZipFile`

*class *zipfile.PyZipFile

A class that builds ZIP archives holding Python libraries.

### PyZipFile objects

The `PyZipFile` constructor accepts the very same parameters as the `ZipFile` constructor, plus one extra parameter, *optimize*.

 *class *zipfile.PyZipFile(*file*, *mode='r'*, *compression=ZIP_STORED*, *allowZip64=True*, *optimize=-1*)

Changed in version 3.2: Added the *optimize* parameter.

Changed in version 3.4: ZIP64 extensions are enabled by default.

Instances have one method in addition to those of `ZipFile` objects:

[Subject index](INDEX.md) · [Previous](zipfile-path-class.md) · [Continue](zipfile-zipinfo-class-to-zipfile-zipinfo-for-archive.md) · [Owning module, declaration or section: zipfile](zipfile-badzipfile-to-zipfile-largezipfile.md) · [Previous](path-joinpath.md) · [Continue](zipfile-pyzipfile-writepy.md)

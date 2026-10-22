# tarfile — Filter errors

### Filter errors

Whenever a filter declines to extract a file, it raises a fitting exception, which is a subclass of `FilterError`. That aborts the extraction when `TarFile.errorlevel` is 1 or higher. Under `errorlevel=0` the error is logged and the member is skipped, while extraction keeps going.

[Subject index](INDEX.md) · [Previous](tarfile-fully-trusted-filter-to-tarfile-data-filter.md) · [Continue](hints-for-further-verification.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)

# tarfile - Extraction filters

### Extraction filters

Added in version 3.12.

The *tar* format aims to record every detail of a UNIX-like filesystem, which gives it a great deal of power. Sadly, those same capabilities make it simple to build tar files that produce unintended - and perhaps malicious - results once extracted. Extracting a tar file might, for example, overwrite arbitrary files through several routes (using absolute paths, `..` path components, or symlinks that influence members that come later).

The full set of capabilities is unnecessary in most situations. For that reason, *tarfile* offers extraction filters: a way to curtail functionality and thereby reduce some of the security concerns.

Warning

Not one of the supplied filters shuts out *all* dangerous archive features. Archives from untrusted sources should never be extracted before you inspect them. Consult Hints for further verification as well.

See also

[**PEP 706**](https://peps.python.org/pep-0706/)

Contains further motivation and rationale behind the design.

The *filter* argument passed to `TarFile.extract()` or `extractall()` may be:

- the string `'fully_trusted'`: Honor every piece of metadata exactly as the archive specifies. Reach for this when the archive is trusted outright, or when you supply your own elaborate verification.

- the string `'tar'`: Honor the bulk of *tar*-specific behavior (that is, the behaviors of UNIX-like filesystems) while blocking the ones most apt to be surprising or malicious. Consult `tar_filter()` for specifics.

- the string `'data'`: Ignore or block the majority of features that are specific to UNIX-like filesystems. Meant for pulling data out of cross-platform archives. Consult `data_filter()` for specifics.

- `None` (default): Use `TarFile.extraction_filter`.

If that is also `None` (the default), the `'data'` filter will be used.

>

Changed in version 3.14: `data` is now the default filter. Earlier, the default behaved like `fully_trusted`.

- A callable that gets invoked for each extracted member, receiving a TarInfo that describes the member and the destination path the archive is being extracted to (the same path applies to every member):

```python
filter(member: TarInfo, path: str, /) -> TarInfo | None

```

Because the callable fires right before each member is extracted, it can factor in the disk's present state. It can:

  - hand back a `TarInfo` object to be applied in place of the archive's stored metadata, or

  - hand back `None`, which causes that member to be skipped, or

  - raise an exception in order to halt the whole operation or skip just that member, the choice depending on `errorlevel`. Keep in mind that once extraction is halted, `extractall()` may leave the archive only partly extracted. No cleanup is attempted.

[Subject index](INDEX.md) · [Previous](tarinfo-isreg-to-tarinfo-isdev.md) · [Continue](tarfile-fully-trusted-filter-to-tarfile-data-filter.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)

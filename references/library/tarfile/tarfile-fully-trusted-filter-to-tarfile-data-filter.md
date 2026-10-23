# tarfile - Default named filters

### Default named filters

The pre-defined, named filters are exposed as functions so that custom filters can reuse them:

 tarfile.fully_trusted_filter(*member*, *path*)

Return *member* unchanged.

This implements the `'fully_trusted'` filter.

 tarfile.tar_filter(*member*, *path*)

Implements the `'tar'` filter.

- Strip leading slashes (`/` and [`os.sep`](https://docs.python.org/3.14/library/os.html#os.sep)) from filenames.

- Decline to extract files bearing absolute paths (for cases where the name stays absolute even once slashes are stripped, such as `C:/foo` on Windows). This raises `AbsolutePathError`.

- Decline to extract any file whose absolute path (after symlinks are followed) would land outside the destination. This raises `OutsideDestinationError`.

- Clear high mode bits (setuid, setgid, sticky) and group/other write bits ([`S_IWGRP`](https://docs.python.org/3.14/library/stat.html#stat.S_IWGRP) | [`S_IWOTH`](https://docs.python.org/3.14/library/stat.html#stat.S_IWOTH)).

Return the modified `TarInfo` member.

 tarfile.data_filter(*member*, *path*)

Implements the `'data'` filter. Beyond everything `tar_filter` does:

- Normalize link targets (`TarInfo.linkname`) using [`os.path.normpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.normpath). Be aware that this strips out internal `..` components, which can alter what the link means whenever the path in `TarInfo.linkname` crosses symbolic links.

- Decline to extract links (whether hard or soft) that point at absolute paths, or that point somewhere outside the destination.

This raises `AbsoluteLinkError` or `LinkOutsideDestinationError`.

Bear in mind that these files get rejected even where the platform has no symbolic link support.

- Decline to extract device files (pipes included). This raises `SpecialFileError`.

- For regular files, including hard links:

  - Set the owner read and write permissions ([`S_IRUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IRUSR) | [`S_IWUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IWUSR)).

  - Drop the group and other executable permission ([`S_IXGRP`](https://docs.python.org/3.14/library/stat.html#stat.S_IXGRP) | [`S_IXOTH`](https://docs.python.org/3.14/library/stat.html#stat.S_IXOTH)) whenever the owner lacks it ([`S_IXUSR`](https://docs.python.org/3.14/library/stat.html#stat.S_IXUSR)).

- For the remaining files (directories), assign `mode` the value `None`, which keeps extraction methods from applying permission bits.

- Assign `None` to the user and group fields (`uid`, `gid`, `uname`, `gname`), which keeps extraction methods from setting them.

Return the modified `TarInfo` member.

Keep in mind that this filter leaves *some* dangerous archive features unblocked. Details appear under Hints for further verification.

Changed in version 3.14: Link targets are now normalized.

[Subject index](INDEX.md) · [Previous](extraction-filters.md) · [Continue](filter-errors.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)

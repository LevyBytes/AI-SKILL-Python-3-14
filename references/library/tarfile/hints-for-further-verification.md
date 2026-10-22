# tarfile — Hints for further verification

### Hints for further verification

Even under `filter='data'`, *tarfile* is not the right tool for extracting untrusted files without inspecting them first. For one thing, the pre-defined filters offer no protection against denial-of-service attacks. Users ought to run extra checks.

What follows is a partial list of points to weigh:

- Unpack into a [`new temporary directory`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp); this blocks, for instance, the abuse of already-present links and simplifies cleanup should an extraction fail.

- Forbid symbolic links whenever you have no need for that capability.

- For untrusted data, impose external caps (at the OS level, say) on disk, memory, and CPU consumption.

- Validate filenames against a character allow-list (so that control characters, confusables, foreign path separators, and the like are screened out).

- Confirm that filenames carry the extensions you expect (steering away from files that run when you "click on them", or from extension-less files such as Windows special device names).

- Cap the count of extracted files, the aggregate size of extracted data, the length of filenames (symlink length included), and the size of each individual file.

- Watch for files that case-insensitive filesystems would end up shadowing.

Also note that:

- A tar file may hold several versions of one file. The later versions are meant to supersede any earlier ones. This behavior is essential for updating tape archives, yet it lends itself to malicious abuse.

- *tarfile* offers no defense against problems with "live" data, such as an attacker meddling with the destination (or source) directory while extraction (or archiving) is underway.

[Subject index](INDEX.md) · [Previous](filter-errors.md) · [Continue](supporting-older-python-versions.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)

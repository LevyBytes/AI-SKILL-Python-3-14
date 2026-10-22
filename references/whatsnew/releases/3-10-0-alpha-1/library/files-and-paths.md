# Python 3.10.0 alpha 1 / library / files and paths

[bpo-40564](https://bugs.python.org/issue?@action=redirect&bpo=40564): Within `zipfile.Path`, mutate the type of the supplied ZipFile object rather than duplicating it. This avoids trouble when the local copy and the caller's copy each try to close the same file handle.

[bpo-33660](https://bugs.python.org/issue?@action=redirect&bpo=33660): Corrected pathlib.PosixPath so it resolves a relative path sitting on the root directory the right way.

[bpo-40626](https://bugs.python.org/issue?@action=redirect&bpo=40626): Register the h5 file extension under the MIME Type application/x-hdf5, following the HDF Group's recommendation for HDF5-formatted data files. Mark Schwab submitted the contributing patch.

[bpo-40105](https://bugs.python.org/issue?@action=redirect&bpo=40105): To prevent corruption, ZipFile now truncates files when a shorter comment is supplied under append (?a?) mode. Jan Mazur wrote the patch.

[bpo-41068](https://bugs.python.org/issue?@action=redirect&bpo=41068): Corrected reading of files bearing non-ASCII names from a ZIP archive right after they were written.

[bpo-41056](https://bugs.python.org/issue?@action=redirect&bpo=41056): Invalid file descriptor values can no longer be handed to os.fpathconf. (discovered by Coverity)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

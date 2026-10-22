# Python 3.5.0 alpha 1 / library / binary

[bpo-21075](https://bugs.python.org/issue?@action=redirect&bpo=21075): When binary mode is requested, fileinput.FileInput now pulls bytes from the standard stream. Sam Kimbrel wrote the patch.

[bpo-21396](https://bugs.python.org/issue?@action=redirect&bpo=21396): TextIOWrapper(…, write_through=True) no longer forces a flush() down to the binary stream beneath it. akira supplied the patch.

[bpo-21057](https://bugs.python.org/issue?@action=redirect&bpo=21057): The read() or read1() method of the underlying binary stream may now hand TextIOWrapper any arbitrary bytes-like object, for instance a memoryview. Nikolaus Rath authored the patch.

[bpo-21580](https://bugs.python.org/issue?@action=redirect&bpo=21580): bytes arguments handed to Tk are now processed correctly by Tkinter. Among other things, this permits building images straight from binary data.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

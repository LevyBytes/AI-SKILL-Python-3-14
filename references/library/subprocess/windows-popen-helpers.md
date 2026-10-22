# subprocess: Windows STARTUPINFO flags and standard handles

dwFlags

A bit field deciding whether particular `STARTUPINFO` attributes apply once the process opens a window.

```python
si = subprocess.STARTUPINFO()
si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW

```

 hStdInput

When `dwFlags` names `STARTF_USESTDHANDLES`, this attribute supplies the process's standard input handle. Absent `STARTF_USESTDHANDLES`, standard input defaults to the keyboard buffer.

 hStdOutput

When `dwFlags` names `STARTF_USESTDHANDLES`, this attribute supplies the process's standard output handle. Otherwise this attribute is disregarded and standard output defaults to the console window's buffer.

 hStdError

When `dwFlags` names `STARTF_USESTDHANDLES`, this attribute supplies the process's standard error handle. Otherwise this attribute is disregarded and standard error defaults to the console window's buffer.

 wShowWindow

When `dwFlags` names `STARTF_USESHOWWINDOW`, this attribute may take on any value valid for the `nCmdShow` parameter of the [ShowWindow](https://msdn.microsoft.com/en-us/library/ms633548(v=vs.85).aspx) function, with the single exception of `SW_SHOWDEFAULT`. Otherwise this attribute is disregarded.

For this attribute `SW_HIDE` is supplied. It comes into play whenever `Popen` runs with `shell=True`.

 lpAttributeList

A dictionary holding extra process-creation attributes as laid out in `STARTUPINFOEX`; see [UpdateProcThreadAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686880(v=vs.85).aspx).

Supported attributes:

**handle_list**

Sequence of handles slated for inheritance. When it is non-empty, *close_fds* has to be true.

For passing to the `Popen` constructor, the handles have to be made inheritable for the moment via [`os.set_handle_inheritable()`](https://docs.python.org/3.14/library/os.html#os.set_handle_inheritable); failing that, [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised carrying the Windows error `ERROR_INVALID_PARAMETER` (87).

Warning

Within a multithreaded process, take care not to leak inheritable-marked handles when you pair this feature with simultaneous calls to other process-creation functions that inherit every handle, like [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system). The same caution covers standard handle redirection, since it briefly produces inheritable handles.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](subprocess-startupinfo-class.md) · [Continue](windows-standard-handles-and-process-flags.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: subprocess.STARTUPINFO](subprocess-startupinfo-class.md) · [Owning module, declaration or section: Windows Popen Helpers](subprocess-startupinfo-class.md)

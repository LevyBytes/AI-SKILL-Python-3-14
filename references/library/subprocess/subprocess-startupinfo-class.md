# subprocess: `subprocess.STARTUPINFO`

### Windows Popen Helpers

The `STARTUPINFO` class together with the following constants exist only on Windows.

 *class *subprocess.STARTUPINFO(***, *dwFlags=0*, *hStdInput=None*, *hStdOutput=None*, *hStdError=None*, *wShowWindow=0*, *lpAttributeList=None*)

`Popen` creation makes use of partial support for the Windows [STARTUPINFO](https://msdn.microsoft.com/en-us/library/ms686331(v=vs.85).aspx) structure. You may set the attributes below by handing them in as keyword-only arguments.

Changed in version 3.7: Keyword-only argument support was added.

[Subject index](INDEX.md) · [Previous](popen-stdout-to-popen-returncode.md) · [Continue](windows-popen-helpers.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)

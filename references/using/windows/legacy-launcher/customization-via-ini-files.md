# 4.12.4.1. Customization via INI files

### 4.12.4. Customization

#### 4.12.4.1. Customization via INI files

The launcher consults two .ini files - `py.ini` inside the current user's application data directory (`%LOCALAPPDATA%` or `$env:LocalAppData`) and `py.ini` sitting in the same directory as the launcher. Those same .ini files apply both to the 'console' launcher (that is, py.exe) and to the 'windows' launcher (that is, pyw.exe).

Settings placed in the "application directory" take priority over the ones beside the executable, so that a user lacking write access to the .ini file next to the launcher can still override commands set in that global .ini file.

[Subject index](INDEX.md) · [Previous source section](arguments-in-shebang-lines.md) · [Following source section](customizing-default-python-versions.md)

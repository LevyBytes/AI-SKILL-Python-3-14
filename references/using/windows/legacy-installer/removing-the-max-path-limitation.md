# 4.11.2. Removing the MAX_PATH limitation

### 4.11.2. Removing the MAX_PATH limitation

For a long time, Windows capped path lengths at 260 characters. As a result, any path exceeding that length failed to resolve and produced errors.

Recent releases of Windows let you raise that cap to roughly 32,000 characters. To do so, your administrator has to turn on the "Enable Win32 long paths" group policy, or assign `LongPathsEnabled` the value `1` within the registry key `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`.

With this in place, the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function, the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module, and nearly all other path-handling features can take and hand back paths beyond 260 characters.

Once you adjust the setting above, nothing else needs to be configured.

Changed in version 3.6: Python gained the ability to handle long paths.

[Subject index](INDEX.md) · [Previous source section](installation-steps.md) · [Following source section](installing-without-ui.md)

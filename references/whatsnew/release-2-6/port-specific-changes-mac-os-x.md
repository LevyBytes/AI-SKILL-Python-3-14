# What’s New in Python 2.6 / Port-Specific Changes: Mac OS X

### Port-Specific Changes: Mac OS X

- While building a framework build of Python, you can now name the framework yourself by handing the `--with-framework-name=` option to the **configure** script.

- The `macfs` module is gone. That in turn forced the removal of the `macostools.touched()` function, since it leaned on the `macfs` module. ([bpo-1490190](https://bugs.python.org/issue?@action=redirect&bpo=1490190))

- A long list of other Mac OS modules has been deprecated and will disappear in Python 3.0: `_builtinSuites`, `aepack`, `aetools`, `aetypes`, `applesingle`, `appletrawmain`, `appletrunner`, `argvemulator`, `Audio_mac`, `autoGIL`, `Carbon`, `cfmfile`, `CodeWarrior`, `ColorPicker`, `EasyDialogs`, `Explorer`, `Finder`, `FrameWork`, `findertools`, `ic`, `icglue`, `icopen`, `macerrors`, `MacOS`, `macfs`, `macostools`, `macresource`, `MiniAEFrame`, `Nav`, `Netscape`, `OSATerminology`, `pimp`, `PixMapWrapper`, `StdSuites`, `SystemEvents`, `Terminal`, and `terminalcommand`.

### Port-Specific Changes: IRIX

[Subject index](INDEX.md) · [Previous source section](port-specific-changes-windows.md) · [Release/subject declaration](python-3-0.md) · [Following release/subject continuation](port-specific-changes-irix.md)

# 4.12.4.2. Customizing default Python versions

#### 4.12.4.2. Customizing default Python versions

In certain situations a version qualifier may be folded into a command to dictate which Python version that command employs. A version qualifier opens with a major version number and may optionally carry a period ('.') trailed by a minor version specifier. Beyond that, you can state whether a 32 or 64 bit build is wanted by appending "-32" or "-64".

For example, the shebang line `#!python` carries no version qualifier, whereas `#!python3` carries one that pins only a major version.

Where a command holds no version qualifiers, the environment variable `PY_PYTHON` can be set to name the default version qualifier. Absent that setting, the default is "3". The variable accepts any value valid on the command line, such as "3", "3.7", "3.7-32" or "3.7-64". (Bear in mind the "-64" option exists only with the launcher bundled with Python 3.7 or newer.)

Where no minor version qualifiers are present, the environment variable `PY_PYTHON{major}` (in which `{major}` is the current major version qualifier worked out as above) can be set to name the full version. If no such setting is found, the launcher walks through the installed Python versions and takes the newest minor release it finds for that major version - likely, though not certain, to be the most recently installed version in that family.

On 64-bit Windows holding both 32-bit and 64-bit builds of one (major.minor) Python version, the 64-bit build is always preferred. This holds for both 32-bit and 64-bit builds of the launcher - a 32-bit launcher will favour running a 64-bit Python install of the named version when one is around. That way the launcher's behavior can be foretold from nothing more than which versions sit on the PC, with no regard to the order they went on (that is, without knowing whether a 32 or 64-bit Python and its matching launcher were installed last). As noted above, an optional "-32" or "-64" suffix on a version specifier can shift this behaviour.

Examples:

- When no relevant options are set, the commands `python` and `python2` will run the most recent installed Python 2.x version, and the command `python3` will run the most recent installed Python 3.x.

- The command `python3.7` consults no options whatsoever, since the version is spelled out in full.

- If `PY_PYTHON=3`, both the commands `python` and `python3` will run the most recent installed Python 3 version.

- If `PY_PYTHON=3.7-32`, the command `python` will run the 32-bit build of 3.7, whereas the command `python3` will run the most recent installed Python (PY_PYTHON went entirely unconsidered, as a major version was given.)

- If `PY_PYTHON=3` and `PY_PYTHON3=3.7`, both the commands `python` and `python3` will run 3.7 specifically

Alongside environment variables, these same settings can be set up in the .INI file the launcher uses. That section of the INI file is named `[defaults]`, and the key name matches the environment variables stripped of the leading `PY_` prefix (and note that the INI file's key names are case insensitive.) Whatever an environment variable holds overrides what the INI file states.

For example:

- Setting `PY_PYTHON=3.7` amounts to the INI file containing:

```ini
[defaults]
python=3.7

```

- Setting `PY_PYTHON=3` and `PY_PYTHON3=3.7` amounts to the INI file containing:

```ini
[defaults]
python=3
python3=3.7

```

[Subject index](INDEX.md) · [Previous source section](customization-via-ini-files.md) · [Following source section](diagnostics.md)

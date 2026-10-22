# What's New In Python 3.11 / Windows `py.exe` launcher improvements

> (Contributed by Irit Katriel in [bpo-45607](https://bugs.python.org/issue?@action=redirect&bpo=45607). PEP written by Zac Hatfield-Dodds.)

### Windows `py.exe` launcher improvements

The version of the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) bundled with Python 3.11 received a major overhaul. It now understands company/tag syntax per [**PEP 514**](https://peps.python.org/pep-0514/) through the `-V:*<company>*/*<tag>*` argument, superseding the restrictive `-*<major>*.*<minor>*`. With it you can launch distributions beyond `PythonCore`, the build published at [python.org](https://www.python.org).

With `-V:` selectors you may drop either the company or the tag, though the search still spans every install. As an illustration, `-V:OtherPython/` picks the "best" tag recorded for `OtherPython`, whereas `-V:3.11` or `-V:/3.11` lands on the "best" distribution carrying tag `3.11`.

Pass the older `-*<major>*`, `-*<major>*.*<minor>*`, `-*<major>*-*<bitness>*` or `-*<major>*.*<minor>*-*<bitness>*` arguments and the prior conduct from earlier versions stays intact, with only `PythonCore` releases eligible. That said, the `-64` suffix has shifted to mean "not 32-bit" (rather than strictly x86-64), since several 64-bit platforms are now supported. A runtime is flagged 32-bit when its tag carries a `-32` suffix. Every Python release from 3.5 onward has embedded that marker in its 32-bit builds.

[Subject index](INDEX.md) · [Previous source section](pep-678-exceptions-can-be-enriched-with-notes.md) · [Next source section](new-features-related-to-type-hints.md) · [Release/subject declaration](summary-release-highlights.md)

# PYTHONHOME

PYTHONHOME

Relocate the standard Python libraries. By default, those libraries are looked for under `*prefix*/lib/python*version*` and `*exec_prefix*/lib/python*version*`, where `*prefix*` and `*exec_prefix*` are installation-dependent directories, each defaulting to `/usr/local`.

Whenever `PYTHONHOME` points at one directory, that value stands in for both `*prefix*` and `*exec_prefix*`. To assign distinct values to these, set `PYTHONHOME` to `*prefix*:*exec_prefix*`.

[Subject index](INDEX.md) · [Previous source section](environment-variables.md) · [Following source section](pythonpath.md)

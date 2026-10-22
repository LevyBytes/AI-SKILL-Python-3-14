# Python 3.5.0 release candidate 1 / idle / platform

[bpo-24745](https://bugs.python.org/issue?@action=redirect&bpo=24745): The default font for the Idle editor. Move off Courier onto the platform-sensitive TkFixedFont. Existing customized font choices should be unaffected. Should an issue crop up, open $HOME/.idlerc/config-main.cfg and delete any "`font*xxx*`" entries under [Editor Window]. Mark Roseman wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

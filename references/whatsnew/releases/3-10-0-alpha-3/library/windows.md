# Python 3.10.0 alpha 3 / library / windows

[bpo-39825](https://bugs.python.org/issue?@action=redirect&bpo=39825): Windows: Change `sysconfig.get_config_var('EXT_SUFFIX')` to the expected full `platform_tag.extension` format. It used to be hard-coded to `.pyd`; it is now consistent with `distutils.sysconfig` and yields something resembling `.cp38-win_amd64.pyd`. That aligns windows with how the other platforms behave.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

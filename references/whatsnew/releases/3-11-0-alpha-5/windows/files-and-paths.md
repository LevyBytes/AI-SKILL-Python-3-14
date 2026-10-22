# Python 3.11.0 alpha 5 / windows / files and paths

[bpo-46362](https://bugs.python.org/issue?@action=redirect&bpo=46362): os.path.abspath(?C:CON?) is corrected so it returns ?\.CON? rather than the unchanged path. The same regression affected every legacy DOS device, including COM1, LPT1, or NUL.

[bpo-44934](https://bugs.python.org/issue?@action=redirect&bpo=44934): The installer now presents a command-line-only choice to append the installation directory to the end of `PATH` instead of placing it at the front.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

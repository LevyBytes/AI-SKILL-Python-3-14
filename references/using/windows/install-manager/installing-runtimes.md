# 4.1.5. Installing runtimes

### 4.1.5. Installing runtimes

```none
$> py install [-s=|--source=<URL>] [-f|--force] [-u|--update] [--dry-run] [<TAG>...]

```

You can add new runtime versions through `py install`. You may give one or more tags, and the special tag `default` can pick the default. Installation does not accept ranges.

Through the `--source=<URL>` option you can override the online index used to fetch runtimes. It works with an offline index, as Offline installs demonstrates.

Giving `--force` disregards any cached files and deletes any current install so the named one replaces it.

Giving `--update` swaps existing installs for the newer version when one exists. Otherwise they stay as they are. Where `--update` is given with no tags, every install managed by the Python install manager gets updated where newer versions exist. Updates wipe out any changes made to the install, globally installed packages included, but virtual environments keep working.

Giving `--dry-run` produces output and logs while leaving all installs unchanged.

Giving `--refresh` updates every registration for installed runtimes. It recreates Start menu shortcuts, registry keys, and global aliases (for instance `python3.14.exe` or any installed scripts). These refresh on their own when any runtime is installed, but a manual refresh may be required after you install packages.

On top of the options above, the `--target` option pulls the runtime out into the named directory rather than performing a regular install. That is handy for embedding runtimes within larger applications. Unlike a normal install, `py` will not know about the extracted runtime, and no Start menu or other shortcuts get created. To start the runtime, run the main executable (usually `python.exe`) in the target directory directly.

```none
$> py install ... [-t=|--target=<PATH>] <TAG>

```

The `py exec` command installs the requested runtime when it is not already on hand. The `automatic_install` configuration (`PYTHON_MANAGER_AUTOMATIC_INSTALL`) governs this, and it is on by default. When no runtimes exist at all, every launch command will perform an automatic install if the configuration setting permits. This exists to give new users a smooth experience, but should generally not be leaned on in place of using the `py exec` command or explicit install commands.

[Subject index](INDEX.md) · [Previous source section](listing-runtimes.md) · [Following source section](offline-installs.md)

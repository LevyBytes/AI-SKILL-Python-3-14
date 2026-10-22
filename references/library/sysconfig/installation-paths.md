# sysconfig — Installation paths

### Installation paths

The installation scheme Python applies varies with both the platform and the chosen installation options. `sysconfig` keeps these schemes under unique identifiers derived from whatever [`os.name`](https://docs.python.org/3.14/library/os.html#os.name) hands back. Package installers lean on the schemes to figure out where files belong.

At present Python backs nine schemes:

- *posix_prefix*: the scheme for POSIX platforms such as Linux or macOS. It serves as the default whenever Python or one of its components gets installed.

- *posix_home*: the scheme for POSIX platforms once the *home* option comes into play. It lays out paths sitting beneath a particular home prefix.

- *posix_user*: the scheme for POSIX platforms once the *user* option comes into play. It lays out paths sitting beneath the user's home directory ([`site.USER_BASE`](https://docs.python.org/3.14/library/site.html#site.USER_BASE)).

- *posix_venv*: the scheme for [`Python virtual environments`](https://docs.python.org/3.14/library/venv.html#module-venv) on POSIX platforms; out of the box it matches *posix_prefix*.

- *nt*: the scheme for Windows. It serves as the default whenever Python or one of its components gets installed.

- *nt_user*: the scheme for Windows once the *user* option comes into play.

- *nt_venv*: the scheme for [`Python virtual environments`](https://docs.python.org/3.14/library/venv.html#module-venv) on Windows; out of the box it matches *nt*.

- *venv*: a scheme drawing its values from either *posix_venv* or *nt_venv*, according to whichever platform Python is executing on.

- *osx_framework_user*: the scheme for macOS once the *user* option comes into play.

A scheme is in turn built from a sequence of paths, each carrying its own unique identifier. At present Python relies on eight paths:

- *stdlib*: the directory holding the standard Python library files that carry no platform dependence.

- *platstdlib*: the directory holding the standard Python library files that are tied to the platform.

- *platlib*: the directory for files that are both site-specific and platform-specific.

- *purelib*: the directory for site-specific files with no platform dependence ('pure' Python).

- *include*: the directory for the Python C-API's platform-independent header files.

- *platinclude*: the directory for the Python C-API's platform-dependent header files.

- *scripts*: the directory holding script files.

- *data*: the directory holding data files.

[Subject index](INDEX.md) · [Previous](sysconfig-get-config-vars-to-sysconfig-get-config-var.md) · [Continue](user-scheme.md) · [Owning module, declaration or section: sysconfig](python-configuration-access-overview.md)

# 4.11.1. Installation steps

### 4.11.1. Installation steps

There are four Python 3.14 installers up for download — a pair each for the 32-bit and 64-bit flavors of the interpreter. The *web installer* starts as a tiny download and pulls down the components it needs on its own as it goes. The *offline installer* bundles in the pieces a default installation requires and only calls for an internet connection when you add optional features. See Installing without downloading for alternative approaches that skip downloading mid-install.

Once the installer launches, you can pick from one of two choices:

 (Figure: ../_images/win_installer.png)

If you select "Install Now":

- Administrator rights are *not* called for (the exceptions being when a system update for the C Runtime Library is needed, or when you set up the Python install manager for all users)

- Python will be installed into your user directory

- Whether the Python install manager gets installed follows the option shown at the foot of the first page

- The standard library, test suite, launcher and pip will be installed

- If selected, the install directory will be added to your `PATH`

- Shortcuts will only be visible for the current user

Choosing "Customize installation" gives you control over which features get installed, where the installation goes, and other options or post-install actions. Picking this option is also how you install debugging symbols or binaries.

For an all-users installation, choose "Customize installation". Under that path:

- You may be required to provide administrative credentials or approval

- Python will be installed into the Program Files directory

- The Python install manager will be installed into the Windows directory

- Optional features may be selected during installation

- The standard library can be pre-compiled to bytecode

- If selected, the install directory will be added to the system `PATH`

- Shortcuts are available for all users

[Subject index](INDEX.md) · [Previous source section](the-full-installer.md) · [Following source section](removing-the-max-path-limitation.md)

# 5.1.1. Installation steps

### 5.1. Using Python for macOS from `python.org`

### 5.1.1. Installation steps

For [current Python versions](https://www.python.org/downloads/) (those not already in `security` status), the release team builds a **Python for macOS** installer package with every new release. You can find a list of the available installers [here](https://www.python.org/downloads/macos/). Wherever you can, we suggest going with the latest supported Python version. The current installers ship a [universal2 binary](https://en.wikipedia.org/wiki/Universal_binary) build of Python that runs natively on every Mac (both Apple Silicon and Intel) supported across a broad span of macOS versions, which today generally starts at **macOS 10.15 Catalina** or later.

What you download is an ordinary macOS installer package file (`.pkg`). The release download page lists file integrity details (checksum, size, sigstore signature, and the like) for each file. To satisfy [macOS Gatekeeper requirements](https://support.apple.com/en-us/102445), the installer packages along with their contents are signed and notarized using `Python Software Foundation` Apple Developer ID certificates.

To perform a default installation, double-click the installer package file you downloaded. Doing so should bring up the standard macOS Installer app, presenting the first in a sequence of installer windows steps.

 (Figure: ../_images/mac_installer_01_introduction.png)

Pressing the **Continue** button surfaces this installer's **Read Me**. Alongside other important details, the **Read Me** records which Python version is about to be installed and the macOS versions it supports. Reading the whole file may require scrolling through it. By default, that **Read Me** also lands in `/Applications/Python 3.14/`, where it stays available to read anytime.

 (Figure: ../_images/mac_installer_02_readme.png)

Pressing **Continue** moves on to show the license covering Python plus the other bundled software. Before you can advance to the next step, you will have to **Agree** to those license terms. The license file gets installed too, so you can read it later.

 (Figure: ../_images/mac_installer_03_license.png)

Once the license terms have been accepted, the **Installation Type** display comes next. The standard collection of installation operations suits most uses.

 (Figure: ../_images/mac_installer_04_installation_type.png)

Pressing the **Customize** button lets you leave out or select particular package components of the installer. Click any package name and a description of what it installs appears. If you also want support for the optional free-threaded feature, consult Installing Free-threaded Binaries.

 (Figure: ../_images/mac_installer_05_custom_install.png)

Either way, pressing **Install** kicks off the install process by requesting permission to install new software. Because the installed Python is made available to every user of the Mac, you will need a macOS user name holding `Administrator` privilege.

Once the installation finishes, the **Summary** window shows up.

 (Figure: ../_images/mac_installer_06_summary.png)

In the `/Applications/Python 3.14/` window, double-click the **Install Certificates.command** icon or file to wrap up the installation.

 (Figure: ../_images/mac_installer_07_applications.png)

A short-lived **Terminal** shell window opens, which uses the freshly installed Python to fetch and install SSL root certificates for its own use.

 (Figure: ../_images/mac_installer_08_install_certificates.png)

The installation has finished once `Successfully installed certifi` and `update complete` show up in the terminal window. Go ahead and close both this terminal window and the installer window.

A default install will include:

- Within your `Applications` folder, a `Python 3.14` folder. Inside it sit **IDLE**, the development environment shipped as a standard part of official Python distributions, and **Python Launcher**, which manages double-clicked Python scripts coming from the macOS [Finder](https://support.apple.com/en-us/HT201732).

- A framework `/Library/Frameworks/Python.framework`, holding the Python executable along with its libraries. The installer appends this location to your shell path. Removing these three items is how you uninstall Python. Symlinks pointing at the Python executable get dropped into `/usr/local/bin/`.

Note

Newer macOS releases bundle a **python3** command at `/usr/bin/python3` that points to a generally older and partial version of Python that Apple supplies for the Apple development tools, **Xcode** or the **Command Line Tools for Xcode**, to use. Never alter or try to delete that installation: Apple controls it and it backs Apple-provided or third-party software. Should you decide to install a fresher Python version from `python.org`, your computer will hold two distinct but working Python installations that can live side by side. With its default options, the installer should make sure its **python3** runs in place of the system **python3**.

[Subject index](INDEX.md) · [Previous source section](using-python-on-macos.md) · [Following source section](how-to-run-a-python-script.md)

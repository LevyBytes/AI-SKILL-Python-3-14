# 4. Using Python on Windows

### 4. Using Python on Windows

The purpose of this document is to outline the Windows-specific behaviours that are worth knowing when you run Python on Microsoft Windows.

In contrast to most Unix systems and services, there is no system-supported Python installation shipped with Windows. Python instead comes from any of several distributors, one of which is the CPython team directly. Every Python distribution brings its own trade-offs, though staying consistent with the rest of your toolchain is usually worth aiming for. We suggest checking whether your current tools already supply Python before you adopt the approach outlined here.

The Python Install Manager is the way to get Python from the CPython team. As a self-contained tool, it exposes Python as global commands on your Windows system, hooks into the system, and keeps things current through updates. The Python Install Manager is available from [python.org/downloads](https://www.python.org/downloads/) or via the [Microsoft Store app](https://apps.microsoft.com/detail/9NQ7512CXL7T).

After the Python Install Manager is in place, you can run the global `python` command from any terminal to start your current latest Python release. That version can shift over time as you install or uninstall versions, and running `py list` reveals which one is current.

As a rule, we advise setting up a [virtual environment](https://docs.python.org/3.14/tutorial/venv.html#tut-venv) per project and running `<env>\Scripts\Activate` in your terminal to engage it. Doing so isolates projects from one another, keeps them stable over time, and makes sure that any extra commands contributed by packages show up in your session too. To build a virtual environment, use `python -m venv <env path>`.

Should the `python` or `py` commands appear not to function, consult the Troubleshooting section further down. Occasionally a few extra manual steps are needed to set up your PC.

Beyond the Python install manager, you can also acquire Python as NuGet packages. Refer to The nuget.org packages below to learn more about those packages.

The embeddable distros are stripped-down Python bundles intended for embedding inside larger applications. The Python install manager can install them. Refer to The embeddable package below to learn more about those packages.

[Subject index](INDEX.md) · [Following source section](installation.md)

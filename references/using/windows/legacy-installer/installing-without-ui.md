# 4.11.3. Installing without UI

### 4.11.3. Installing without UI

Every option offered by the installer UI is also available from the command line, so scripted installers can reproduce one installation across many machines with no user interaction. You can likewise apply these options without hiding the UI, simply to alter a few of the defaults.

The options below (turned up by running the installer with `/?`) may be handed to the installer:

| Name | Description |
| --- | --- |
| /passive | to display progress without requiring user interaction |
| /quiet | to install/uninstall without displaying any UI |
| /simple | to prevent user customization |
| /uninstall | to remove Python (without confirmation) |
| /layout [directory] | to pre-download all components |
| /log [filename] | to specify log files location |

Every remaining option goes in as `name=value`, where the value is normally `0` to switch a feature off, `1` to switch a feature on, or a path. The complete roster of available options appears below.

| Name | Description | Default |
| --- | --- | --- |
| InstallAllUsers | Perform a system-wide installation. | 0 |
| TargetDir | The installation directory | Selected based on InstallAllUsers |
| DefaultAllUsersTargetDir | The default installation directory for all-user installs | `%ProgramFiles%\Python X.Y` or `%ProgramFiles(x86)%\Python X.Y` |
| DefaultJustForMeTargetDir | The default install directory for just-for-me installs | `%LocalAppData%\Programs\Python\PythonXY` or `%LocalAppData%\Programs\Python\PythonXY-32` or `%LocalAppData%\Programs\Python\PythonXY-64` |
| DefaultCustomTargetDir | The default custom install directory displayed in the UI | (empty) |
| AssociateFiles | Create file associations if the launcher is also installed. | 1 |
| CompileAll | Compile all `.py` files to `.pyc`. | 0 |
| PrependPath | Prepend install and Scripts directories to `PATH` and add `.PY` to `PATHEXT` | 0 |
| AppendPath | Append install and Scripts directories to `PATH` and add `.PY` to `PATHEXT` | 0 |
| Shortcuts | Create shortcuts for the interpreter, documentation and IDLE if installed. | 1 |
| Include_doc | Install Python manual | 1 |
| Include_debug | Install debug binaries | 0 |
| Include_dev | Install developer headers and libraries. Leaving it out can render the install unusable. | 1 |
| Include_exe | Install `python.exe` and related files. Leaving it out can render the install unusable. | 1 |
| Include_launcher | Install Python install manager. | 1 |
| InstallLauncherAllUsers | Sets up the launcher across every user account. Depends as well on `Include_launcher` being 1 | 1 |
| Include_lib | Install standard library and extension modules. Leaving it out can render the install unusable. | 1 |
| Include_pip | Install bundled pip and setuptools | 1 |
| Include_symbols | Install debugging symbols (`*.pdb`) | 0 |
| Include_tcltk | Install Tcl/Tk support and IDLE | 1 |
| Include_test | Install standard library test suite | 1 |
| Include_tools | Install utility scripts | 1 |
| LauncherOnly | Only installs the launcher. This will override most other options. | 0 |
| SimpleInstall | Disable most install UI | 0 |
| SimpleInstallDescription | A custom message to display when the simplified install UI is used. | (empty) |

As an example, to quietly carry out a default, system-wide Python installation, the command below would work (run from an elevated command prompt):

```none
python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

```

To make it easy for users to drop in a personal copy of Python without the test suite, you might hand them a shortcut using the command below. It brings up a streamlined first page and blocks customization:

```none
python-3.9.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0
    SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."

```

(Bear in mind that leaving out the launcher also leaves out file associations, and is advisable only for per-user installs when a system-wide installation that did include the launcher is also present.)

You can also supply the options listed above through a file called `unattend.xml` placed beside the executable. That file holds a list of options together with their values. A value given as an attribute is turned into a number where possible. Values given as element text always stay strings. The example file below applies the same options as the earlier example:

```xml
<Options>
    <Option Name="InstallAllUsers" Value="no" />
    <Option Name="Include_launcher" Value="0" />
    <Option Name="Include_test" Value="no" />
    <Option Name="SimpleInstall" Value="yes" />
    <Option Name="SimpleInstallDescription">Just for me, no test suite</Option>
</Options>

```

[Subject index](INDEX.md) · [Previous source section](removing-the-max-path-limitation.md) · [Following source section](installing-without-downloading.md)

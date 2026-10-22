# 4.1.10. Advanced installation

### 4.1.10. Advanced installation

When an MSIX cannot be deployed -- for instance on certain legacy administrative distribution systems -- the python.org downloads page also offers an MSI. That MSI runs without any user interface and supports only per-machine installs to its default Program Files location. It tries to add this install path to the system `PATH` environment variable, though you should confirm that on your own setup.

Note

Among the Windows releases that CPython supports, Windows Server 2019 is the lone one lacking MSIX support. On Windows Server 2019, reach for the MSI instead.

Keep in mind that the MSI package ships without any bundled runtimes, so it does not fit offline deployments unless you also build an offline install index. Consult Offline installs and Administrative configuration to learn how to cover these cases.

The runtimes that the MSI installs are the same ones the MSIX installs, and every one of them is per-user only. Installing runtimes per-machine is not something the Python install manager supports. If you want to mimic a per-machine install, run `py install --target=<shared location>` as administrator and then layer in your own system-wide tweaks to `PATH`, the registry, or the Start menu.

If the MSIX has been installed yet its commands are absent from the `PATH` environment variable, you can locate them beneath `%LocalAppData%\Microsoft\WindowsApps\PythonSoftwareFoundation.PythonManager_3847v3x7pw1km` or `%LocalAppData%\Microsoft\WindowsApps\PythonSoftwareFoundation.PythonManager_qbz5n2kfra8p0`, the choice depending on whether the source was python.org or the Windows Store. Running the executable straight out of Program Files is discouraged.

The simplest way to install the Python install manager programmatically is via WinGet, which ships with every supported Windows release:

```powershell
$> winget install 9NQ7512CXL7T -e --accept-package-agreements --disable-interactivity

# Optionally run the configuration checker and accept all changes
$> py install --configure -y

```

If you want to fetch the Python install manager and set it up on a different machine, the WinGet command below pulls the needed files from the Store into your Downloads directory (append `-d <location>` to change where output lands). It also emits a YAML file that seems superfluous, since the fetched MSIX installs by launching it or by running the commands shown below.

```powershell
$> winget download 9NQ7512CXL7T -e --skip-license --accept-package-agreements --accept-source-agreements

```

For installing or removing an MSIX programmatically with PowerShell alone, the recommended approach is the [Add-AppxPackage](https://learn.microsoft.com/powershell/module/appx/add-appxpackage) and [Remove-AppxPackage](https://learn.microsoft.com/powershell/module/appx/remove-appxpackage) PowerShell cmdlets:

```powershell
$> Add-AppxPackage C:\Downloads\python-manager-25.0.msix
...
$> Get-AppxPackage PythonSoftwareFoundation.PythonManager | Remove-AppxPackage

```

Handing the AppInstaller file to the Add-AppxPackage command lets Windows fetch and install the most recent release. That path installs from the MSIX hosted on python.org and is advised only when Store installation (whether interactive or through WinGet) is unavailable.

```powershell
$> Add-AppxPackage -AppInstallerFile https://www.python.org/ftp/python/pymanager/pymanager.appinstaller

```

Additional tools and APIs exist for provisioning an MSIX package across every user on a machine, but Python treats this as unsupported. Worth exploring are the PowerShell [Add-AppxProvisionedPackage](https://learn.microsoft.com/powershell/module/dism/add-appxprovisionedpackage) cmdlet, the native Windows [PackageManager](https://learn.microsoft.com/uwp/api/windows.management.deployment.packagemanager) class, or whatever documentation and support your deployment tool offers.

No matter which install route you pick, each user must still install their own copy of Python proper, because nothing can trigger those installs unless a user is logged in. With the MSIX in place, the newest Python build becomes available for every user to install without any network connection.

Bear in mind that the MSIX you download from the Store differs subtly from the one on the Python website, and the two cannot coexist. Whenever you can, prefer the WinGet commands above to grab the package from the Store, which lowers the chance of creating clashing installs. The Python install manager carries no licensing limits that would block using the Store package this way.

[Subject index](INDEX.md) · [Previous source section](shebang-lines.md) · [Following source section](administrative-configuration.md)

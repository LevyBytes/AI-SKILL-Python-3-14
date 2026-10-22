# 4.3. The nuget.org packages

### 4.3. The nuget.org packages

Added in version 3.5.2.

The nuget.org package provides a trimmed-down Python environment meant for continuous integration and build systems lacking a system-wide Python install. Although nuget is “the package manager for .NET”, it serves packages of build-time tools perfectly well too.

Head to [nuget.org](https://www.nuget.org/) for the freshest guidance on working with nuget. The following is a summary that covers what Python developers need.

You can download the `nuget.exe` command line tool straight from `https://aka.ms/nugetclidl`, for instance with curl or PowerShell. Using that tool, you install the newest Python for 64-bit or 32-bit machines with:

```none
nuget.exe install python -ExcludeVersion -OutputDirectory .
nuget.exe install pythonx86 -ExcludeVersion -OutputDirectory .

```

For a specific version, tack on a `-Version 3.x.y`. You may point the output directory somewhere other than `.`, and the package gets installed into a subdirectory. That subdirectory defaults to the same name as the package, and without the `-ExcludeVersion` option the name will carry the exact version installed. Within the subdirectory sits a `tools` directory holding the Python installation:

```doscon
# Without -ExcludeVersion
> .\python.3.5.2\tools\python.exe -V
Python 3.5.2

# With -ExcludeVersion
> .\python\tools\python.exe -V
Python 3.5.2

```

As a rule, nuget packages cannot be upgraded; install newer versions side-by-side and refer to them by their full path. Otherwise, delete the package directory by hand and install it once more. Many CI systems handle this on their own whenever they do not retain files across builds.

Next to the `tools` directory sits a `build\native` directory. It holds a MSBuild properties file `python.props` usable in a C++ project to reference the Python install. Bringing in the settings makes your build automatically pick up the headers and import libraries.

On nuget.org, the package information pages live at [www.nuget.org/packages/python](https://www.nuget.org/packages/python) for the 64-bit build, [www.nuget.org/packages/pythonx86](https://www.nuget.org/packages/pythonx86) for the 32-bit build, and [www.nuget.org/packages/pythonarm64](https://www.nuget.org/packages/pythonarm64) for the ARM64 build

[Subject index](INDEX.md) · [Previous source section](embedding-python.md) · [Following source section](free-threaded-packages.md)

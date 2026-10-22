# What’s New in Python 2.3 / Port-Specific Changes — fcntl

### Port-Specific Changes

A port to IBM's OS/2 built on the EMX runtime environment was merged into the principal Python source tree. EMX provides a POSIX emulation layer atop the OS/2 system APIs. The EMX Python port aims to cover every POSIX-like capability the EMX runtime exposes, and largely manages it; `fork()` and [`fcntl()`](https://docs.python.org/3.14/library/fcntl.html#module-fcntl) are constrained by the limits of the underlying emulation layer. The standard OS/2 port, which builds with IBM's Visual Age compiler, picked up case-sensitive import semantics as well during the integration of the EMX port into CVS. (Contributed by Andrew MacIntyre.)

On MacOS, the majority of toolbox modules have been weaklinked to enhance backward compatibility. As a result, modules will no longer fail to load when a single routine is absent on the current OS version. Instead, an exception is raised when the missing routine is called. (Contributed by Jack Jansen.)

The RPM spec files located in the `Misc/RPM/` directory of the Python source distribution were brought up to date for 2.3. (Contributed by Sean Reifschneider.)

Additional new platforms now carried by Python include AtheOS ([http://www.atheos.cx/](http://www.atheos.cx/)), GNU/Hurd, and OpenVMS.

[Subject index](INDEX.md) · [Previous source section](build-and-c-api-changes.md) · [Next source section](other-changes-and-fixes.md) · [Release/subject declaration](standard-set-type.md)

# Python 3.7.0 alpha 1 / build / build and platforms

[bpo-31354](https://bugs.python.org/issue?@action=redirect&bpo=31354): Permit `--with-lto` on every build, rather than only with `make profile-opt`.

[bpo-30687](https://bugs.python.org/issue?@action=redirect&bpo=30687): On Windows, find msbuild.exe at build time in place of vcvarsall.bat

[bpo-29941](https://bugs.python.org/issue?@action=redirect&bpo=29941): Provide a `--with-assertions` configure flag that turns on C `assert()` checks explicitly. It is off by default. Note that `--with-pydebug` automatically enables `--with-assertions`.

[bpo-29243](https://bugs.python.org/issue?@action=redirect&bpo=29243): Avoid needless rebuilding of Python under `make test`, `make install` and certain other make targets when the build was configured with `--enable-optimizations`.

[bpo-29572](https://bugs.python.org/issue?@action=redirect&bpo=29572): Move the Windows build and OS X installers onto OpenSSL 1.0.2k.

[bpo-29080](https://bugs.python.org/issue?@action=redirect&bpo=29080): Eliminates the hard dependency on hg.exe within PCBuild/build.bat

[bpo-28762](https://bugs.python.org/issue?@action=redirect&bpo=28762): Although lockf() exists at Android API level 24, the F_LOCK macro remains undefined within android-ndk-r13.

[bpo-28849](https://bugs.python.org/issue?@action=redirect&bpo=28849): Refrain from defining sys.implementation._multiarch when on Android.

[bpo-28208](https://bugs.python.org/issue?@action=redirect&bpo=28208): Move the Windows build and OS X installers onto SQLite 3.14.2.

[bpo-28248](https://bugs.python.org/issue?@action=redirect&bpo=28248): Move the Windows build and OS X installers onto OpenSSL 1.0.2j.

[bpo-21085](https://bugs.python.org/issue?@action=redirect&bpo=21085): Add a configure probe for siginfo_t.si_band, something Cygwin lacks. Masayuki Yamamoto wrote the patch, which Erik Bray reviewed and rebased.

[bpo-28676](https://bugs.python.org/issue?@action=redirect&bpo=28676): Stop the missing ‘getentropy’ declaration warning from appearing on macOS. Gareth Rees supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

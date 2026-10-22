# Python 3.7.0 alpha 3 / build / build and platforms

[bpo-28762](https://bugs.python.org/issue?@action=redirect&bpo=28762): The latest commit was reverted, since the F_LOCK macro comes from Android Unified Headers.

[bpo-29040](https://bugs.python.org/issue?@action=redirect&bpo=29040): Building Android with Unified Headers is now supported. android-ndk-r14 is the earliest NDK release that supports Unified Headers.

[bpo-31957](https://bugs.python.org/issue?@action=redirect&bpo=31957): Corrects detection of the Windows SDK version during Windows builds.

[bpo-31934](https://bugs.python.org/issue?@action=redirect&bpo=31934): Halt the build whenever it runs against a source tree that is not clean.

[bpo-28791](https://bugs.python.org/issue?@action=redirect&bpo=28791): Move the Windows builds onto SQLite 3.21.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

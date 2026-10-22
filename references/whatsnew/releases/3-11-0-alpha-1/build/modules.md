# Python 3.11.0 alpha 1 / build / modules

[bpo-45020](https://bugs.python.org/issue?@action=redirect&bpo=45020): Freeze the stdlib modules that get imported while the interpreter starts up. Doing so yields a meaningful speedup at startup. Should it be needed, fall back on the earlier "-X frozen_modules=off" commandline option to compel loading of the source modules.

[bpo-45188](https://bugs.python.org/issue?@action=redirect&bpo=45188): On Windows, frozen modules are now regenerated as the very first build step. Earlier this regeneration happened further along, forcing a restart whenever any modules had been altered.

[bpo-45019](https://bugs.python.org/issue?@action=redirect&bpo=45019): Produce the lines for frozen modules across the relevant files. Previously every one of those files needed manual editing. The change simplifies adding to and modifying the frozen modules.

[bpo-41282](https://bugs.python.org/issue?@action=redirect&bpo=41282): Repair a broken `make install` that left standard library extension modules being needlessly and wrongly rebuilt throughout cpython's install phase.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

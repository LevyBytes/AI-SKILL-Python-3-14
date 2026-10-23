# zipapp - Caveats

### Caveats

When your application relies on a package carrying a C extension, that package can’t run straight out of a zip file (an OS limitation, since the OS loader needs executable code sitting in the filesystem to load it). Here you might leave that dependency out of the zipfile and either insist users have it installed, or ship it beside your zipfile while adding code to your `__main__.py` that puts the directory of the unzipped module onto `sys.path`. Going that route, you’ll have to be sure to ship suitable binaries for your target architecture(s) (and perhaps choose the right one to append to `sys.path` at runtime, depending on the user’s machine).

[Subject index](INDEX.md) · [Previous](creating-standalone-applications-with-zipapp.md) · [Continue](the-python-zip-application-archive-format.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)

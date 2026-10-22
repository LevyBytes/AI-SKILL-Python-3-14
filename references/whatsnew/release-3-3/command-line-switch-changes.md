# What's New In Python 3.3 / Command Line Switch Changes

### Command Line Switch Changes

- Both the -Q command-line flag and its associated bits and pieces are gone. Code that inspects sys.flags.division_warning will have to be revised.

([bpo-10998](https://bugs.python.org/issue?@action=redirect&bpo=10998), contributed by Éric Araujo.)

- Launch **python** with [`-S`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-S) and `import site` will from now on skip adding site-specific paths to the module search paths — something it used to do in earlier releases.

([bpo-11591](https://bugs.python.org/issue?@action=redirect&bpo=11591), contributed by Carl Meyer with editions by Éric Araujo.)

[Subject index](INDEX.md) · [Previous source section](building-c-extensions.md) · [Release/subject declaration](summary-release-highlights.md)

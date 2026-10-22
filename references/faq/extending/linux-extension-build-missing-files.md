# I want to compile a Python module on my Linux system, but some files are missing. Why?

### I want to compile a Python module on my Linux system, but some files are missing. Why?

The majority of prepackaged Python distributions leave out certain files needed to compile Python extensions.

On Red Hat, pull in the python3-devel RPM, which carries the files you're missing.

On Debian, the command is `apt-get install python3-dev`.

[Subject index](INDEX.md)

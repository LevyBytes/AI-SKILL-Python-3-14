# I added a module using the Setup file and the make fails; why?

### I added a module using the Setup file and the make fails; why?

A trailing newline is mandatory at the close of Setup; without one, the build collapses. (Patching this would call for some unsightly shell-script trickery, and the bug is trivial enough that the bother hardly seems justified.)

[Subject index](INDEX.md)

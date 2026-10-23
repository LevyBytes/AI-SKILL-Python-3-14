# zipapp - Specifying the Interpreter

### Specifying the Interpreter

Keep in mind that once you pin an interpreter and then hand your application archive around, you have to be sure that interpreter is portable. The Windows Python launcher copes with most ordinary POSIX `#!` lines, yet further wrinkles deserve thought:

- Should you go with “/usr/bin/env python” (or some other spelling of the “python” command, like “/usr/bin/python”), remember your users might default to either Python 2 or Python 3, so write code that runs on both.

- Should you pin an exact version, say “/usr/bin/env python3”, your application won’t run for anyone lacking that version. (That might be precisely what you intend if your code isn’t Python 2 compatible.)

- Nothing lets you express “python X.Y or newer”, so tread carefully with a fixed version such as “/usr/bin/env python3.4”, since you’d have to edit your shebang line for, say, Python 3.5 users.

As a rule, reach for “/usr/bin/env python2” or “/usr/bin/env python3”, according to whether your code targets Python 2 or 3.

[Subject index](INDEX.md) · [Previous](examples.md) · [Continue](creating-standalone-applications-with-zipapp.md) · [Owning module, declaration or section: zipapp](zipapp-manage-executable-python-zip-archives.md)

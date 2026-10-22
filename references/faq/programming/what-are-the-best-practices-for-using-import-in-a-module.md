# What are the “best practices” for using import in a module?

### What are the “best practices” for using import in a module?

As a rule, steer clear of `from modulename import *`. It pollutes the importer's namespace and makes it considerably harder for linters to flag undefined names.

Put module imports at the top of a file. That makes plain which other modules your code depends on and removes any doubt about whether a module name is in scope. Writing one import per line makes adding and removing module imports straightforward, whereas packing several imports onto one line conserves screen space.

A sound practice is to import modules in this sequence:

1.

standard library modules – such as [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys), [`os`](https://docs.python.org/3.14/library/os.html#module-os), [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse), [`re`](https://docs.python.org/3.14/library/re.html#module-re)

2.

third-party library modules (whatever lives in the site-packages directory of Python) – for instance [dateutil](https://pypi.org/project/dateutil/), [requests](https://pypi.org/project/requests/), [tzdata](https://pypi.org/project/tzdata/)

3.

locally developed modules

Occasionally you must relocate imports into a function or class to sidestep trouble with circular imports. Gordon McMillan says:

>

So long as each module relies on the “import &lt;module&gt;” style of import, circular imports work fine. The breakdown comes when the 2nd module tries to pull a name straight out of the first (“from module import name”) with that import sitting at the top level. The reason: the names in the 1st aren’t ready yet, since the first module is in the middle of importing the 2nd.

Here, when only one function within the second module uses it, that import can simply be relocated inside the function. By the point the import runs, the first module will be done initializing, allowing the second module to perform its import.

Pulling imports out of the top level of code may also be required if certain modules are platform-specific. In that situation, importing every module at the top of the file might not even be feasible. Here, a good route is to import the right modules in the matching platform-specific code.

Move imports into a local scope, like the inside of a function definition, only when you need it to resolve a problem such as dodging a circular import or you're attempting to cut a module's initialization time. The technique pays off especially when many of the imports turn out to be unnecessary depending on the way the program runs. You might also want to relocate imports into a function when the modules see use only within that function. Bear in mind that loading a module the first time can be costly owing to the module's one-time initialization, yet loading a module repeatedly is essentially free, costing just a few dictionary lookups. Even after the module name has left scope, the module is likely still reachable in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules).

[Subject index](INDEX.md)

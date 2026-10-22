# What’s New in Python 2.1 / PEP 241: Metadata in Python Packages

As an initial modest move toward solving this, any Python software bundled through the Distutils **sdist** command now ships a file called `PKG-INFO` that records details about the package — its name, version, author, and so on (what cataloguers would call metadata). The complete roster of fields allowed in the `PKG-INFO` file is laid out in [**PEP 241**](https://peps.python.org/pep-0241/). Once people start bundling their software with Python 2.1, an ever-growing share of packages will carry metadata, which opens the door to building automated cataloguing systems and trying them out. Armed with that experience, it may eventually prove feasible to design a genuinely good catalog and then bake support for it into Python 2.2. The Distutils **sdist** and **bdist_*** commands, for instance, might grow an `upload` option that ships your package off to a catalog server on its own.

Even without Python 2.1, you can begin producing packages that bundle `PKG-INFO`, because a fresh Distutils release is being put out for people on older Python versions too. The changes spelled out in [**PEP 241**](https://peps.python.org/pep-0241/), together with assorted bugfixes and improvements, ride along in Distutils version 1.0.2. You can grab it from the Distutils SIG at [https://www.python.org/community/sigs/current/distutils-sig/](https://www.python.org/community/sigs/current/distutils-sig/).

See also

[**PEP 241**](https://peps.python.org/pep-0241/) - Metadata for Python Software Packages

Written and implemented by A.M. Kuchling.

[**PEP 243**](https://peps.python.org/pep-0243/) - Module Repository Upload Mechanism

Authored by Sean Reifschneider, this draft PEP sets out a suggested way to push Python packages up to a central server.

### PEP 241: Metadata in Python Packages

A frequent gripe among Python users is the absence of one unified catalog covering every Python module out there. The largest such catalog of Python modules was the Vaults of Parnassus, run by T. Middleton at `www.vex.net/parnassus/` (retired in February 2009, [available in the Internet Archive Wayback Machine](https://web.archive.org/web/20090130140102/http://www.vex.net/parnassus/)); however, registering your software with the Vaults was optional, so a great many people simply never did.

[Subject index](INDEX.md) · [Next source section](new-and-improved-modules.md) · [Release/subject declaration](introduction.md) · [Previous source section](pep-208-new-coercion-model.md)

# What's New In Python 3.4 / Summary

Single-dispatch generic functions in [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) ([**PEP 443**](https://peps.python.org/pep-0443/)).

- New [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) protocol 4 ([**PEP 3154**](https://peps.python.org/pep-3154/)).

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) gains a setting that sidesteps os.fork under Unix ([bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)).

- [`email`](https://docs.python.org/3.14/library/email.html#module-email) gains a fresh submodule, [`contentmanager`](https://docs.python.org/3.14/library/email.contentmanager.html#module-email.contentmanager), plus a fresh [`Message`](https://docs.python.org/3.14/library/email.compat32-message.html#email.message.Message) subclass ([`EmailMessage`](https://docs.python.org/3.14/library/email.message.html#email.message.EmailMessage)), together making MIME work easier ([bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891)).

- The [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) and [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) modules can now correctly introspect a far broader range of callable objects, sharpening what the Python [`help()`](https://docs.python.org/3.14/library/functions.html#help) system prints.

- The [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) module API has been declared stable

Security improvements:

- Secure and interchangeable hash algorithm ([**PEP 456**](https://peps.python.org/pep-0456/)).

- Render freshly created file descriptors non-inheritable ([**PEP 446**](https://peps.python.org/pep-0446/)) so that descriptors don't leak into child processes.

- New command line option for isolated mode, ([bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)).

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) gains a setting that sidesteps os.fork under Unix. The *spawn* and *forkserver* approaches tighten security since they keep data from being shared into child processes.

- On Windows, [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) child processes stop inheriting every inheritable handle of the parent and pick up just the required ones.

- A new [`hashlib.pbkdf2_hmac()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.pbkdf2_hmac) function provides the [PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2).

- TLSv1.1 and TLSv1.2 support for [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl).

- Retrieving certificates from the Windows system cert store support for [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl).

- Server-side SNI (Server Name Indication) support for [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl).

- The [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) class has a lot of improvements.

- Every standard-library module offering SSL can now perform server certificate verification, covering hostname matching (`ssl.match_hostname()`) plus CRLs (Certificate Revocation lists, see [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext.load_verify_locations)).

CPython implementation improvements:

- Safe object finalization ([**PEP 442**](https://peps.python.org/pep-0442/)).

- Thanks to [**PEP 442**](https://peps.python.org/pep-0442/), most of the time a module's globals will no longer be reset to None while finalization runs ([bpo-18214](https://bugs.python.org/issue?@action=redirect&bpo=18214)).

- Configurable memory allocators ([**PEP 445**](https://peps.python.org/pep-0445/)).

-

[Subject index](INDEX.md) · [Previous source section](release-highlights.md) · [Next source section](summary-release-highlights-argument-clinic-pep-436.md) · [Release/subject declaration](release-highlights.md)

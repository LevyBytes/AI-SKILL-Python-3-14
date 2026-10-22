# What’s New in Python 2.7 / PEP 493: HTTPS verification migration tools for Python 2.7

### PEP 493: HTTPS verification migration tools for Python 2.7

[**PEP 493**](https://peps.python.org/pep-0493/) supplies extra migration tooling to enable a more gradual infrastructure-upgrade path for setups whose applications and services lean on the formerly lenient handling of server certificates when opening client HTTPS connections. The Python 2.7.12 release brought in these additions.

The intent behind these tools is situations where the affected applications and services cannot be edited to pass a more permissive SSL context explicitly as the connection is opened.

Where applications and services cannot be touched in any way, the new `PYTHONHTTPSVERIFY` environment variable can be set to `0` to roll a whole Python process back to the lenient default seen in Python 2.7.8 and before.

Where the connection-setup code is off-limits but the application as a whole is editable, the new `ssl._https_verify_certificates()` function lets you tune the default behaviour while running.

[Subject index](INDEX.md) · [Previous source section](pep476-default-http-certificate-verification.md) · [Next source section](new-make-regen-all-build-target.md) · [Release/subject declaration](the-future-for-python-2-x.md)

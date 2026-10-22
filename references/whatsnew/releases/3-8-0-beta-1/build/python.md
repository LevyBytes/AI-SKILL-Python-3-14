# Python 3.8.0 beta 1 / build / python

[bpo-36721](https://bugs.python.org/issue?@action=redirect&bpo=36721): When embedding Python inside an application, you must now hand a fresh `--embed` option to `python3-config --libs --embed` in order to obtain `-lpython3.8` (linking the application against libpython). For compatibility across both 3.8 and older releases, attempt `python3-config --libs --embed` first and fall back to `python3-config --libs` (lacking `--embed`) should the earlier command fail.

A pkg-config `python-3.8-embed` module is added for embedding Python inside an application: `pkg-config python-3.8-embed --libs` pulls in `-lpython3.8`. For compatibility across both 3.8 and older releases, attempt `pkg-config python-X.Y-embed --libs` first and fall back to `pkg-config python-X.Y --libs` (lacking `--embed`) should the earlier command fail (substitute the Python version for `X.Y`).

Conversely, `pkg-config python3.8 --libs` no longer carries `-lpython3.8`. C extensions must avoid linking against libpython (Android excepted, a case the script handles); this break in backward compatibility is deliberate.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

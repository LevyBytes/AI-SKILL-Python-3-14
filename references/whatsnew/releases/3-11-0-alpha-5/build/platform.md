# Python 3.11.0 alpha 5 / build / platform

[bpo-45569](https://bugs.python.org/issue?@action=redirect&bpo=45569): Builds now default to 30-bit digits for Python integers. Formerly the platform decided between 15-bit or 30-bit digits. You can still pick 15-bit digits through the `--enable-big-digits=15` option passed to the `configure` script, or by defining `PYLONG_BITS_IN_DIGIT` inside `pyconfig.h`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

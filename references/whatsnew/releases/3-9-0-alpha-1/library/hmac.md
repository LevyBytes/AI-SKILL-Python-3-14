# Python 3.9.0 alpha 1 / library / hmac

[bpo-33604](https://bugs.python.org/issue?@action=redirect&bpo=33604): When the digestmod parameter (mandatory since 3.8) is left out, `hmac.new` and `hmac.HMAC` were fixed to throw TypeError rather than ValueError. The hmac module's documentation and docstrings were also made clearer.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

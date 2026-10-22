# Python 3.7.0 alpha 1 / library / gettext

[bpo-28692](https://bugs.python.org/issue?@action=redirect&bpo=28692): Passing a non-integer value to choose a plural form within gettext now carries a deprecation.

[bpo-28563](https://bugs.python.org/issue?@action=redirect&bpo=28563): Closed a possible DoS plus arbitrary code execution path during plural-form selection handling inside the gettext module. Its expression parser now matches the precise syntax that GNU gettext accepts.

[bpo-29755](https://bugs.python.org/issue?@action=redirect&bpo=29755): The lgettext() family within the gettext module was corrected; these calls now consistently hand back bytes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.7.0 alpha 1 / library / compression

[bpo-28449](https://bugs.python.org/issue?@action=redirect&bpo=28449): Invoking tarfile.open() under mode “r” or “r:” now attempts to open a tar file assuming compression before falling back to opening it without. Without that, it carried a 50% chance of failing whenever ignore_zeros=True.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

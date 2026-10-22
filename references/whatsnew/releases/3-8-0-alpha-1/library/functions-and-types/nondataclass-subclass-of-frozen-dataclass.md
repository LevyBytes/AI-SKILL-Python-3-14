# Python 3.8.0 alpha 1 / library / non dataclass derives frozen dataclass permit attributes derived class

[bpo-32953](https://bugs.python.org/issue?@action=redirect&bpo=32953): When a non-dataclass derives from a frozen dataclass, permit attributes on the derived class. Only the frozen dataclass's attributes remain unassignable. Insist that every dataclass across a hierarchy be uniformly frozen or uniformly non-frozen.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)

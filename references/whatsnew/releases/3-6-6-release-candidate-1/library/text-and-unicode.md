# Python 3.6.6 release candidate 1 / library / text and unicode

[bpo-11874](https://bugs.python.org/issue?@action=redirect&bpo=11874): Adopted a stronger regex for splitting usage into wrappable pieces. This sidesteps spurious assertion errors arising from custom metavar strings.

[bpo-30877](https://bugs.python.org/issue?@action=redirect&bpo=30877): Repaired a defect in the Python JSON decoder implementation that kept the parsed-string cache from being emptied once decoding completed. The work builds on a patch from c-fos.

[bpo-33422](https://bugs.python.org/issue?@action=redirect&bpo=33422): Stopped trailing quotation marks from vanishing when byte or string literals are looked up in pydoc. Andrés Delfino sent the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

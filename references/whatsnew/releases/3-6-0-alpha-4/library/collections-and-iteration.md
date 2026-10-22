# Python 3.6.0 alpha 4 / library / collections and iteration

[bpo-25958](https://bugs.python.org/issue?@action=redirect&bpo=25958): Allow "anti-registration" of the special methods belonging to assorted ABCs, such as __hash__, __iter__ or __len__. Each of these (and several others) may be set to None in an implementation class, and the result is as though the method were never defined. (That mechanism previously applied solely to __hash__, in order to render mutable classes unhashable.) Andrew Barnert and Ivan Levkivskyi contributed the code.

[bpo-26750](https://bugs.python.org/issue?@action=redirect&bpo=26750): unittest.mock.create_autospec() now behaves correctly for subclasses of property() and other data descriptors. The never publicly used, never documented unittest.mock.DescriptorTypes tuple is removed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

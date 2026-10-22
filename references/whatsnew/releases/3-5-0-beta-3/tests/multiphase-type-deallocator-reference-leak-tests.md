# Python 3.5.0 beta 3 / tests / dodge reference leaks show up tp dealloc paired pytype fromspec testmultiphase

[bpo-24373](https://bugs.python.org/issue?@action=redirect&bpo=24373): To dodge the reference leaks that show up when tp_dealloc is paired with PyType_FromSpec, _testmultiphase and xxlimited now rely on tp_traverse together with tp_finalize (consult [bpo-16690](https://bugs.python.org/issue?@action=redirect&bpo=16690) for the specifics)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

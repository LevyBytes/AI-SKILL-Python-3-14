# multiprocessing: `multiprocessing.managers.Namespace`

*class *multiprocessing.managers.Namespace

A type that is able to register with `SyncManager`.

A namespace object exposes no public methods, yet it does carry writable attributes. Its representation displays the values of those attributes.

That said, when a proxy for a namespace object is in play, an attribute starting with `'_'` belongs to the proxy rather than to the referent:

```pycon
>>> mp_context = multiprocessing.get_context('spawn')
>>> manager = mp_context.Manager()
>>> Global = manager.Namespace()
>>> Global.x = 10
>>> Global.y = 'hello'
>>> Global._z = 12.3    # this is an attribute of the proxy
>>> print(Global)
Namespace(x=10, y='hello')

```

[Subject index](INDEX.md) · [Previous](sync-manager-shared-object-factories.md) · [Continue](customized-managers.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: Managers](multiprocessing-manager.md)

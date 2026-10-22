# pickle — Persistence of External Objects — Section introduction and initial examples

### Persistence of External Objects

For the sake of object persistence, the `pickle` module lets you reference an object sitting outside the pickled data stream. Such references rely on a persistent ID, which ought to be a string of alphanumeric characters (for protocol 0) [5], or else just any arbitrary object (for any newer protocol).

The `pickle` module itself does not define how those persistent IDs get resolved; it hands that resolution off to the user-defined methods on the pickler and unpickler, `persistent_id()` and `persistent_load()` respectively.

To pickle objects carrying an external persistent ID, the pickler needs a custom `persistent_id()` method that takes an object as its argument and returns either `None` or that object's persistent ID. Returning `None` makes the pickler pickle the object the ordinary way. Returning a persistent ID string makes the pickler pickle that object together with a marker, so the unpickler recognizes it as a persistent ID.

For external objects to be unpickled, the unpickler needs a custom `persistent_load()` method that accepts a persistent ID object and hands back the object it refers to.

Below is a thorough example showing how a persistent ID can serve to pickle external objects by reference.

[Subject index](INDEX.md) · [Previous](object-reduce-to-object-reduce-ex.md) · [Continue](persistence-of-external-objects-code-example-import-pickle.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md)

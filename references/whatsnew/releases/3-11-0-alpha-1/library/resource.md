# Python 3.11.0 alpha 1 / library / resource

[bpo-44771](https://bugs.python.org/issue?@action=redirect&bpo=44771): Added the `importlib.simple` module, which provides adapters bridging a low-level resources reader interface across to a `TraversableResources` interface. The legacy API (`path`, `contents`, ?) is now backed wholly by the `.files()` API, with a compatibility shim furnished for resource loaders that lack that capability. This reaches feature parity with `importlib_resources` 5.2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

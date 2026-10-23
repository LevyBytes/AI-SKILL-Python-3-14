# unittest.mock - Patching Descriptors and Proxy Objects

### Patching Descriptors and Proxy Objects

Both patch and patch.object faithfully patch and restore descriptors — class methods, static methods, and properties. Apply these patches on the *class*, not on an instance. They function as well with *some* objects that proxy attribute access, like the [django settings object](https://web.archive.org/web/20200603181648/http://www.voidspace.org.uk/python/weblog/arch_d7_2010_12_04.shtml#e1198).

[Subject index](INDEX.md) · [Previous](where-to-patch.md) · [Continue](magic-method-mocking-overview.md) · [Owning module, declaration or section: unittest.mock](unittest-mock-mock-object-library.md)

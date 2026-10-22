# `Enum` member type

### `Enum` member type

Each enum member is an instance of its enum class, and the usual way to reach one is via `EnumClass.member`. There are cases — say, when crafting custom enum behavior — where reaching one member straight from another comes in handy, and this is allowed; nevertheless, to keep member names from colliding with attributes/methods inherited from mixed-in classes, upper-case names are strongly recommended.

Changed in version 3.5.

[Subject index](INDEX.md) · [Previous source context](private-names.md) · [Following source context](creating-members-that-are-mixed-with-other-data-types.md)

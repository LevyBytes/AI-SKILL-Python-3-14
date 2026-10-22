# enum — Supported `_sunder_` names

### Supported `_sunder_` names

- `_name_` – the member's name

- `_value_` – the member's value; assignable within `__new__`

- `_missing_()` – a resolver invoked whenever a value cannot be located; overridable

- `_ignore_` – names supplied as either a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str); these never become members and get dropped from the resulting class

- `_order_` – obsolete now, retained only for backward compatibility (a class attribute that is stripped while the class is built)

- `_generate_next_value_()` – consulted to derive a suitable value for an enum member; overridable

- `_add_alias_()` – registers an additional name pointing at a member that already exists.

- `_add_value_alias_()` – registers an extra value pointing at a member that already exists.

- Although `_sunder_` names are by and large set aside for ongoing evolution of the `Enum` class and remain off-limits, a handful are permitted outright:

  - `_repr_*` (for example `_repr_html_`), of the kind employed by [IPython’s rich display](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display)

Added in version 3.6: `_missing_`, `_order_`, `_generate_next_value_`

Added in version 3.7: `_ignore_`

Added in version 3.13: `_add_alias_`, `_add_value_alias_`, `_repr_*`

---

[Subject index](INDEX.md) · [Previous](supported-dunder-names.md) · [Continue](enum-auto-class.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)

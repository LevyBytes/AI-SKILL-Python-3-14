# Python 3.8.0 beta 1 / library / text

[bpo-36878](https://bugs.python.org/issue?@action=redirect&bpo=36878): With `type_comments=True` active in `ast.parse`, a `# type: ignore` trailed by a non-alphanumeric character plus any further text now counts as a type ignore; previously only whitespace or one more comment was accepted. The motivation is to allow shapes such as `# type: ignore[E1000]`.

[bpo-31829](https://bugs.python.org/issue?@action=redirect&bpo=31829): The characters `\r`, `\0` and `\x1a` (Windows end-of-file) are now escaped inside protocol 0 pickles of Unicode strings. That makes it possible to load them intact out of files opened in text mode under Python 2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

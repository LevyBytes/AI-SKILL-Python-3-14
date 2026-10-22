# Python 3.14 changes: Invalid import and context-manager as-target diagnostics

- Improved error messages when using `as` with incompatible targets in:

  - Imports: `import ... as ...`

  - From imports: `from ... import ... as ...`

  - Except handlers: `except ... as ...`

  - Pattern-match cases: `case ... as ...`

(Contributed by Nikita Sobolev in [gh-123539](https://github.com/python/cpython/issues/123539), [gh-123562](https://github.com/python/cpython/issues/123562), and [gh-123440](https://github.com/python/cpython/issues/123440).)

-

[Subject index](INDEX.md) · [Previous source section](syntax-error-hints.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](syntax-error-hints.md) · [Following release/subject continuation](unhashable-object-error-diagnostics.md)

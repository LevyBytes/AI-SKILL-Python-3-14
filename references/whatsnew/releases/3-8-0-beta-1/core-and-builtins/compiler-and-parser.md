# Python 3.8.0 beta 1 / core and builtins / compiler and parser

[bpo-34616](https://bugs.python.org/issue?@action=redirect&bpo=34616): The `compile()` builtin functions henceforth honor the `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` flag, letting sources with top-level `await`, `async with` or `async for` compile. That helps in evaluating async-code from inside an already async function; a custom REPL is one example.

[bpo-26219](https://bugs.python.org/issue?@action=redirect&bpo=26219): A per-opcode cache scheme landed, and the `LOAD_GLOBAL` instruction taps it; `LOAD_GLOBAL` runs roughly 40% quicker now. Yury Selivanov and Inada Naoki contributed the work.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# readline — Startup hooks

### Startup hooks

 readline.set_startup_hook([*function*])

Install or clear the function that the `rl_startup_hook` callback of the underlying library calls. When *function* is given, it serves as the replacement hook function; if it is left off or set to `None`, whatever function was already in place is cleared. readline calls the hook with no arguments right before it prints the first prompt.

 readline.set_pre_input_hook([*function*])

Install or clear the function that the `rl_pre_input_hook` callback of the underlying library calls. When *function* is given, it serves as the replacement hook function; if it is left off or set to `None`, whatever function was already in place is cleared. readline calls the hook with no arguments once the first prompt has been printed and right before it begins reading input characters. This function is present only when Python was built against a library version that provides it.

[Subject index](INDEX.md) · [Previous](readline-clear-history-to-readline-set-auto-history.md) · [Continue](readline-completion-and-display-hooks.md) · [Owning module, declaration or section: readline](readline-backend.md)

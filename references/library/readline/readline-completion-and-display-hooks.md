# readline - Completion

### Completion

The functions below concern building a custom word completion function. The Tab key typically drives this, and it can offer suggestions and finish a word as it is being typed. Out of the box, Readline is wired so that [`rlcompleter`](https://docs.python.org/3.14/library/rlcompleter.html#module-rlcompleter) can complete Python identifiers for the interactive interpreter. When you pair the `readline` module with a custom completer, you should establish a different set of word delimiters.

 readline.set_completer([*function*])

Install or clear the completer function. When *function* is given, it serves as the replacement completer function; if it is left off or set to `None`, whatever completer function was already in place is cleared. The completer function is invoked as `function(text, state)`, for *state* across `0`, `1`, `2`, …, until it gives back a non-string value. It is expected to give back the next candidate completion that begins with *text*.

The completer function you installed is invoked through the *entry_func* callback handed to `rl_completion_matches()` in the underlying library. The *text* string originates from the first parameter to the `rl_attempted_completion_function` callback of the underlying library.

 readline.get_completer()

Fetch the completer function, or `None` when no completer function has been installed.

 readline.get_completion_type()

Fetch which kind of completion is being attempted. This gives back the `rl_completion_type` variable in the underlying library as an integer.

 readline.get_begidx()

 readline.get_endidx()

Fetch the start or the end index of the completion scope. These indexes correspond to the *start* and *end* arguments handed to the `rl_attempted_completion_function` callback of the underlying library. Within an identical input editing scenario the values can differ depending on the underlying C readline implementation. For example, libedit is known to behave differently than libreadline.

 readline.set_completer_delims(*string*)

 readline.get_completer_delims()

Assign or fetch the word delimiters for completion. These mark where the word being considered for completion (the completion scope) begins. These functions reach the `rl_completer_word_break_characters` variable in the underlying library.

 readline.set_completion_display_matches_hook([*function*])

Install or clear the completion display function. When *function* is given, it serves as the replacement completion display function; if it is left off or set to `None`, whatever completion display function was already in place is cleared. In the underlying library, this installs or removes the `rl_completion_display_matches_hook` callback. Each time matches have to be shown, the completion display function gets invoked as `function(substitution, [matches], longest_match_length)`.

[Subject index](INDEX.md) · [Previous](readline-set-startup-hook-to-readline-set-pre-input-hook.md) · [Continue](example.md) · [Owning module, declaration or section: readline](readline-backend.md)

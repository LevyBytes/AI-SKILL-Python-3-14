# 3.4.3.1. make

### 3.4.3. Main Makefile targets

#### 3.4.3.1. make

In most situations, after you tweak some code or pull a fresh checkout from upstream, simply running `make` is enough; following Make's rules, that builds the default target, namely the first one listed in the Makefile. As convention has it (the CPython project included), that target is normally `all`. The `configure` script substitutes an `autoconf` variable, `@DEF_MAKE_ALL_RULE@`, to spell out exactly which targets `make all` ends up building. The trio of possibilities is:

- `profile-opt` (configured with `--enable-optimizations`)

- `build_wasm` (picked when the host platform lines up with `wasm32-wasi*` or `wasm32-emscripten`)

- `build_all` (the configuration when neither of the other two is requested outright)

Based on whichever source files changed most recently, Make rebuilds any targets (object files and executables) it judges stale, and it will re-run `configure` when that proves necessary. Yet the source-to-target dependencies are numerous and tracked by hand, so Make occasionally lacks the full picture needed to spot every target due for a rebuild. Which problems crop up hinges on which targets went un-rebuilt. When you hit build or test trouble that defies explanation, `make clean && make` sidesteps the bulk of dependency snags, though it costs you a longer build.

[Subject index](INDEX.md) · [Previous source section](main-build-steps.md) · [Following source section](make-platform.md)

# Reference checks

Recurring failure modes when relying on the Python Language Reference reference, and what to do instead. Read alongside `SKILL.md`.

- This is the Python 3.14 documentation and is version-specific. Entries carry `Added in version`, `Changed in version`, and `Deprecated since version` notes - honor them and do not assume a feature, parameter, or default exists on an older interpreter.
- The Standard Library is large and packed across many files under `library/references/`; use that sub-skill's `references/INDEX.md` or grep (`rg -n "^### |class |def " library/references/*.md`) to find the exact module/function rather than guessing a filename.
- Interactive examples keep their `>>>` and `...` prompts and expected output verbatim - strip the prompts before running the code, and remember the output lines are illustrative, not part of the source.
- Treat every signature, parameter name, default value, exception type, module path, and `__dunder__` name as an exact reference fact - do not paraphrase, reorder keyword-only args, or invent names.
- `installing` and `distributing` are intentionally short overviews that defer to the Python Packaging User Guide (packaging.python.org); the detailed packaging workflow is not reproduced here.

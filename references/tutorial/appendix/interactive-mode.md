# 16.1. Interactive Mode

# Appendix, Appetite

## Overview

Covers: 16. Appendix; 1. Whetting Your Appetite.

## 16. Appendix

### 16. Appendix

### 16.1. Interactive Mode

The interactive [REPL](https://docs.python.org/3.14/glossary.html#term-REPL) ships in two flavors. The traditional, no-frills interpreter runs everywhere but offers only rudimentary control over the input line.

Beginning with Python 3.13, a fresh interactive shell became the standard. It brings colorized output, editing across multiple lines, scrolling through past entries, and a dedicated paste mode. Should you wish to turn colors off, the page on [Controlling color](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color) explains how. The function keys layer on extra capabilities too. Pressing F1 opens the interactive help viewer [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc). With F2 you can page through your command-line history stripped of any output and of the [>>>](https://docs.python.org/3.14/glossary.html#term-0) and […](https://docs.python.org/3.14/glossary.html#term-...) prompts. F3 switches on “paste mode”, smoothing the insertion of sizeable chunks of code; hit F3 again to come back to the normal prompt.

To leave the new interactive shell, simply type exit or quit; there is no need to append call parentheses to either keyword.

Prefer not to use the new interactive shell? Switch it off through the [`PYTHON_BASIC_REPL`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable.

[Subject index](INDEX.md) · [Following source section](error-handling.md)

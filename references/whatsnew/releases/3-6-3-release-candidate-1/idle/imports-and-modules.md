# Python 3.6.3 release candidate 1 / idle / imports and modules

[bpo-30728](https://bugs.python.org/issue?@action=redirect&bpo=30728): Audit and revise the idlelib.configdialog names. Make method and attribute names lowercase. Swap "colour" for "color", broaden names that were too cryptic, and remove needless underscores. Trade `import *` for explicit imports. Cheryl Sabella supplied the patches.

[bpo-30617](https://bugs.python.org/issue?@action=redirect&bpo=30617): IDLE - Supply docstrings plus tests for the outwin subclass of editor. Several data items and functions shifted from the class up to module level. Cheryl Sabella wrote the patch.

[bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099): Turned IDLE's built-in "extensions" into ordinary features. Roughly 10 IDLE capabilities had been written as nominally optional extensions. Because they behaved differently they risked confusing (or worse) users and were awkward to maintain, hence this conversion. For users the chief change is that the user-configurable key bindings for builtin features now follow a single uniform model. From now on, altering a binding inside a keyset changes only its value within that keyset. Every binding sits together in the system-specific default keysets held in config-extensions.def. Whole custom keysets get stored as a unit in config-extension.cfg. They all apply the moment one presses Apply or Ok. These are the events that this touches:
> "<&lt;force-open-completions&gt;>", "<&lt;expand-word&gt;>", "<&lt;force-open-calltip&gt;>", "<&lt;flash-paren&gt;>", "<&lt;format-paragraph&gt;>", "<&lt;run-module&gt;>", "<&lt;check-module&gt;>", and "<&lt;zoom-height&gt;>".

Should a person have set any (global) customizations earlier than 3.6.3, none of those will reach the keyset-specific customization that follows 3.6.3. and the reverse holds too. Charles Wohlganger contributed the initial patch.

[bpo-30674](https://bugs.python.org/issue?@action=redirect&bpo=30674): IDLE: supply docstrings within the grep module. Cheryl Sabella wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

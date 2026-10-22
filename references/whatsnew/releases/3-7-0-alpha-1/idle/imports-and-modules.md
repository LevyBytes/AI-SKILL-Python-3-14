# Python 3.7.0 alpha 1 / idle / imports and modules

[bpo-30728](https://bugs.python.org/issue?@action=redirect&bpo=30728): Audit and revise the idlelib.configdialog names. Lowercase the method and attribute names. Swap ‘color’ in for ‘colour’, expand overly cryptic names, and remove unnecessary underscores. Replace `import *` with explicit imports. Cheryl Sabella supplied the patches.

[bpo-30617](https://bugs.python.org/issue?@action=redirect&bpo=30617): IDLE - Supply docstrings plus tests for the editor's outwin subclass. Shift some data and functions out of the class up to module level. Cheryl Sabella supplied the patch.

[bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099): Turn IDLE’s built-in ‘extensions’ into ordinary features. Roughly 10 IDLE features had been built as nominally optional extensions. The way they behaved differently could confuse users or worse, and it was bad for maintenance, which is why they were converted. From a user's standpoint, the chief change is that configurable key bindings for builtin features are now treated uniformly. Editing a binding within a keyset now changes only that binding's value in that keyset. Every binding is now declared together inside the system-specific default keysets in config-extensions.def. Each custom keyset is stored as a whole within config-extension.cfg. They all become active the moment one clicks Apply or Ok. This touches the following events: ‘<&lt;force-open-completions&gt;>’ plus ‘<&lt;expand-word&gt;>’; ‘<&lt;force-open-calltip&gt;>’ together with ‘<&lt;flash-paren&gt;>’; ‘<&lt;format-paragraph&gt;>’ alongside ‘<&lt;run-module&gt;>’; and finally ‘<&lt;check-module&gt;>’ as well as ‘<&lt;zoom-height&gt;>’. Whatever (global) customizations were made prior to 3.6.3 will not carry over to their keyset-specific customization from 3.6.3 onward, and the reverse holds too. Charles Wohlganger wrote the first version of the patch.

[bpo-30674](https://bugs.python.org/issue?@action=redirect&bpo=30674): IDLE: add docstrings throughout the grep module. Cheryl Sabella supplied the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

# Python 3.8.0 alpha 1 / idle / imports and modules

[bpo-33906](https://bugs.python.org/issue?@action=redirect&bpo=33906): Rename idlelib.windows into window to align with Window on the main menu and shed the final plural module name.

[bpo-33907](https://bugs.python.org/issue?@action=redirect&bpo=33907): To improve clarity and stay consistent, an IDLE module plus its classes get renamed. The calltips module and its CallTips class become calltip and Calltip. Within calltip_w, the former CallTip class is renamed CalltipWindow.

[bpo-33855](https://bugs.python.org/issue?@action=redirect&bpo=33855): Give every IDLE module at least minimal testing. Supply absent files, import each module, build its classes, and confirm coverage. Audit the files already present.

[bpo-32905](https://bugs.python.org/issue?@action=redirect&bpo=32905): Drop dead code from the pyparse module.

[bpo-35660](https://bugs.python.org/issue?@action=redirect&bpo=35660): Repair the imports inside idlelib.window.

[bpo-35202](https://bugs.python.org/issue?@action=redirect&bpo=35202): Strip the unused imports out of lib/idlelib.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

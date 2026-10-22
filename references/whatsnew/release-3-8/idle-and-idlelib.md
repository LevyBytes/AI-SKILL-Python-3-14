# What’s New In Python 3.8 / IDLE and idlelib

> (Contributed by Filip Gruszczyński, Michele Orr??, and Zackery Spytz in [bpo-6584](https://bugs.python.org/issue?@action=redirect&bpo=6584).)

### IDLE and idlelib

When output runs past N lines (the default being 50), it collapses into a button. You can adjust N within the PyShell section of the General page in the Settings dialog. Lines that are fewer yet perhaps very long can be collapsed via a right click on the output. Collapsed output can reopen in place through a double-click on the button, or land on the clipboard or in its own window if you right-click the button.
> (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

A "Run Customized" entry now sits on the Run menu for launching a module under tailored settings. Whatever command line arguments you type get appended to sys.argv. Those also show up again inside the box for your next customized run. You can additionally hold back the usual Shell main module restart.
> (Contributed by Cheryl Sabella, Terry Jan Reedy, and others in [bpo-5680](https://bugs.python.org/issue?@action=redirect&bpo=5680) and [bpo-37627](https://bugs.python.org/issue?@action=redirect&bpo=37627).)

Optional line numbers have been added for IDLE editor windows. A window opens without line numbers unless you have configured otherwise on the General tab of the configuration dialog. For any window already open, line numbers get toggled on or off through the Options menu.
> (Contributed by Tal Einat and Saimadhav Heblikar in [bpo-17535](https://bugs.python.org/issue?@action=redirect&bpo=17535).)

Conversion between Python strings and Tcl objects now relies on the OS native encoding. Thanks to that, IDLE handles emoji along with other non-BMP characters. Such characters can show up or be copied and pasted into or out of the clipboard. Round-tripping strings from Tcl over to Python and back never breaks anymore. (Numerous contributors chased this for eight years, but the fix finally came from Serhiy Storchaka in [bpo-13153](https://bugs.python.org/issue?@action=redirect&bpo=13153).)

New in 3.8.1:

An option now lets you switch the cursor blink off.
> (Contributed by Zackery Spytz in [bpo-4603](https://bugs.python.org/issue?@action=redirect&bpo=4603).)

Pressing the Escape key now dismisses IDLE completion windows.
> (Contributed by Johnny Najera in [bpo-38944](https://bugs.python.org/issue?@action=redirect&bpo=38944).)

Every change listed above has been backported into the 3.7 maintenance releases.

Keywords are now folded into the module name completion list.

[Subject index](INDEX.md) · [Previous source section](gzip.md) · [Next source section](inspect.md) · [Release/subject declaration](assignment-expressions.md)

# What's New In Python 3.7 / idlelib and IDLE

### idlelib and IDLE

Several autocompletion bugs were corrected. (Contributed by Louie Lu in [bpo-15786](https://bugs.python.org/issue?@action=redirect&bpo=15786).)

The Module Browser (reachable from the File menu, once known as Class Browser) will now show both nested functions and classes alongside the ones declared at the top level. (Contributed by Guilherme Polo, Cheryl Sabella, and Terry Jan Reedy in [bpo-1612262](https://bugs.python.org/issue?@action=redirect&bpo=1612262).)

To sharpen its look and behavior, the Settings dialog (Options, Configure IDLE) saw a partial rewrite. (Contributed by Cheryl Sabella and Terry Jan Reedy in multiple issues.)

A range of non-Latin characters now appears in the font sample, helping users gauge more clearly what a given font looks like. (Contributed by Terry Jan Reedy in [bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802).) You can edit the sample to add other characters too. (Contributed by Serhiy Storchaka in [bpo-31860](https://bugs.python.org/issue?@action=redirect&bpo=31860).)

IDLE capabilities that previously shipped as extensions are now built directly into the application as standard features. Where you configure them moved off the Extensions tab and onto other dialog tabs. (Contributed by Charles Wohlganger and Terry Jan Reedy in [bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099).)

The editor's code context option saw a rework. Its box now shows every context line up through maxlines, and clicking any of those lines moves the editor straight to it. For custom themes, you can now set context colors via the Highlights tab of the Settings dialog. (Contributed by Cheryl Sabella and Terry Jan Reedy in [bpo-33642](https://bugs.python.org/issue?@action=redirect&bpo=33642), [bpo-33768](https://bugs.python.org/issue?@action=redirect&bpo=33768), and [bpo-33679](https://bugs.python.org/issue?@action=redirect&bpo=33679).)

On Windows, a fresh API call notifies the OS that tk handles DPI scaling. Under Windows 8.1+ or 10, provided the Python binary's DPI compatibility properties are left as-is and the display runs above 96 DPI, text and lines ought to look crisper. Otherwise nothing visibly changes. (Contributed by Terry Jan Reedy in [bpo-33656](https://bugs.python.org/issue?@action=redirect&bpo=33656).)

New in 3.7.1:

When output exceeds N lines (the default being 50), it collapses into a single button. You can adjust N from the PyShell section under the General page of the Settings dialog. Right-clicking on output lets you squeeze a smaller number of lines that may each be very long. To bring squeezed output back, double-click the button to expand it in place, or right-click the button to send it either to the clipboard or to its own window. (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

Everything described above was also backported into the 3.6 maintenance releases.

NEW in 3.7.4:

A “Run Customized” entry was added under the Run menu so a module can run with tailored settings. Whatever command line arguments you type get appended to sys.argv, and they show up again in the box on the following customized run. There is also the option to disable that customary restart of the Shell main module. (Contributed by Cheryl Sabella, Terry Jan Reedy, and others in [bpo-5680](https://bugs.python.org/issue?@action=redirect&bpo=5680) and [bpo-37627](https://bugs.python.org/issue?@action=redirect&bpo=37627).)

New in 3.7.5:

IDLE editor windows gained optional line numbers. By default a window opens with none, unless you change that on the General tab of the configuration dialog. Use the Options menu to toggle the display of line numbers for any window already open. (Contributed by Tal Einat and Saimadhav Heblikar in [bpo-17535](https://bugs.python.org/issue?@action=redirect&bpo=17535).)

[Subject index](INDEX.md) · [Previous source section](http-server.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](importlib.md)

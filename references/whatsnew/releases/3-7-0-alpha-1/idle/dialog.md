# Python 3.7.0 alpha 1 / idle / dialog

[bpo-30913](https://bugs.python.org/issue?@action=redirect&bpo=30913): IDLE: Document the ConfigDialog tk Vars, methods, and widgets inside docstrings. Doing so will ease refining the dialog and breaking up the class. Cheryl Sabella wrote the first version of the patch.

[bpo-30870](https://bugs.python.org/issue?@action=redirect&bpo=30870): IDLE: Within the Settings dialog, pick a font using the Up and Down keys as well as the mouse. Louie Lu wrote the first version of the patch.

[bpo-30723](https://bugs.python.org/issue?@action=redirect&bpo=30723): IDLE: Apply several refinements to parenmatch. Introduce a ‘parens’ style that highlights both the opener and the closer. Turn the ‘default’ style, which is not actually the default, into a synonym for ‘opener’. Make the time-delay behave identically across every style. Add help on the config dialog extensions tab, including help for parenmatch. Add new tests. Charles Wohlganger wrote the first version of the patch.

[bpo-21519](https://bugs.python.org/issue?@action=redirect&bpo=21519): IDLE’s basic custom key entry dialog now spots duplicates correctly. Saimadhav Heblikar wrote the first version of the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

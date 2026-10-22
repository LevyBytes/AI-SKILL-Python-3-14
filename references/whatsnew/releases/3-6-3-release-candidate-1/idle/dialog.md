# Python 3.6.3 release candidate 1 / idle / dialog

[bpo-30913](https://bugs.python.org/issue?@action=redirect&bpo=30913): IDLE: Describe the ConfigDialog tk Vars, methods, plus widgets through docstrings, which will ease refining the dialog and breaking up the class. Cheryl Sabella supplied the original patch.

[bpo-30870](https://bugs.python.org/issue?@action=redirect&bpo=30870): IDLE: Within the Settings dialog, pick a font using the Up and Down keys in addition to the mouse. Louie Lu supplied the initial patch.

[bpo-30723](https://bugs.python.org/issue?@action=redirect&bpo=30723): IDLE: Roll out several parenmatch refinements. Add a "parens" style that highlights both the opener and the closer. Turn the "default" style, which is in fact not the default, into a synonym for "opener". Make the time-delay behave identically across all styles. Add help for the config dialog extensions tab, parenmatch included. Add fresh tests. Charles Wohlganger supplied the original patch.

[bpo-21519](https://bugs.python.org/issue?@action=redirect&bpo=21519): IDLE's basic custom key entry dialog now spots duplicates the right way. Saimadhav Heblikar supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

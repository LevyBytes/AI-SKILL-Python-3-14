# configparser: `configparser.ExtendedInterpolation`

*class *configparser.ExtendedInterpolation

A different interpolation handler offering a richer syntax, employed for example by `zc.buildout`. With extended interpolation, `${section:option}` names a value living in another section. References can nest through several levels. As a shortcut, dropping the `section:` portion makes interpolation fall back to the present section (plus, where relevant, the defaults from the special section).

For example, the very configuration given above under basic interpolation would appear as follows when extended interpolation is used:

```ini
[Paths]
home_dir: /Users
my_dir: ${home_dir}/lumberjack
my_pictures: ${my_dir}/Pictures

[Escape]
# use a $$ to escape the $ sign ($ is the only character that needs to be escaped):
cost: $$80

```

Pulling values out of other sections works too:

```ini
[Common]
home_dir: /Users
library_dir: /Library
system_dir: /System
macports_dir: /opt/local

[Frameworks]
Python: 3.2
path: ${Common:system_dir}/Library/Frameworks/

[Arthur]
nickname: Two Sheds
last_name: Jackson
my_dir: ${Common:home_dir}/twosheds
my_pictures: ${my_dir}/Pictures
python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}

```

[Subject index](INDEX.md) · [Previous](configparser-basicinterpolation-class.md) · [Continue](mapping-protocol-access.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Interpolation of values](configparser-basicinterpolation-class.md)

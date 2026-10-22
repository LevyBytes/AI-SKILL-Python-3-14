# configparser: `configparser.BasicInterpolation`

### Interpolation of values

Beyond its essential features, `ConfigParser` offers interpolation. What that means is that values can undergo preprocessing before `get()` calls hand them back.

 *class *configparser.BasicInterpolation

This is what `ConfigParser` employs by default. It lets values hold format strings that point at other values within the same section, or at values stored in the special default section [1]. You may also pass extra default values at initialization time.

For example:

```ini
[Paths]
home_dir: /Users
my_dir: %(home_dir)s/lumberjack
my_pictures: %(my_dir)s/Pictures

[Escape]
# use a %% to escape the % sign (% is the only character that needs to be escaped):
gain: 80%%

```

Given the example above, a `ConfigParser` whose *interpolation* is `BasicInterpolation()` would expand `%(home_dir)s` into the `home_dir` value (here that's `/Users`). `%(my_dir)s` would then come out as `/Users/lumberjack`. Each interpolation happens lazily, so the keys feeding a reference chain need not appear in any particular sequence within the configuration file.

When `interpolation` is `None`, the parser hands back `%(my_dir)s/Pictures` as `my_pictures`'s value verbatim and `%(home_dir)s/lumberjack` as `my_dir`'s value.

[Subject index](INDEX.md) · [Previous](unnamed-sections.md) · [Continue](configparser-extendedinterpolation-class.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)

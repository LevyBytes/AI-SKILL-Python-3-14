# configparser — Fallback Values

### Fallback Values

Just like with a dictionary, a section's `get()` method lets you supply fallback values:

```pycon
>>> topsecret.get('Port')
'50022'
>>> topsecret.get('CompressionLevel')
'9'
>>> topsecret.get('Cipher')
>>> topsecret.get('Cipher', '3des-cbc')
'3des-cbc'

```

Bear in mind that defaults outrank fallback values. Take our case: the `'CompressionLevel'` key appeared solely within the `'DEFAULT'` section. Should we request it from section `'topsecret.server.example'`, the default comes back every time, even when a fallback is supplied:

```pycon
>>> topsecret.get('CompressionLevel', '3')
'9'

```

There's a further point worth noting: the `get()` method at the parser level exposes a richer, somewhat unusual interface, kept around for backwards compatibility. With that method, you supply a fallback value by way of the `fallback` keyword-only argument:

```pycon
>>> config.get('forge.example', 'monster',
...            fallback='No such things as monsters')
'No such things as monsters'

```

That very same `fallback` argument also works with the `getint()`, `getfloat()` and `getboolean()` methods, as shown here:

```pycon
>>> 'BatchMode' in topsecret
False
>>> topsecret.getboolean('BatchMode', fallback=True)
True
>>> config['DEFAULT']['BatchMode'] = 'no'
>>> topsecret.getboolean('BatchMode', fallback=True)
False

```

[Subject index](INDEX.md) · [Previous](supported-datatypes.md) · [Continue](supported-ini-file-structure.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)

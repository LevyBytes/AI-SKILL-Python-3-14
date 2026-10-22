# 16.1.4. The Customization Modules

### 16.1.4. The Customization Modules

For customization, Python exposes a pair of hooks: sitecustomize and usercustomize. Before you can use them, locate your user site-packages directory. Launch Python and execute the following:

```python
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.x/site-packages'

```

At that point you may add a `usercustomize.py` file inside that folder and fill it with whatever you like. Every run of Python will then pick it up, unless Python was launched with the [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) flag, which turns off the automatic import.

The sitecustomize hook behaves identically, except it is usually set up by a machine administrator inside the global site-packages directory and loads ahead of usercustomize. Consult the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module documentation for further specifics.

Footnotes

[Subject index](INDEX.md) · [Previous source section](the-interactive-startup-file.md) · [Following source section](../whetting-your-appetite/whetting-your-appetite.md)

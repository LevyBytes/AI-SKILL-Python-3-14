# gettext — Internationalizing your programs and modules

### Internationalizing your programs and modules

Internationalization (I18N) names the process whereby a program becomes aware of multiple languages. Localization (L10N) names the step of tailoring your already-internationalized program to a particular local language together with its cultural conventions. To deliver multilingual messages for your Python programs, you must carry out the following steps:

1.

ready your program or module by distinctively flagging the translatable strings

2.

apply a toolchain across your flagged files to produce raw messages catalogs

3.

author per-language translations of those message catalogs

4.

bring in the `gettext` module so message strings get translated correctly

To ready your code for I18N, you must examine every string in your files. Each string requiring translation should be flagged by enclosing it in `_('...')` — that is, a call to the function `_`. For instance:

```python
filename = 'mylog.txt'
message = _('writing a log message')
with open(filename, 'w') as fp:
    fp.write(message)

```

Within this example, the string `'writing a log message'` is flagged as a candidate for translation, whereas the strings `'mylog.txt'` and `'w'` are not.

Several tools exist to pull out the strings intended for translation. The original GNU **gettext** handled only C or C++ source code, but its extended version **xgettext** scans code authored in numerous languages, Python included, to locate strings flagged as translatable. [Babel](https://babel.pocoo.org/) is a Python internationalization library that ships a `pybabel` script for extracting and compiling message catalogs. François Pinard's program named **xpot** performs a comparable job and is distributed within his [po-utils package](https://github.com/pinard/po-utils).

(Python additionally bundles pure-Python editions of these programs, named **pygettext.py** and **msgfmt.py**; certain Python distributions will install them on your behalf. **pygettext.py** resembles **xgettext**, yet it understands only Python source code and cannot process other programming languages like C or C++. **pygettext.py** offers a command-line interface much like **xgettext**; for specifics on its use, run `pygettext.py --help`. **msgfmt.py** is binary compatible with GNU **msgfmt**. Armed with these two programs, you might not need the GNU **gettext** package to internationalize your Python applications.)

**xgettext**, **pygettext**, and comparable tools produce `.po` files that act as message catalogs. They are structured human-readable files holding every flagged string from the source code, paired with a placeholder for the translated versions of those strings.

Copies of these `.po` files then go to the individual human translators who compose translations for each supported natural language. They return the finished language-specific versions as a `<language-name>.po` file that gets compiled into a machine-readable `.mo` binary catalog file via the **msgfmt** program. The `.mo` files are consumed by the `gettext` module for the actual translation processing at run-time.

The way you employ the `gettext` module within your code hinges on whether you are internationalizing one module or your whole application. Each case is covered in the two sections that follow.

[Subject index](INDEX.md) · [Previous](the-catalog-constructor.md) · [Continue](localizing-your-module.md) · [Owning module, declaration or section: gettext](gettext-multilingual-internationalization-services.md)

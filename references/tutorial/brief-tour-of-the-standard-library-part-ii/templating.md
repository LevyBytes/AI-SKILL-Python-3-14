# 11.2. Templating

### 11.2. Templating

Bundled in the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module is a flexible [`Template`](https://docs.python.org/3.14/library/string.html#string.Template) class whose pared-down syntax is friendly for end-users to edit. That lets people tailor their applications without modifying the application itself.

In this scheme, placeholder names are built from `$` followed by any valid Python identifier (alphanumeric characters and underscores). Wrapping a placeholder in braces lets additional alphanumeric letters trail it without a gap in between. To emit a single literal escaped `$`, write `$$`:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'

```

Should a placeholder go unsupplied by a dictionary or keyword argument, the [`substitute()`](https://docs.python.org/3.14/library/string.html#string.Template.substitute) method throws a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError). Because user-provided data can be partial in mail-merge scenarios, the [`safe_substitute()`](https://docs.python.org/3.14/library/string.html#string.Template.safe_substitute) method is often a better fit — any placeholder whose data is absent is simply left as-is:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'

```

A custom delimiter can be declared by subclasses of Template. As an illustration, a bulk-renaming tool inside a photo browser might choose percent signs for placeholders that stand in for things like today's date, an image sequence number, or the file's format:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
...
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg

```

Templating also serves to keep a program's logic apart from the particulars of several output formats. That separation lets you swap in tailored templates for XML files, plain text reports, and HTML web reports.

[Subject index](INDEX.md) · [Previous source section](output-formatting.md) · [Following source section](working-with-binary-data-record-layouts.md)

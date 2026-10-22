# xml.etree.ElementTree — Modifying an XML File

### Modifying an XML File

`ElementTree` gives you an easy means of assembling XML documents and saving them to files. That job is handled by the `ElementTree.write()` method.

After an `Element` object exists, you can work on it by altering its fields outright (for instance `Element.text`), by inserting and changing attributes (the `Element.set()` method), and by attaching new children (with `Element.append()`, for example).

Suppose we'd like to bump each country's rank by one and attach an `updated` attribute onto the rank element:

```python
>>> for rank in root.iter('rank'):
...     new_rank = int(rank.text) + 1
...     rank.text = str(new_rank)
...     rank.set('updated', 'yes')
...
>>> tree.write('output.xml')

```

At this point our XML reads as follows:

```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

```

Elements can be deleted via `Element.remove()`. Imagine we want to drop every country whose rank exceeds 50:

```python
>>> for country in root.findall('country'):
...     # using root.findall() to avoid removal during traversal
...     rank = int(country.find('rank').text)
...     if rank > 50:
...         root.remove(country)
...
>>> tree.write('output.xml')

```

Keep in mind that altering a structure during iteration over it can cause trouble, much as it does when you iterate over and change Python lists or dicts. For that reason, the example gathers every matching element up front through `root.findall()` and only afterward loops across the resulting list of matches.

At this point our XML reads as follows:

```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
</data>

```

[Subject index](INDEX.md) · [Previous](finding-interesting-elements.md) · [Continue](building-xml-documents.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)

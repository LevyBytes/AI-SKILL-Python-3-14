# xml.etree.ElementTree — Parsing XML with Namespaces

### Parsing XML with Namespaces

When the XML input carries [namespaces](https://en.wikipedia.org/wiki/XML_namespace), tags and attributes whose prefixes look like `prefix:sometag` are widened into `{uri}sometag`, with the *prefix* swapped for the complete *URI*. On top of that, when a [default namespace](https://www.w3.org/TR/xml-names/#defaulting) is present, its full URI is attached to the front of every tag lacking a prefix.

Below is an XML example that brings in two namespaces - one carrying the prefix "fictional" and the other acting as the default namespace:

```xml
<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>

```

One approach to searching and navigating this XML example is to attach the URI by hand to each tag or attribute within the xpath given to `find()` or `findall()`:

```python
root = fromstring(xml_text)
for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)

```

A more effective approach to querying the namespaced XML example is to build a dictionary holding prefixes of your choosing and supply those to the search functions:

```python
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor', ns):
    name = actor.find('real_person:name', ns)
    print(name.text)
    for char in actor.findall('role:character', ns):
        print(' |-->', char.text)

```

Each of these two methods produces the same output:

```python
John Cleese
 |--> Lancelot
 |--> Archie Leach
Eric Idle
 |--> Sir Robin
 |--> Gunther
 |--> Commander Clement

```

[Subject index](INDEX.md) · [Previous](building-xml-documents.md) · [Continue](xpath-support.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)

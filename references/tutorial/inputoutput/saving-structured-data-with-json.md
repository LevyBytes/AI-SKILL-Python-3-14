# 7.2.2. Saving structured data with `json`

### 7.2.2. Saving structured data with [`json`](https://docs.python.org/3.14/library/json.html#module-json)

Writing strings out to a file and reading them back is a simple affair. Numbers call for a little more work, because the [`read()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.read) method hands back only strings, and one of those must be fed to a function such as [`int()`](https://docs.python.org/3.14/library/functions.html#int), which accepts a string like `'123'` and gives back its numeric value 123. The moment you set out to store richer data types, such as nested lists and dictionaries, doing the parsing and serializing yourself turns awkward.

So that users aren't forever writing and debugging code to commit involved data types to files, Python lets you reach for the widely used data interchange format known as [JSON (JavaScript Object Notation)](https://json.org). The standard module named [`json`](https://docs.python.org/3.14/library/json.html#module-json) is able to take Python data hierarchies and render them as string representations, a step termed *serializing*. Rebuilding the data out of that string representation goes by the name *deserializing*. In the interval between the two, the string standing in for the object might have been tucked away in a file or data, or shipped across a network connection to some far-off machine.

Note

Today's applications lean on the JSON format heavily as a means of trading data. A great many programmers already know it well, and that familiarity makes it a sound pick for interoperability.

Given an object `x`, a single line of code is enough to inspect its JSON string representation:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'

```

A further form of the [`dumps()`](https://docs.python.org/3.14/library/json.html#json.dumps) function, named [`dump()`](https://docs.python.org/3.14/library/json.html#json.dump), just serializes the object straight to a [text file](https://docs.python.org/3.14/glossary.html#term-text-file). So when `f` is a text file object opened for writing, we can write the following:

```python
json.dump(x, f)

```

To decode that object once more, where `f` is a [binary file](https://docs.python.org/3.14/glossary.html#term-binary-file) or [text file](https://docs.python.org/3.14/glossary.html#term-text-file) object that was opened for reading:

```python
x = json.load(f)

```

Note

A JSON file has to be encoded as UTF-8. Pass `encoding="utf-8"` whenever you open a JSON file as a [text file](https://docs.python.org/3.14/glossary.html#term-text-file), for reading as well as for writing.

Lists and dictionaries fall within reach of this basic serialization method, yet getting arbitrary class instances into JSON takes a bit more work. The explanation of that lives in the reference for the [`json`](https://docs.python.org/3.14/library/json.html#module-json) module.

See also

[`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) - the pickle module

Unlike JSON, *pickle* is a protocol that supports serializing Python objects of arbitrary complexity. Because of that, it is tied to Python and won't serve to talk to applications built in other languages. It is, moreover, insecure out of the box: feeding pickle data from a source you don't trust through deserialization can run arbitrary code, should a capable attacker have shaped that data.

[Subject index](INDEX.md) · [Previous source section](methods-of-file-objects.md)

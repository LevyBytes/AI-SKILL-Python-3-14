# re — Making a Phonebook

### Making a Phonebook

`split()` breaks a string into a list using the supplied pattern as the delimiter. That makes the method indispensable for turning raw text into data structures Python can read and edit with ease — as the phonebook-building example that follows shows.

To begin, here is the source data. It would usually be loaded from a file, but here we rely on triple-quoted string syntax

```pycon
>>> text = """Ross McFluff: 834.345.1254 155 Elm Street
...
... Ronald Heathmore: 892.345.3428 436 Finley Avenue
... Frank Burger: 925.541.7625 662 South Dogwood Way
...
...
... Heather Albrecht: 548.326.4584 919 Park Place"""

```

A run of one or more newlines divides the entries. Next we transform the string into a list in which every nonempty line becomes a separate entry:

```pycon
>>> entries = re.split("\n+", text)
>>> entries
['Ross McFluff: 834.345.1254 155 Elm Street',
'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
'Frank Burger: 925.541.7625 662 South Dogwood Way',
'Heather Albrecht: 548.326.4584 919 Park Place']

```

To finish, break each entry into a list holding first name, last name, telephone number, and address. We supply the `maxsplit` parameter to `split()` since the address itself contains spaces — and spaces are exactly the pattern we split on:

```pycon
>>> [re.split(":? ", entry, maxsplit=3) for entry in entries]
[['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

```

Thanks to the `:?` pattern, the colon trailing the last name is consumed and so never lands in the resulting list. Bumping `maxsplit` up to `4` would let us split the house number away from the street name:

```pycon
>>> [re.split(":? ", entry, maxsplit=4) for entry in entries]
[['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]

```

[Subject index](INDEX.md) · [Previous](re-search.md) · [Continue](text-munging.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)

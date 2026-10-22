# ORM example

### ORM example

What follows is a trimmed-down skeleton illustrating one way that data descriptors might back an [object relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping).

At its core, the data resides in an outside database. Each Python instance merely retains keys pointing into the database's tables. The descriptors handle the lookups and the updates:

```python
class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()

```

The `Field` class lets us declare [models](https://en.wikipedia.org/wiki/Database_model) that lay out the schema for every table in a database:

```python
class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key

```

Putting the models to work begins with a connection to the database:

```python
>>> import sqlite3
>>> conn = sqlite3.connect('entertainment.db')

```

The following interactive session demonstrates fetching data from the database along with updating it:

```pycon
>>> Movie('Star Wars').director
'George Lucas'
>>> jaws = Movie('Jaws')
>>> f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

>>> Song('Country Roads').artist
'John Denver'

>>> Movie('Star Wars').director = 'J.J. Abrams'
>>> Movie('Star Wars').director
'J.J. Abrams'

```

[Subject index](INDEX.md) · [Previous source context](automatic-name-notification.md) · [Following source context](pure-python-equivalents.md)

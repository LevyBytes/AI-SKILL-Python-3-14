# How do I cache method calls?

### How do I cache method calls?

For caching methods, the two main instruments are [`functools.cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property) and [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache). The first keeps its results per instance, while the second keeps them per class.

The `cached_property` route is usable only with methods that accept no arguments. It holds no reference to the instance. Whatever the cached method computed survives only for as long as the instance does.

The upside is that once an instance falls out of use, its cached method result is freed immediately. The downside is that as instances pile up, the cached method results pile up alongside them. There is no upper limit on how far they can grow.

The `lru_cache` route handles methods whose arguments are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). It does hold a reference to the instance unless you go out of your way to supply weak references.

The benefit of the least recently used algorithm is that *maxsize* caps the cache. The drawback is that instances stay alive until they fall out of the cache by age or until the cache is emptied.

This example demonstrates the assorted approaches:

```python
class Weather:
    "Lookup weather information on a government website"

    def __init__(self, station_id):
        self._station_id = station_id
        # The _station_id is private and immutable

    def current_temperature(self):
        "Latest hourly observation"
        # Do not cache this because old results
        # can be out of date.

    @cached_property
    def location(self):
        "Return the longitude/latitude coordinates of the station"
        # Result only depends on the station_id

    @lru_cache(maxsize=20)
    def historic_rainfall(self, date, units='mm'):
        "Rainfall on a given date"
        # Depends on the station_id, date, and units.

```

The example above takes for granted that the *station_id* stays fixed. Should the pertinent instance attributes be mutable, the `cached_property` route cannot be made to function, since it has no way to notice when those attributes change.

For the `lru_cache` route to function once the *station_id* is mutable, the class has to provide [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) and [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) methods, allowing the cache to register the relevant attribute changes:

```python
class Weather:
    "Example with a mutable station identifier"

    def __init__(self, station_id):
        self.station_id = station_id

    def change_station(self, station_id):
        self.station_id = station_id

    def __eq__(self, other):
        return self.station_id == other.station_id

    def __hash__(self):
        return hash(self.station_id)

    @lru_cache(maxsize=20)
    def historic_rainfall(self, date, units='cm'):
        'Rainfall on a given date'
        # Depends on the station_id, date, and units.

```

[Subject index](INDEX.md)

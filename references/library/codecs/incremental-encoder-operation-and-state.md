# codecs.IncrementalEncoder: `encode()`, `reset()`, `getstate()`, `setstate()`

encode(*object*, *final=False*)

Encodes *object* (taking the encoder's current state into account) and returns the resulting encoded object. When this is the final call to `encode()`, *final* must be true (its default is false).

 reset()

Restore the encoder to its starting state. Any output is thrown away: invoke `.encode(object, final=True)` — handing it an empty byte or text string where needed — both to clear the encoder and to retrieve the output.

 getstate()

Return the encoder's current state, which has to be an integer. The implementation should arrange for `0` to be the most common state. (A state more elaborate than an integer can be reduced to one by marshaling/pickling the state and then encoding the bytes of the resulting string into an integer.)

 setstate(*state*)

Put the encoder into the state given by *state*. That *state* has to be an encoder state that `getstate()` produced.

[Subject index](INDEX.md) · [Previous](codecs-incrementalencoder-class.md) · [Continue](codecs-incrementaldecoder-class.md) · [Owning module, declaration or section: codecs](codecs-encode-to-codecs-lookup.md) · [Owning module, declaration or section: codecs.IncrementalEncoder](codecs-incrementalencoder-class.md) · [Owning module, declaration or section: IncrementalEncoder Objects](codecs-incrementalencoder-class.md)

# codecs.IncrementalDecoder reset and state

 reset()

Return the decoder to its starting state.

 getstate()

Hand back the decoder's present state. The value has to be a two-item tuple: the first item holds the buffer with the input not yet decoded. The second has to be an integer that may carry extra state information. (Implementations ought to ensure that `0` serves as the most frequent extra state value.) When that extra state value equals `0`, it must be feasible to put the decoder into the state with nothing buffered and `0` for the extra state value, such that resupplying the formerly buffered input drives the decoder back to its prior state while emitting nothing. (Extra state information richer than plain integers can be folded into an integer by marshaling or pickling that information and then encoding the resulting string's bytes into an integer.)

 setstate(*state*)

Place the decoder into *state*. Here *state* has to be a decoder state that `getstate()` produced.

[Subject index](INDEX.md) · [Incremental decoder class](codecs-incrementaldecoder-class.md) · [Decode input](codecs-incrementaldecoder-decode.md) · [Stream encoding and decoding](stream-encoding-and-decoding.md)

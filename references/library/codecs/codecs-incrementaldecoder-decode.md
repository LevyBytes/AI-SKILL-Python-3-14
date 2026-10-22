# codecs.IncrementalDecoder.decode

decode(*object*, *final=False*)

Decodes *object* (factoring in where the decoder currently stands) and gives back the decoded object that results. When this represents the final invocation of `decode()`, *final* has to be true (false being the default). With *final* set true, the decoder is required to fully consume the input and empty every buffer. Should that prove unworkable (for instance, when truncated byte sequences sit at the input's tail) it has to begin error handling exactly as it would in the stateless case (which may throw an exception).

[Subject index](INDEX.md) · [Incremental decoder class](codecs-incrementaldecoder-class.md) · [Reset and state methods](incremental-decoder-reset-and-state.md)

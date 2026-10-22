# STRICT, CONFORM, EJECT and KEEP boundary modes

A fresh boundary mechanism now governs the treatment of out-of-range / invalid bits: `STRICT`, `CONFORM`, `EJECT`, and `KEEP`:

- STRICT –> raises an exception when presented with invalid values

- CONFORM –> discards any invalid bits

- EJECT –> drop Flag status, turning into an ordinary int that carries the supplied value

- KEEP –> keep the extra bits

  - keeps Flag status and extra bits

  - extra bits do not show up in iteration

  - extra bits do show up in repr() and str()

For Flag the default is `STRICT`, for `IntFlag` it is `EJECT`, and for `_convert_` it is `KEEP` (consult `ssl.Options` for a case where `KEEP` is required).

[Subject index](INDEX.md) · [IntFlag Color setup, canonical bits and pseudo-flag names](intflag-color-setup-canonical-bits-and-pseudo-flag-names.md) · [Flag aliases and containment](flag-aliases-and-containment.md) · [Previous source context](flag-aliases-and-containment.md) · [Following source context](how-are-enums-and-flags-different.md)

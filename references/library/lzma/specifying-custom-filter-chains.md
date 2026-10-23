# lzma - Specifying custom filter chains

### Specifying custom filter chains

What a filter chain specifier amounts to is a sequence of dictionaries, with each one holding the ID together with the options for a single filter. Every dictionary is required to carry the key `"id"`, and it may carry further keys that set filter-dependent options. The legal filter IDs run as follows:

- Compression filters:

  - `FILTER_LZMA1` (for use with `FORMAT_ALONE`)

  - `FILTER_LZMA2` (for use with `FORMAT_XZ` and `FORMAT_RAW`)

- Delta filter:

  - `FILTER_DELTA`

- Branch-Call-Jump (BCJ) filters:

  - `FILTER_X86`

  - `FILTER_IA64`

  - `FILTER_ARM`

  - `FILTER_ARMTHUMB`

  - `FILTER_POWERPC`

  -

`FILTER_SPARC`

Any filter chain may hold as many as 4 filters and is never allowed to be empty. Whatever sits last in the chain has to be a compression filter, while every other filter has to be either a delta or a BCJ filter.

The options below are available to compression filters (given as extra entries inside the dictionary that stands for the filter):

- `preset`: A compression preset that supplies default values for whichever options you leave unset.

- `dict_size`: Dictionary size in bytes. Pick a value from 4 KiB up to 1.5 GiB (inclusive).

- `lc`: Number of literal context bits.

- `lp`: Number of literal position bits. Their total, `lc + lp`, may not exceed 4.

- `pb`: Number of position bits; this too may not exceed 4.

- `mode`: `MODE_FAST` or `MODE_NORMAL`.

- `nice_len`: The length treated as a “nice length” when matching. Keep this at 273 or below.

- `mf`: What match finder to use – `MF_HC3`, `MF_HC4`, `MF_BT2`, `MF_BT3`, or `MF_BT4`.

- `depth`: The deepest search the match finder will perform. A value of 0 (the default) lets it choose automatically from the other filter options.

By recording byte-to-byte differences, the delta filter can hand the compressor more repetitive input under the right conditions. Its lone option is `dist`, which sets how far apart the bytes being subtracted are. With the default of 1, it takes the differences between neighbouring bytes.

The BCJ filters target machine code. They rewrite relative branches, calls and jumps so the code uses absolute addressing, the goal being to expose more redundancy for the compressor to exploit. Their single option, `start_offset`, names the address to be mapped onto the start of the input data, defaulting to 0.

[Subject index](INDEX.md) · [Previous](lzma-is-check-supported.md) · [Owning module, declaration or section: lzma](lzma-lzmaerror.md) · [Continue](examples.md)

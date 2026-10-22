# compression.zstd: `compression.zstd.ZstdDict`

*class *compression.zstd.ZstdDict(*dict_content*, */*, ***, *is_raw=False*)

A wrapper around Zstandard dictionaries. Dictionaries help you compress numerous small chunks of data more tightly. Reach for `train_dict()` when you need to train a fresh dictionary out of sample data.

The *dict_content* argument (a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object)), is the already trained dictionary information.

The *is_raw* argument, a boolean, is an advanced parameter that governs what *dict_content* signifies. `True` says *dict_content* is a ?raw content? dictionary, free of any format constraints. `False` says *dict_content* is an ordinary Zstandard dictionary, built by Zstandard functions such as `train_dict()` or by the external **zstd** CLI.

While handing a `ZstdDict` to a function, the `as_digested_dict` and `as_undigested_dict` attributes let you steer how the dictionary loads by passing them as the `zstd_dict` argument, for instance `compress(data, zstd_dict=zd.as_digested_dict)`. Digesting a dictionary is an expensive step that happens whenever a Zstandard dictionary loads. Across repeated compression or decompression calls, handing over a digested dictionary cuts the cost of loading the dictionary.

>   Difference for compression
|  | Digested dictionary | Undigested dictionary |
| --- | --- | --- |
| Compressor advanced parameters that the dictionary's own parameters may override | `window_log`, `hash_log`, `chain_log`, `search_log`, `min_match`, `target_length`, `strategy`, `enable_long_distance_matching`, `ldm_hash_log`, `ldm_min_match`, `ldm_bucket_size_log`, `ldm_hash_rate_log`, and some non-public parameters. | None |
| `ZstdDict` internally caches the dictionary | Yes. Reloading a digested dictionary at the same compression level runs faster. | No. Should you need an undigested dictionary loaded repeatedly, reuse a single compressor object instead. |

Where a `ZstdDict` arrives with no attribute set, an undigested dictionary goes through by default when compressing, and a digested dictionary is built if needed and goes through by default when decompressing.

>

 dict_content

The content of the Zstandard dictionary, a `bytes` object. It matches the *dict_content* argument from the `__init__` method. Other programs, such as the `zstd` CLI program, can consume it.

 dict_id

Identifier of the Zstandard dictionary, a non-negative int value.

A non-zero value marks the dictionary as ordinary, built by Zstandard functions and conforming to the Zstandard format.

`0` marks a ?raw content? dictionary that carries no format restriction at all and serves advanced users.

Note

What `0` signifies for `ZstdDict.dict_id` is not the same as the `dictionary_id` attribute on the `get_frame_info()` function.

 as_digested_dict

Load as a digested dictionary.

 as_undigested_dict

Load as an undigested dictionary.

[Subject index](INDEX.md) · [Previous](compression-zstd-train-dict-to-compression-zstd-finalize-dict.md) · [Continue](compression-zstd-compressionparameter-class.md) · [Owning module, declaration or section: Zstandard dictionaries](compression-zstd-train-dict-to-compression-zstd-finalize-dict.md)

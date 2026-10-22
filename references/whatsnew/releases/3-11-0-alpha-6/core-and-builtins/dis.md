# Python 3.11.0 alpha 6 / core and builtins / dis

[bpo-45923](https://bugs.python.org/issue?@action=redirect&bpo=45923): Provide a quickened variant of [`RESUME`](https://docs.python.org/3.14/library/dis.html#opcode-RESUME) that bypasses the quickening checks.

[bpo-46702](https://bugs.python.org/issue?@action=redirect&bpo=46702): Specialize [`UNPACK_SEQUENCE`](https://docs.python.org/3.14/library/dis.html#opcode-UNPACK_SEQUENCE) so [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) and [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) unpackings are handled directly.

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Correct mishandling of inline cache entries while specializing [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Use an oparg to make building helpful error messages simpler in [`GET_AWAITABLE`](https://docs.python.org/3.14/library/dis.html#opcode-GET_AWAITABLE).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Gather more granular specialization-failure stats for [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) trailed by [`EXTENDED_ARG`](https://docs.python.org/3.14/library/dis.html#opcode-EXTENDED_ARG).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Adopt inline caching for [`LOAD_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR), `LOAD_METHOD`, and [`STORE_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_ATTR).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Adopt inline caching for [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Adopt inline caching for [`UNPACK_SEQUENCE`](https://docs.python.org/3.14/library/dis.html#opcode-UNPACK_SEQUENCE).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Adopt an inline cache for [`LOAD_GLOBAL`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_GLOBAL).

[bpo-46072](https://bugs.python.org/issue?@action=redirect&bpo=46072): Gather richer specialization-failure statistics for [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP).

[bpo-46841](https://bugs.python.org/issue?@action=redirect&bpo=46841): Keep [`BINARY_OP`](https://docs.python.org/3.14/library/dis.html#opcode-BINARY_OP) caches inline by means of a new [`CACHE`](https://docs.python.org/3.14/library/dis.html#opcode-CACHE) instruction.

[bpo-44337](https://bugs.python.org/issue?@action=redirect&bpo=44337): Cut the memory footprint of the specialized [`LOAD_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR) and [`STORE_ATTR`](https://docs.python.org/3.14/library/dis.html#opcode-STORE_ATTR) instructions.

[bpo-45885](https://bugs.python.org/issue?@action=redirect&bpo=45885): Avoid un-adapting [`COMPARE_OP`](https://docs.python.org/3.14/library/dis.html#opcode-COMPARE_OP) while gathering specialization stats.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)

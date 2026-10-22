# --prefix=PREFIX

### 3.3.6. Install Options

 --prefix=PREFIX

Place architecture-independent files into PREFIX. Under Unix the default is `/usr/local`.

You can read this value back at runtime through [`sys.prefix`](https://docs.python.org/3.14/library/sys.html#sys.prefix).

For instance, `--prefix="$HOME/.local/"` will set up a Python within the user's home directory.

[Subject index](INDEX.md) · [Previous source section](enable-wasm-pthreads.md) · [Following source section](exec-prefix-eprefix.md)

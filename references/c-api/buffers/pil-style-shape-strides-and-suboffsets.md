# PIL-style: shape, strides and suboffsets

### PIL-style: shape, strides and suboffsets

Beyond the ordinary items, PIL-style arrays may hold pointers that have to be followed before the next element along a dimension can be reached. To illustrate, the ordinary three-dimensional C-array `char v[2][2][3]` can equally be regarded as an array of 2 pointers to 2 two-dimensional arrays: `char (*v[2])[2][3]`. Under suboffsets representation, those two pointers may sit at the start of `buf`, each pointing to a `char x[2][3]` array that may reside anywhere in memory.

Below is a function that, given an N-dimensional index, returns a pointer to the matching element of an N-D array when both non-`NULL` strides and suboffsets are present:

```c
void *get_item_pointer(int ndim, void *buf, Py_ssize_t *strides,
                       Py_ssize_t *suboffsets, Py_ssize_t *indices) {
    char *pointer = (char*)buf;
    int i;
    for (i = 0; i < ndim; i++) {
        pointer += strides[i] * indices[i];
        if (suboffsets[i] >=0 ) {
            pointer = *((char**)pointer) + suboffsets[i];
        }
    }
    return (void*)pointer;
}

```

[Subject index](INDEX.md) · [Previous source contract](numpy-style-shape-and-strides.md) · [Following source contract](pyobject-checkbuffer-to-pybuffer-fillcontiguousstrides.md)

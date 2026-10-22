# NumPy-style: shape and strides

### Complex arrays

### NumPy-style: shape and strides

For NumPy-style arrays, the logical structure is set by `itemsize`, `ndim`, `shape`, and `strides`.

When `ndim == 0`, whatever `buf` points at is read as a scalar of size `itemsize`. In that event, both `shape` and `strides` are `NULL`.

When `strides` is `NULL`, the array is read as an ordinary n-dimensional C-array. Otherwise, the consumer is to reach an n-dimensional array in this manner:

```c
ptr = (char *)buf + indices[0] * strides[0] + ... + indices[n-1] * strides[n-1];
item = *((typeof(item) *)ptr);

```

As mentioned earlier, `buf` may point at any spot within the real memory block. An exporter is able to confirm a buffer's validity using this function:

```python
def verify_structure(memlen, itemsize, ndim, shape, strides, offset):
    """Verify that the parameters represent a valid array within
       the bounds of the allocated memory:
           char *mem: start of the physical memory block
           memlen: length of the physical memory block
           offset: (char *)buf - mem
    """
    if offset % itemsize:
        return False
    if offset < 0 or offset+itemsize > memlen:
        return False
    if any(v % itemsize for v in strides):
        return False

    if ndim <= 0:
        return ndim == 0 and not shape and not strides
    if 0 in shape:
        return True

    imin = sum(strides[j]*(shape[j]-1) for j in range(ndim)
               if strides[j] <= 0)
    imax = sum(strides[j]*(shape[j]-1) for j in range(ndim)
               if strides[j] > 0)

    return 0 <= offset+imin and offset+imax+itemsize <= memlen

```

[Subject index](INDEX.md) · [Previous source contract](compound-requests.md) · [Following source contract](pil-style-shape-strides-and-suboffsets.md)

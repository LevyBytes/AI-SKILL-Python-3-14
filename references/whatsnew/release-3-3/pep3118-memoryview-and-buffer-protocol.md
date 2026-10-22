# What's New In Python 3.3 / PEP 3118: New memoryview implementation and buffer protocol documentation

### PEP 3118: New memoryview implementation and buffer protocol documentation

The [**PEP 3118**](https://peps.python.org/pep-3118/) implementation received a major overhaul.

This new memoryview code thoroughly resolves every ownership and lifetime problem with the dynamically allocated fields inside the Py_buffer struct, problems that had produced numerous crash reports. On top of that, a number of functions that previously crashed or gave wrong answers for non-contiguous or multi-dimensional input were corrected.

The memoryview object is now equipped with a PEP-3118 compliant getbufferproc() that inspects what request type the consumer made. A great many new capabilities were introduced, and most of them operate in full generality across non-contiguous arrays as well as arrays with suboffsets.

The docs were revised to lay out plainly what both exporters and consumers must do. The buffer request flags fall into basic and compound categories. How the memory of non-contiguous and multi-dimensional NumPy-style arrays is laid out gets explained as well.

[Subject index](INDEX.md) · [Previous source section](pep-420-implicit-namespace-packages.md) · [Next source section](features.md) · [Release/subject declaration](summary-release-highlights.md)

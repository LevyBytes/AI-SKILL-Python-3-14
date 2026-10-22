# slice.indices(*self*, *length*)

slice.indices(*self*, *length*)

Given one integer argument *length*, this method works out details about the slice that the slice object would denote were it applied to a sequence holding *length* items. A tuple of three integers comes back; these correspond, in order, to the *start* and *stop* indices together with the *step* (the stride length) of the slice. Indices that are missing or fall outside the bounds get treated the same way ordinary slices treat them.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Owning language section](slice-objects.md) · [Previous source section](slice-objects.md) · [Following source section](static-method-objects.md)

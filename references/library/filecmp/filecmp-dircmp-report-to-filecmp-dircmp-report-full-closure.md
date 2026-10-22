# filecmp.dircmp: `report()`, `report_partial_closure()`, `report_full_closure()`

report()

Write out (onto [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout)) how `a` and `b` compare.

 report_partial_closure()

Write out how `a` and `b` compare together with their shared first-level subdirectories.

 report_full_closure()

Write out how `a` and `b` compare along with their shared subdirectories, descending recursively.

A handful of useful attributes on the `dircmp` class let you pull assorted details about the directory trees under comparison.

Bear in mind that thanks to [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) hooks every attribute is worked out on demand, so you pay no performance cost as long as you stick to the cheap-to-compute ones.

 left

The directory *a*.

 right

The directory *b*.

 left_list

The contents of `a` — its files and subdirectories — after `hide` and `ignore` filtering.

 right_list

The contents of `b` — its files and subdirectories — after `hide` and `ignore` filtering.

 common

Whatever files and subdirectories `a` and `b` share.

 left_only

Files and subdirectories that exist solely in `a`.

 right_only

Files and subdirectories that exist solely in `b`.

 common_dirs

Subdirectories common to `a` and `b` alike.

 common_files

Files in both *a* and *b*.

 common_funny

Names present in `a` as well as `b` where either the type is not the same across the two directories or [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat) signals an error.

 same_files

Files that come out identical across `a` and `b` according to the class's own file-comparison operator.

 diff_files

Files found in both `a` and `b` whose contents diverge as judged by the class's file-comparison operator.

 funny_files

Files turning up in both `a` and `b` that nonetheless resisted comparison.

 subdirs

A dictionary that ties each name from `common_dirs` to a `dircmp` instance (or to MyDirCmp instances when this object happens to be a MyDirCmp, itself a subclass of `dircmp`).

Changed in version 3.10: Entries had always been `dircmp` instances before. They now take on the same type as `self`, provided `self` derives from `dircmp`.

[Subject index](INDEX.md) · [Previous](filecmp-dircmp-class.md) · [Continue](filecmp-default-ignores.md) · [Owning module, declaration or section: filecmp](filecmp-cmp-to-filecmp-clear-cache.md) · [Owning module, declaration or section: filecmp.dircmp](filecmp-dircmp-class.md) · [Owning module, declaration or section: The `dircmp` class](filecmp-dircmp-class.md)

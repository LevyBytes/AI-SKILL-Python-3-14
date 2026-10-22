# tkinter — The Packer

### The Packer

Among Tk’s geometry-management mechanisms is the packer. Geometry managers exist to lay out how widgets sit relative to one another inside their container. Set against the clunkier *placer* (seen less often, and skipped here), the packer accepts a qualitative description of the relationships - *above*, *to the left of*, *filling*, and so on - then figures out the precise placement coordinates on your behalf.

How large any container widget ends up is dictated by the size of the “content widgets” it holds. The packer governs where those content widgets land inside the container they are packed into. You can pack widgets within frames, and frames within still other frames, to build whatever layout you’re after. On top of that, once packed, the arrangement reflows on the fly to absorb piecemeal changes to the configuration.

Keep in mind a widget stays invisible until a geometry manager has assigned its geometry. Forgetting the geometry step is a frequent beginner slip, leaving people puzzled that the widget got created yet nothing shows. A widget surfaces only once something like the packer’s `pack()` method has been applied to it.

You can call the pack() method with keyword-option/value pairs that steer where the widget shows within its container and how it reacts as the main application window is resized. A few examples follow:

```python
fred.pack()                     # defaults to side = "top"
fred.pack(side="left")
fred.pack(expand=1)

```

[Subject index](INDEX.md) · [Previous](setting-options.md) · [Continue](packer-options.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)

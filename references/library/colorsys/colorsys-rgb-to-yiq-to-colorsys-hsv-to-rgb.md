# colorsys`colorsys` - Conversions between color systems

### `colorsys` - Conversions between color systems

**Source code:** [Lib/colorsys.py](https://github.com/python/cpython/tree/3.14/Lib/colorsys.py)

---

With `colorsys`, you can translate color values back and forth between the RGB (Red Green Blue) model — the one driving computer displays — and three alternative coordinate schemes: YIQ, HLS (Hue Lightness Saturation), and HSV (Hue Saturation Value). Every one of these color models uses floating-point numbers for its coordinates. For YIQ, the Y component falls within 0 and 1, whereas the I and Q components may take either sign. Across the remaining models, each coordinate stays within the 0-to-1 range.

See also

Further reading on color spaces is available at [https://poynton.ca/ColorFAQ.html](https://poynton.ca/ColorFAQ.html) and [https://www.cambridgeincolour.com/tutorials/color-spaces.htm](https://www.cambridgeincolour.com/tutorials/color-spaces.htm).

These are the functions exposed by the `colorsys` module:

 `colorsys.rgb_to_yiq(*r*, *g*, *b*)`

Turn an RGB-coordinate color into its YIQ-coordinate equivalent.

 `colorsys.yiq_to_rgb(*y*, *i*, *q*)`

Turn a YIQ-coordinate color into its RGB-coordinate equivalent.

 `colorsys.rgb_to_hls(*r*, *g*, *b*)`

Turn an RGB-coordinate color into its HLS-coordinate equivalent.

 `colorsys.hls_to_rgb(*h*, *l*, *s*)`

Turn an HLS-coordinate color into its RGB-coordinate equivalent.

 `colorsys.rgb_to_hsv(*r*, *g*, *b*)`

Turn an RGB-coordinate color into its HSV-coordinate equivalent.

 `colorsys.hsv_to_rgb(*h*, *s*, *v*)`

Turn an HSV-coordinate color into its RGB-coordinate equivalent.

Example:

```python
>>> import colorsys
>>> colorsys.rgb_to_hsv(0.2, 0.4, 0.4)
(0.5, 0.5, 0.4)
>>> colorsys.hsv_to_rgb(0.5, 0.5, 0.4)
(0.2, 0.4, 0.4)

```

[Subject index](INDEX.md) · [Previous](conversions-between-color-systems.md) · [Continue](../compileall/compileall-byte-compile-python-libraries.md)

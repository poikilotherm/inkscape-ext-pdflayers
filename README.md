# Inkscape Extension: Layers to multipage PDF

This is a small Inkscape 1.x+ extension to write layered SVG images as multipage PDF.

## Installation

Remember: this is an Inkscape **1.x** extension. It's not compatible with older
release like the famous 0.48 or 0.92 trains.

You can install via
`pip install --isolated --target ~/.config/inkscape/extensions git+https://github.com/poikilotherm/inkscape-ext-pdflayers.git`

## How to use

**Preparation**

When creating a SVG file with multiple layers, you can edit-lock layers.
(See [docs](https://wiki.inkscape.org/wiki/index.php?title=Layer_Dialog))

Those will be used as the "background" of every page. (So those layers should
actually be in the background / lower in the layer stack...)

Every other layer is added in order to the resulting PDF as a single page.

**Exporting**  

After installation of the extension, simply save your SVG drawing as a PDF
with the "one page per layer" option. Be prepared (read above).

## Credits

Thank you to the great inkscape community and [@sizmailov](https://github.com/sizmailov).
Thank you [@doctormo](https://github.com/doctormo) for a nice new extension API.
Your help on getting this little pioneer plugin going is very much appreciated!

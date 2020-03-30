#! /usr/bin/env python
# coding=utf-8
#
# Copyright 2020 Oliver Bertuch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
"""
Export layers to a multipage PDF file, using locked layers as backgrounds
for every page, adding one layer at a time.
"""

import inkex
from inkex.base import TempDirMixin
from inkex.command import take_snapshot

import PyPDF2

class Layers_Multipage_PDF_Export(TempFileMixin, inkex.OutputExtension):

    dir_prefix = 'multipagePDF-'

    def save(self, stream):
        # Init PDF merger
        pdf_merger = PyPDF2.PdfFileMerger()

        # Find layers.
        bg_layers = self.svg.xpath("//svg:g[@inkscape:groupmode='layer' and @sodipodi:insensitive='true']")
        layers = self.svg.xpath("//svg:g[@inkscape:groupmode='layer' and not(@sodipodi:insensitive)]")

        if len(layers) + len(bg_layers) < 1:
            inkex.errormsg("No layers found.")
            return

        for node in layers:
            # Make all layers invisible
            node.style['display'] = "none"

        # Iterate the layers, save to PDF.
        for node in layers:
            # Show only one layer at a time.
            node.style.update("display:inherit;opacity:1")

            name = node.get('inkscape:label')
            newname = "{}.{}".format(name, 'pdf')
            # Save snapshot as PDF export in temp file
            filename = take_snapshot(self.document, dirname=self.tempdir,
                                        name=name, ext='pdf')
            # Append temp PDF to merged PDF
            pdf_merger.append(filename, bookmark=name)

            node.style['display'] = "none"

        # Write out merged PDF to destination
        pdf_merger.write(stream)


if __name__ == '__main__':
    Layers_Multipage_PDF_Export().run()

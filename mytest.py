#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Display the Raspberry Pi logo (loads image as .png).
"""
import os
import os.path
from demo_opts import get_device
from PIL import Image


def main():
    while True:
        img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        './', 'desktop-thumb.png'))
        logo = Image.open(img_path).convert("RGBA")
        fff = Image.new(logo.mode, logo.size, (255,) * 4)
        background = Image.new("RGBA", device.size, "white")
        posn = ((device.width - logo.width) // 2, 0)
        cmd="scrot desktop.png -t 9"
        os.system(cmd)
        rot = logo.rotate(0, resample=Image.BILINEAR)
        img = Image.composite(rot, fff, rot)
        background.paste(img, posn)
        device.display(background.convert(device.mode))


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass

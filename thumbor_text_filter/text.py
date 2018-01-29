#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
from thumbor.filters import BaseFilter, filter_method
import webcolors

class Filter(BaseFilter):
    @filter_method(
        BaseFilter.String, # word
        BaseFilter.PositiveNumber, # position_x
        BaseFilter.PositiveNumber, # position_y
        BaseFilter.String, # text_color
        BaseFilter.PositiveNumber, # font_size
        BaseFilter.PositiveNumber, # padding_x
        BaseFilter.PositiveNumber, # padding_y
        BaseFilter.String, # background_color
        BaseFilter.PositiveNumber, # transparency
        BaseFilter.String # font_family
    )
    def text(self, word, position_x, position_y, text_color, font_size, padding_x, padding_y, background_color, transparency, font_family):
        image = self.engine.image.convert("RGB")
        usr_font = ImageFont.truetype(font_family, font_size)
        drawer = ImageDraw.Draw(image, 'RGBA')
        textsize = drawer.textsize(word, usr_font)

        text_color = webcolors.hex_to_rgb('#' + text_color)
        background_color = webcolors.hex_to_rgb('#' + background_color)

        drawer.rectangle([position_x - padding_x, position_y - padding_y, position_x + textsize[0] + padding_x, position_y + textsize[1] + padding_y], fill=(background_color[0], background_color[1], background_color[2], transparency), outline=None)
        drawer.text((position_x, position_y), word, fill=text_color, font=usr_font)
        self.engine.image = image

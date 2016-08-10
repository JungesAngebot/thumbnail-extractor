from colorthief import ColorThief


""" This module performs analysis of given images.

Analysis:
- detect dominant color
- detect faces in an image
"""


def determine_dominant_color_for_images(images):
    for image in images:
        color_thief = ColorThief(image.image_name)
        dominant_color = 'nocolor'
        try:
            dominant_color = color_thief.get_color(quality=1)
        except:
            pass
        image.dominant_color = dominant_color


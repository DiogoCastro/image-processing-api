import os
from PIL import Image


def image_debug(img):
    print(f'[IMAGE FILENAME]{img.filename}')
    print(f'[IMAGE FORMAT]  {img.format}')
    print(f'[IMAGE MODE]    {img.mode}')
    print(f'[IMAGE SIZE]    {img.size}')
    print(f'[IMAGE PALETTE] {img.palette}')


def file_exists(file):
    if os.path.isfile(file):
        os.remove(file)


def merge_image(image, water_mark):
    image = Image.open(image)
    logo = Image.open(water_mark)
    image_copy = image.copy()
    position = (
        (image_copy.width - logo.width),
        (image_copy.height - logo.height),
    )
    image_copy.paste(logo, position, logo)
    file_exists(image_copy)
    image_copy.save('pasted_image.jpg')
    return image_copy


# image.thumbnail((1200, 800))

# box = (200, 300, 700, 600)  # Coordinates are (left, upper, right, lower)

# cropped_image = image.crop(box)

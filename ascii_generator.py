from __future__ import print_function

from PIL import Image

if __name__ == '__main__':
    ascii_table = Image.open('ascii.bmp')
    start_width = 76
    start_height = 26
    tile_size = 24
    ascii_code = 32
    
    for i in range(6):
        for k in range(16):
            width = start_width + i * (tile_size + 1)
            height = start_height + k * (tile_size + 1)
            tile = ascii_table.crop((width, height, width + tile_size, height + tile_size))
            tile.save('ascii{}.jpg'.format(ascii_code))
            ascii_code += 1



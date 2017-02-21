from __future__ import print_function

from PIL import Image

if __name__ == '__main__':
    start_width = 76
    start_height = 26
    tile_size = 24
    tiles = []

    # partition ascii table
    ascii_table = Image.open('ascii.bmp') 
    for i in range(6):
        for k in range(16):
            width = start_width + i * (tile_size + 1)
            height = start_height + k * (tile_size + 1)
            tile = ascii_table.crop((width, height, width + tile_size, height + tile_size))
            tiles.append(tile)

    # convert from noritake itron format to 5x7 format
    ascii_offset = 32
    for i in range(len(tiles)):
        dot_matrix = Image.new('RGB', (7, 9), (255, 255, 255))
#        tiles[i].save('ascii{}.jpg'.format(i + ascii_offset))

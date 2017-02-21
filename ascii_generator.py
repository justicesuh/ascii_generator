from __future__ import print_function

from PIL import Image

if __name__ == '__main__':
    start_width = 76
    start_height = 26
    tile_size = 24
    tiles = []

    # partition ascii table
    ascii_table = Image.open('ascii.bmp') 
    for col in range(6):
        for row in range(16):
            width = start_width + col * (tile_size + 1)
            height = start_height + row * (tile_size + 1)
            tile = ascii_table.convert('RGB').crop((width + 5, height + 2, width + tile_size - 5, height + tile_size - 2))
            tiles.append(tile)

    # convert from noritake itron format to 5x7 format
    ascii_offset = 32
    BLACK = (0, 0, 0)
    for i in range(len(tiles)):
        dot_matrix = Image.new('RGB', (7, 9), (255, 255, 255))
        pixel_dot_matrix = dot_matrix.load()
        pixel_tile = tiles[i].load()
        print(ascii_offset + i)
        for col in range(5):
            for row in range(7):
                x = col * 3 + 1
                y = row * 3 + 1
                if pixel_tile[x - 1, y - 1] == BLACK and pixel_tile[x, y - 1] == BLACK and pixel_tile[x - 1, y] == BLACK and pixel_tile[x, y] == BLACK:
                    pixel_dot_matrix[col + 1, row + 1] = BLACK
                    print(ascii_offset + i, col + 1, row + 1)
        tiles[i] = dot_matrix
        tiles[i].save('ascii{}.jpg'.format(i + ascii_offset))

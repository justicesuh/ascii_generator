from __future__ import print_function

from PIL import Image

if __name__ == '__main__':
    start_width = 76 # this skips the low nibble header and the two control columns
    start_height = 26 # skip high nibble header
    tile_size = 24
    tiles = []

    # partition ascii table
    ascii_table = Image.open('ascii.bmp') # from http://www.noritake-itron.com/NewWeb/CVFD/CVFDCust.shtml
    for col in range(6): # there are 6 columns of standard ascii characters
        for row in range(16): # 16 rows in the ascii table
            width = start_width + col * (tile_size + 1)
            height = start_height + row * (tile_size + 1)
            tile = ascii_table.convert('RGB').crop((width + 5, height + 2, width + tile_size - 5, height + tile_size - 2))
            tiles.append(tile)

    # convert from noritake itron format to .graphic file
    ascii_offset = 32 # x20, skip all control characters
    BLACK = (0, 0, 0)
    for i in range(len(tiles)):
        pixel_tile = tiles[i].load()
        code = hex(ascii_offset + i)[2:]
        graphic = open('x{}.graphic'.format(code), 'w+')

        # .graphic files are 7x9, but noritake itron are 5x7
        # pad the font with white border
        graphic.write('x{}row{}:\t.FILL x7fff\n'.format(code, 0))
        for col in range(6):
            graphic.write('\t\t.FILL x7fff\n')
        graphic.write('\n')

        for row in range(7):
            graphic.write('x{}row{}:\t.FILL x7fff\n'.format(code, row + 1))
            for col in range(5):
                x = col * 3 + 1
                y = row * 3 + 1
                # noritake itron "pixels" are 2x2
                if pixel_tile[x - 1, y - 1] == BLACK and pixel_tile[x, y - 1] == BLACK and pixel_tile[x - 1, y] == BLACK and pixel_tile[x, y] == BLACK:
                    graphic.write('\t\t.FILL x7c00\n')
                else:
                    graphic.write('\t\t.FILL x7fff\n')
            graphic.write('\t\t.FILL x7fff\n\n')

        # ditto here 
        graphic.write('x{}row{}:\t.FILL x7fff\n'.format(code, 8))
        for col in range(6):
            graphic.write('\t\t.FILL x7fff\n')

        graphic.close()

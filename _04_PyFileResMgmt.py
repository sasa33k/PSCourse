"""
open()
- file: path to file (required)
- mode: read/write/apend, binary/text e.g. wt = write string
r-reading,w0writing, trancating the file first, x-open for exclusive creating, fail if already exist, a-write&append
b-binary, t-text
+ open a disk file for updating (r&w), U- universal newline mode(for backwards compatibility)
- encoding: text encoding  else : import sys, sys.getdefaultencoding()

files - series of bytes

text - encode & decode, universal newlines \n // \r\n

write(), line sep by \n, no writeline  ** close to store it?
but have writelines(['a\n','b\n'])
read(#char), read() - all remaining
seek(0) - back to beginning
readline()
readlines() ==> [] list



with_blocks - resource cleanup with context-managers
*open() returns a context-manager, remove need of explicit close()

import sys
def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [ int(line.strip()) for line in f ]
    finally:
        f.close()

VS

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f ]


with urlopen('xxx') as web_file:
type(web_file) --> httpResponase (instead of IO..)
(file like objects)

from contextlib import closing --> always execute close() for ur defined class

raise RuntimeError("XXX")

help() can be used on instance objects, & types..
"""


"""Module for demonstrating files."""

import sys

def main(filename):
  f = open(filename, mode='rt', encoding='utf-8')
  for line in f:
      sys.stdout.write(line)  #vs print(line) --> hv \n and print ==> double line spacing
  f.close()

if __name__ == '__main__':
  main(sys.argv[1])



## bmp files

"""A module for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    2D list

    Args:
        filename: The name of the BMP file to me created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.

    Raises:
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp: # no need encoding for binary file la
        # BMP Header
        bmp.write(b'BM') # byte object

        size_bookmark = bmp.tell()      # The next four bytes hold the filesize as a 32-bit
        # tell method for file object as we dunno the size yet, offeset from the beginning of file
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next four bytes hold the integer offset
        bmp.write(b'\x00\x00\x00\x00')      # to the pixel data. Zero placeholder for now.

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')  # Image header size in bytes - 40 decimal (whole header 40 bytes)
        bmp.write(_int32_to_bytes(width))   # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')          # Number of image planes
        bmp.write(b'\x08\x00')          # Bits per pixel 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):  # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark) # back to the places .tell() bookmark
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    # bit-wise shift and bit-wise &, >> right-shift by specified # of bits
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def _bytes_to_int32(b):
    """Convert a bytes object containing four bytes into an integer."""
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.

    Args:
        filename: The filename of a BMP file.

    Returns:
        A tuple containing two integers with the width
        and height in pixels.

    Raises:
        ValueError: If the file was not a BMP file.
        OSError: If there was a problem reading the file.
    """

    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))



#!/usr/bin/python3

'''
Author: Hayssam Noweir
Written: 26.01.2020
Description: Amazon BIF image extractor
Licensed under the MIT license, see LICENSE for details
'''

import os
import sys
import struct
from Bif import Bif

def usage():
    return print("usage: %s path/to/amazon_file.bif" % sys.argv[0])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Provided file not found.", file=sys.stderr)
        exit(1)

    bifObj = Bif()
    bifObj.openBif(sys.argv[1])
    if not bifObj.verifyBif():
        print("File seems not to be valid BIF.", file=sys.stderr)
        exit(1)

    bifObj.get_mapping()
    bifObj.extract_images()

    print("%s images with multiplier of %s milliseconds." % (bifObj.img_count, bifObj.img_multiplier))

    bifObj.closeBif()


'''
Author: Hayssam Noweir
Written: 26.01.2020
Description: Amazon BIF image extractor
Licensed under the MIT license, see LICENSE for details
'''
import struct
import os
class Bif():

    def __init__(self):
        self.__fObj = None

    def openBif(self, file):
        if os.path.isfile(file):
            self.__fObj = open(file, "rb")
            self.filesize = os.path.getsize(file)

    def closeBif(self):
        if self.__fObj != None:
            self.__fObj.close()

    def readBif(self, offset, size):
        self.__fObj.seek(offset)
        return self.__fObj.read(size)

    def readInt(self,  offset):
        return struct.unpack('i', self.readBif(offset, 4))[0]

    def extract_images(self):
        i = 0
        while i < len(self.mapping_dict) :
            fw = open("img_%s.jpg" % self.mapping_dict[i]['positionMillis'], "wb")
            if i == len(self.mapping_dict)-1:
                bd = self.readBif(
                    self.mapping_dict[i]['offsetBytes'], self.filesize-self.mapping_dict[i]['offsetBytes'])
            else:
                bd = self.readBif(self.mapping_dict[i]['offsetBytes'], self.mapping_dict[i+1]
                                  ['offsetBytes']-self.mapping_dict[i]['offsetBytes'])
            fw.write(bd)
            fw.close()
            i += 1

    def verifyBif(self):
        return struct.unpack('3s', self.readBif(1, 3))[0] == bytes("BIF", 'ascii')

    def get_mapping(self):
        self.img_count = self.readInt(12)
        self.img_multiplier = self.readInt(16)
        self.mapping_dict, l, u = [], 64, 1
        while u <= self.img_count:
            c = self.readInt(l) * self.img_multiplier
            d = self.readInt(l+4)
            self.mapping_dict.append({"positionMillis": c,  "offsetBytes": d})
            u += 1
            l += 8


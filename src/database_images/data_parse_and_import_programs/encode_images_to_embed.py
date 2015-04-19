'''
  Copyright (C) 2015 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

import base64
import os

"""
encoded = base64.b64encode('data to be encoded')
#encoded 'ZGF0YSB0byBiZSBlbmNvZGVk'
print encoded
data = base64.b64decode(encoded)
#data
print data
"""

fin = open("images.txt", "w")
fin.write("embed_image_data = {")
path="..\\images_to_embed\\flags"  # insert the path to the directory of interest
dirList=os.listdir(path)
for fname in dirList:
    iconfile = open(path + "\\" + fname,"rb")
    icondata = iconfile.read()
    icondata = base64.b64encode(icondata)
    fin.write("\"flag_" + fname.split(".")[0] + "\": \"" + icondata + "\",")
path="..\\images_to_embed\\os"  # insert the path to the directory of interest
dirList=os.listdir(path)
for fname in dirList:
    iconfile = open(path + "\\" + fname,"rb")
    icondata = iconfile.read()
    icondata = base64.b64encode(icondata)
    fin.write("\"os_" + fname.split(".")[0] + "\": \"" + icondata + "\",")
fin.write("}")
fin.close()
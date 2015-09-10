# Copyright (C) 2015 AndroidFire@xda <sahidalmas@gmail.com>
__author__ = 'Sahid Almas'

import urllib.request
import zipfile


def print_header():
    print(""
          "\n             ++------++          " +
          "         +-+___________\n            / /      \\ \\  " +
          "                | |__________ |\n           / /     " +
          "   \\ \\                 | |\n          / /       " +
          "   \\ \\                | |_______\n         / /   " +
          "         \\ \\               |  _______|\n       " +
          " / / ============ \\ \\              | |\n       / / ===============\\ \\  " +
          "           | |\n      / /                  \\ \\        " +
          "    | |\n     / /                    \\ \\         " +
          "  | |\n    / /  " +
          "                    \\ \\          | |\n   ~ ~           " +
          "            ~ ~          ~ ~\n\n   A HUMAN BEING FROM INDIA TO THE WORLD"
          "")
    return


print_header()
num = [1,22,23,24,25,22,33,34,36,37,38,39,40,
       41,42,43,45,50,60,77,90,99,100]
print(" \n Program to fetch translations and set to there own place")
link = input("Enter the link of zip file :")

urllib.request.urlretrieve(link, "androidfire.zip")
for a in num:
    print("Downloading "+str(a))
fh = open("androidfire.zip", "rb")
zip = zipfile.ZipFile(fh)

for name in zip.namelist():
    zip.extract(name, "res/")
    fh.close()
print("Good bye Have nice day")

import urllib.request
import sys
import re
import os

def download(url, title):
    urllib.request.urlretrieve(url,"{0}".format(title))

def findimages(s):
    return re.findall('!\[.{1,}\]\(.{1,}\)', s)

def geturl(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<link>', s)

def getfile(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<file>', s)

def replaceimageblock(text, url, path):
    return text.replace(url, path)

def downloadmarkdownpage(url, path):   
    # download .md
    download(url, path)

    # download images and replace image source path
    with open(path, 'r+') as file:
        text = file.read()
        directory = os.path.dirname(path)
        imageblocks = findimages(text)
        for block in imageblocks:
            imageurl = geturl(block)
            imagetitle = getfile(block)
            # download image
            download(imageurl, directory + os.sep + imagetitle)
            # replace image source path
            text = replaceimageblock(text, imageurl, imagetitle)
        # uodate file
        file.write(text)


if __name__ == "__main__":
    # help menu
    if sys.argv[1] == '-h':
        print('Input $ main.py URL path')
        exit()

    # Arguments check
    if len(sys.argv) != 3:
        print('Argument error')
        exit()

    
    #--------------------------
    # main
    #--------------------------
    
    # read arguments
    url = sys.argv[1]
    path = sys.argv[2]

    downloadmarkdownpage(url, path)
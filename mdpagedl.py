import urllib.request
import re
import os

def __downloadfile(url, title):
    urllib.request.urlretrieve(url,"{0}".format(title))

def __findimages(s):
    return re.findall('!\[.{1,}\]\(.{1,}\)', s)

def __geturl(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<link>', s)

def __getfile(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<file>', s)

def __replaceimageblock(text, url, path):
    return text.replace(url, path)

def download(url, path):   
    # download .md
    __downloadfile(url, path)

    # download images and replace image source path
    with open(path, 'r+') as file:
        text = file.read()
        directory = os.path.dirname(path)
        imageblocks = __findimages(text)
        for block in imageblocks:
            imageurl = __geturl(block)
            imagetitle = __getfile(block)
            # download image
            __downloadfile(imageurl, directory + os.sep + imagetitle)
            # replace image source path
            text = __replaceimageblock(text, imageurl, imagetitle)
        # uodate file
        file.write(text)

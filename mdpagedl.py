import urllib.request
import re
import os

def __download_file(url, title):
    urllib.request.urlretrieve(url,"{0}".format(title))

def __find_images(s):
    return re.findall('!\[.{1,}\]\(.{1,}\)', s)

def __get_url(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<link>', s)

def __get_file(s):
    return re.sub('!\[(?P<file>.{1,})\]\((?P<link>.{1,})\)', '\g<file>', s)

def __replace_image_block(text, url, path):
    return text.replace(url, path)

def download(url, path):   
    # download .md
    __download_file(url, path)

    # download images and replace image source path
    with open(path, 'r+') as file:
        text = file.read()
        directory = os.path.dirname(path)
        imageblocks = __find_images(text)
        for block in imageblocks:
            imageurl = __get_url(block)
            imagetitle = __get_file(block)
            # download image
            __download_file(imageurl, directory + os.sep + imagetitle)
            # replace image source path
            text = __replace_image_block(text, imageurl, imagetitle)
        # uodate file
        file.write(text)

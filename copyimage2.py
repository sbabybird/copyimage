#!/usr/bin/env python
# -*- coding:gbk -*-
""" 
复制指定目录的照片到目标目录，并且根据照片的拍摄时间进行重命名
比如某张照片拍摄于2008年3月15日12:00:00，则目标目录为2008\\03\\15\\120000.jpg
"""
from PIL import Image
import os, sys

def getdistpath(str, distdir):
    date = str.split(' ')[0].split(':')
    dirs = distdir + '\\' + '\\'.join(date)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    dirs = dirs + '\\' + ''.join(str.split(' ')[1].split(':')) + '.jpg'
    return dirs

def copyimage(srcdir, distdir):
    for root, dirs, files in os.walk(srcdir):
        for dir in dirs:
            for file in files:
                imgpath = root+'\\'+file
                print imgpath
                try:
                    image = Image.open(imgpath)
                except:
                    print 'file open error:', imgpath
                
                try:
                    distpath = getdistpath(image._getexif()[306], distdir)
                except:
                    print 'getexif error:', imgpath
                try:
                    if not os.path.exists(distpath):
                        image.save(distpath)
                        del image
                except:
                    print 'file copy error:', imgpath
                    del image

def main():
    if len(sys.argv) == 3:
        copyimage(sys.argv[1], sys.argv[2])
    else:
        print '需要给出两个参数，第一个是照片目录，第二个是目标目录'
        print '例如：', sys.argv[0],'e:\\photo f:\\goodphoto'


if __name__ == '__main__':
    main()

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
    dirs = distdir + os.sep + os.sep.join(date)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    dirs = dirs + os.sep + ''.join(str.split(' ')[1].split(':')) + '.jpg'
    return dirs

def copyimage(srcdir, distdir):
    for path in [srcdir+os.sep+i for i in os.listdir(srcdir)]:
        if os.path.isdir(path):
            copyimage(path, distdir)
        else:
            writelog(path)
            try:
                image = Image.open(path)
            except:
                logstr = 'file open error:' + path
                writelog(logstr)
            try:
                distpath = getdistpath(image._getexif()[306], distdir)
                logstr = 'distpath:' + distpath
                writelog(logstr)
            except:
                logstr = 'getextif error:' + path
                writelog(logstr)
            try:
                if not os.path.exists(distpath):
                    image.save(distpath)
            except:
                logstr = 'file copy error:' + path
                writelog(logstr)

def writelog(str):
    global logfile
    logfile.write(str+'\n')
    print str

def main():
    if len(sys.argv) == 3:
        global logfile
        logfile = open('cilog.txt', 'w')
        copyimage(sys.argv[1], sys.argv[2])
        logfile.close()
    else:
        print '需要给出两个参数，第一个是照片目录，第二个是目标目录'
        print '例如：', sys.argv[0],'e:\\photo f:\\goodphoto'


if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding:gbk -*-
""" 
����ָ��Ŀ¼����Ƭ��Ŀ��Ŀ¼�����Ҹ�����Ƭ������ʱ�����������
����ĳ����Ƭ������2008��3��15��12:00:00����Ŀ��Ŀ¼Ϊ2008\\03\\15\\120000.jpg
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
        print '��Ҫ����������������һ������ƬĿ¼���ڶ�����Ŀ��Ŀ¼'
        print '���磺', sys.argv[0],'e:\\photo f:\\goodphoto'


if __name__ == '__main__':
    main()


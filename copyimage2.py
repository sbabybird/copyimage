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
        print '��Ҫ����������������һ������ƬĿ¼���ڶ�����Ŀ��Ŀ¼'
        print '���磺', sys.argv[0],'e:\\photo f:\\goodphoto'


if __name__ == '__main__':
    main()

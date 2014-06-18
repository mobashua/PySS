#-*- coding:UTF-8 -*-

import zipfile
# parses flags and optional parameters 
import optparse
# utilisation de thread
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print "[+] Found password "+ password +"\n"
    except:
        pass

def main():
    """<Version 1> avec thread, sans optparse
    zFile=zipfile.ZipFile('2_evil.zip')
    passFile=open('dictionary.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
    </Version 1> """
    parser=optparse.OptionParser("usage%prog "+\
                                 "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
    zFile=zipfile.ZipFile(zname)
    passFile=open(dname)
    for line in passFile.readlines():
        password=line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
                
    
if __name__ == "__main__":
    main()

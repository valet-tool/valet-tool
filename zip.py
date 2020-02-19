from datetime import datetime
import time as time
import os
import tarfile
import csv

import psutil


def zip_file(url):
    starttime = time.time()
    tar = tarfile.open("myzipfile.tar.gz", "w:gz")
    for dirname, subdirs, files in os.walk('LibreOffice_6.2.8.2_Linux_x86_deb'):
        tar.add(dirname)
        for filename in files:
            tar.add(os.path.join(dirname, filename))
    tar.close()
    print("File Zipped")
    endtime = time.time()
    dateTimeObj = datetime.now()

    if (url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (url == 'http://ftp-srv2.kddilabs.jp/office/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 2
    elif (url == 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 3
    elif (url == 'https://download.nus.edu.sg/mirror/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (url =='https://tdf.c3sl.ufpr.br/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 5
    elif (url == 'https://mirror-hk.koddos.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 6
    elif (url == 'http://mirrors.coreix.net/thedocumentfoundation/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 7
    elif (url == 'https://mirror.aarnet.edu.au/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 8
    elif (url == 'http://tdf.saix.net/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 9

    reliability = 1
    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow([dateTimeObj, flag, "3", (str)(endtime - starttime),psutil.cpu_percent(),reliability])




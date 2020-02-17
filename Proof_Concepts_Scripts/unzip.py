from datetime import datetime
import tarfile
import time as time
import csv

import psutil


def unzipfile(url):
    starttime = time.time()
    fname = 'zip_file.tar.gz'
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        tar.close()
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        tar.close()
    print("File unzipped")
    endtime = time.time()
    dateTimeObj = datetime.now()

    if (url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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
        writer.writerow([dateTimeObj, flag, "2" , (str)(endtime - starttime),psutil.cpu_percent(),reliability])






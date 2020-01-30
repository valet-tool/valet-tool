from __future__ import print_function
from datetime import datetime
import requests
import time as time
import csv
import psutil



def download_file(url):
    starttime = time.time()
    results = requests.get(url)
    open('/Users/sakshikarnawat/PycharmProjects/data/zip_file.tar.gz', 'wb').write(results.content)
    print("File downloaded")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'http://ftp-srv2.kddilabs.jp/office/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 2
    elif (url == 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 3
    elif (
            url == 'https://download.nus.edu.sg/mirror/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (url == 'https://tdf.c3sl.ufpr.br/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 5
    elif (
            url == 'https://mirror-hk.koddos.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 6
    elif (
            url == 'http://mirrors.coreix.net/thedocumentfoundation/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 7
    elif (
            url == 'https://mirror.aarnet.edu.au/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 8
    elif (url == 'http://tdf.saix.net/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 9


    if final_time > 60.00:
        final_time = -1

    reliability = 1

    if final_time == -1:
        reliability= 0

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow([dateTimeObj, flag, "1", (str)(final_time), psutil.cpu_percent(),reliability])


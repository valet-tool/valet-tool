from __future__ import print_function
import shutil
from datetime import datetime
import requests
import time as time
import csv
import psutil
import tarfile
import os


def download_file(url):
    starttime = time.time()
    results = requests.get(url)
    open('zip_file.tar.gz', 'wb').write(results.content)
    print("File downloaded")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()
    current_time = dateTimeObj.strftime("%H:%M:%S")

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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
        reliability = 0

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow([dateTimeObj, current_time, flag, "1", (str)(final_time), psutil.cpu_percent(), reliability])


def unzipfile(url):
    starttime = time.time()
    fname = 'zip_file.tar.gz'
    if fname.endswith("tar.gz"):
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
    current_time = dateTimeObj.strftime("%H:%M:%S")

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(
            [dateTimeObj, current_time, flag, "2", (str)(endtime - starttime), psutil.cpu_percent(), reliability])


def grep_file(url):
    starttime = time.time()
    with open('LibreOffice_6.2.8.2_Linux_x86_deb/readmes/README_en-US', 'r') as f:
        for line in f.readlines():
            if 'Installation' in line:
                print("File grep complete")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    if final_time == -1:
        reliability = 0

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow([dateTimeObj, flag, "3", (str)(final_time), psutil.cpu_percent(), reliability])


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
    current_time = dateTimeObj.strftime("%H:%M:%S")

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1
    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(
            [dateTimeObj, current_time, flag, "4", (str)(endtime - starttime), psutil.cpu_percent(), reliability])


def delete_file(url):
    starttime = time.time()
    os.remove("zip_file.tar.gz")
    os.remove("myzipfile.tar.gz")
    shutil.rmtree('LibreOffice_6.2.8.2_Linux_x86_deb')
    print("Files deleted")
    endtime = time.time()
    dateTimeObj = datetime.now()
    current_time = dateTimeObj.strftime("%H:%M:%S")

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1
    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(
            [dateTimeObj, current_time, flag, "5", (str)(endtime - starttime), psutil.cpu_percent(), reliability])


pointer = True
while pointer == True:
    flag = True
    print("Location 1")
    location1 = 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location1)
        # if r.status_code == 200:
        download_file(location1)
        unzipfile(location1)
        grep_file(location1)
        zip_file(location1)
        delete_file(location1)
        flag = False

    print("Location 2")
    flag = True
    location2 = 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location2)
        # if r.status_code == 200:
        download_file(location2)
        unzipfile(location2)
        grep_file(location2)
        zip_file(location2)
        delete_file(location2)
        flag = False

    print("Location 3")
    flag = True
    location3 = 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location3)
        # if r.status_code == 200:
        download_file(location3)
        unzipfile(location3)
        grep_file(location3)
        zip_file(location3)
        delete_file(location3)
        flag = False

    print("Location 4")
    flag = True
    location4 = 'https://download.nus.edu.sg/mirror/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location4)
        # if r.status_code == 200:
        download_file(location4)
        unzipfile(location4)
        grep_file(location4)
        zip_file(location4)
        delete_file(location4)
        flag = False

    print("Location 5")
    flag = True
    location5 = 'https://tdf.c3sl.ufpr.br/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location5)
        # if r.status_code == 200:
        download_file(location5)
        unzipfile(location5)
        grep_file(location5)
        zip_file(location5)
        delete_file(location5)
        flag = False

    print("Location 6")
    flag = True
    location6 = 'https://mirror-hk.koddos.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.head(location5)
        # if r.status_code == 200:
        download_file(location6)
        unzipfile(location6)
        grep_file(location6)
        zip_file(location6)
        delete_file(location6)
        flag = False

    print("Location 7")
    flag = True
    location7 = 'http://mirrors.coreix.net/thedocumentfoundation/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location7)
        # if r.status_code == 200:
        download_file(location7)
        unzipfile(location7)
        grep_file(location7)
        zip_file(location7)
        delete_file(location7)
        flag = False

    print("Location 8")
    flag = True
    location8 = 'https://mirror.aarnet.edu.au/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        # r = requests.get(location8)
        # if r.status_code == 200:
        download_file(location8)
        unzipfile(location8)
        grep_file(location8)
        zip_file(location8)
        delete_file(location8)
        flag = False


from download import download_file
from unzip import unzipfile
import grep
from zip import zip_file
from delete import delete_file

pointer = True
while pointer == True:
    flag = True
    print("Location 1")
    location1 = 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location1)
        unzipfile(location1)
        zip_file(location1)
        delete_file(location1)
        flag = False
    print("Location 2")
    flag = True
    location2 = 'https://ftp.tu-chemnitz.de/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location2)
        unzipfile(location2)
        zip_file(location2)
        delete_file(location2)
        flag = False
    print("Location 3")
    flag = True
    location3 = 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location3)
        unzipfile(location3)
        zip_file(location3)
        delete_file(location3)
        flag = False
    print("Location 4")
    flag = True
    location4 = 'https://download.nus.edu.sg/mirror/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location4)
        unzipfile(location4)
        zip_file(location4)
        delete_file(location4)
        flag = False
    print("Location 5")
    flag = True
    location5 = 'https://tdf.c3sl.ufpr.br/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location5)
        unzipfile(location5)
        zip_file(location5)
        delete_file(location5)
        flag = False
    print("Location 6")
    flag = True
    location6 = 'https://mirror-hk.koddos.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location6)
        unzipfile(location6)
        zip_file(location6)
        delete_file(location6)
        flag = False
    print("Location 7")
    flag = True
    location7 = 'http://mirrors.coreix.net/thedocumentfoundation/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location7)
        unzipfile(location7)
        zip_file(location7)
        delete_file(location7)
        flag = False
    print("Location 8")
    flag = True
    location8 = 'https://mirror.aarnet.edu.au/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location8)
        unzipfile(location8)
        zip_file(location8)
        delete_file(location8)
        flag = False
    print("Location 9")
    flag = True
    location9 = 'http://tdf.saix.net/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
    while flag == True:
        download_file(location9)
        unzipfile(location9)
        zip_file(location9)
        delete_file(location9)
        flag = False

from __future__ import print_function
import subprocess
import platform
import shutil
from datetime import datetime
import requests
import time as time
import csv
import psutil
import tarfile
import os

global counter

counter = False

with open('document1.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["", "Timestamp", "Server", "Tactic", "Latency", "Cost", "Reliability", ""])

with open('ping.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Server", "Tactic", "PingSuccess", "PingTime"])


def download_file(url, location):
    try:
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
                url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
            flag = 2
        elif (
                url == 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
            flag = 3
        elif (
                url == 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
            flag = 4
        elif (
                url == 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

        if final_time > 120.00:
            final_time = 0

        reliability = 1

        if final_time == 0:
            reliability = 0

        with open('document1.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(["", dateTimeObj, flag, "1", (str)(final_time), psutil.cpu_percent(), reliability, ""])

        counter = False
        return counter


    except Exception:
        counter = True
        # dateTimeObj = datetime.now()
        with open('document1.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(["", dateTimeObj, location, "1", "-1", psutil.cpu_percent(), 0, ""])
        return counter


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
            url == 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (url == 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "2", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def grep_file(url):
    starttime = time.time()
    with open('LibreOffice_6.2.8.2_Linux_x86_deb/readmes/README_en-US', 'r') as f:
        for line in f.readlines():
            if 'Installation' in line:
                print("File grep complete")
    for i in range(1, 100000):
        for j in (1, 100000):
            k = i * j
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
            url == 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (url == 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "3", (str)(final_time), psutil.cpu_percent(), reliability, ""])


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
            url == 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (url == 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "4", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def delete_file(url):
    starttime = time.time()
    os.remove("zip_file.tar.gz")
    os.remove("myzipfile.tar.gz")
    shutil.rmtree('LibreOffice_6.2.8.2_Linux_x86_deb')
    print("Files deleted")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 1
    elif (
            url == 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 2
    elif (
            url == 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 3
    elif (
            url == 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
        flag = 4
    elif (
            url == 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'):
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

    reliability = 1

    with open('document1.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "5", (str)(final_time), psutil.cpu_percent(), reliability, ""])


pointer = True
location1 = 'http://ftp.utexas.edu/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location2 = 'https://mirror.init7.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location3 = 'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location4 = 'https://mirrors.syringanetworks.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location5 = 'http://libreoffice-mirror.rbc.ru/pub/libreoffice/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location6 = 'https://mirror-hk.koddos.net/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location7 = 'http://mirrors.coreix.net/thedocumentfoundation/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'
location8 = 'https://mirror.aarnet.edu.au/pub/tdf/libreoffice/stable/6.2.8/deb/x86/LibreOffice_6.2.8_Linux_x86_deb.tar.gz'

while pointer:

    flag = True
    print("Location 1")

    while flag:

        try:
            r = requests.get(location1)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location1, 1)
                if not counter:
                    unzipfile(location1)
                    grep_file(location1)
                    zip_file(location1)
                    delete_file(location1)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 1, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 1, 1, 0, psutil.cpu_percent(), 0, ""])

        flag = False
        counter = False

    operating_sys = platform.system()
    host = '103.109.101.20'

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False
        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()
        if success == 0:
            print("success")
        else:
            print("fail")

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([6, 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([6, 1, 0, 0])



    flag = True
    print("Location 2")

    while flag:

        try:
            r = requests.get(location2)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location2, 1)
                if not counter:
                    unzipfile(location2)
                    grep_file(location2)
                    zip_file(location2)
                    delete_file(location2)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 2, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 2, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location7'

    host = '85.13.241.50'
    operating_sys = platform.system()

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([7, 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([7, 1, 0, 0])



    print("Location 3")
    flag = True

    while flag:

        try:
            r = requests.get(location3)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location3, 1)
                if not counter:
                    unzipfile(location3)
                    grep_file(location3)
                    zip_file(location3)
                    delete_file(location3)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 3, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 3, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location8'

    host = '202.158.214.106'
    operating_sys = platform.system()

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False
        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()
        if success == 0:
            print("success")
        else:
            print("fail")
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([8, 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([8, 1, 0, 0])



    print("Location 4")
    flag = True

    while flag:

        try:
            r = requests.get(location4)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location4, 1)
                if not counter:
                    unzipfile(location4)
                    grep_file(location4)
                    zip_file(location4)
                    delete_file(location4)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 4, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 4, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location1'

    host = '146.6.15.16'
    operating_sys = platform.system()

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([1, 1, 1, end - start])
    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([1, 1, 0, 0])



    print("Location 5")
    flag = True
    while flag:

        try:
            r = requests.get(location5)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location5, 1)
                if not counter:
                    unzipfile(location5)
                    grep_file(location5)
                    zip_file(location5)
                    delete_file(location5)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 5, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 5, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location2
    host = '109.202.202.202'
    operating_sys = platform.system()

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([2, 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([2, 1, 0, 0])


    print("Location 6")
    flag = True

    while flag:

        try:
            r = requests.get(location6)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location6, 1)
                if not counter:
                    unzipfile(location6)
                    grep_file(location6)
                    zip_file(location6)
                    delete_file(location6)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 6, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 6, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location3
    host = '207.210.46.249'
    operating_sys = platform.system()

    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([3, 1, 1, end - start])
    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([3, 1, 0,0])

    print("Location 7")
    flag = True

    while flag:

        try:
            r = requests.get(location7)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location7, 1)
                if not counter:
                    unzipfile(location7)
                    grep_file(location7)
                    zip_file(location7)
                    delete_file(location7)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 7, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 7, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location4
    operating_sys = platform.system()

    host = '66.232.64.7'
    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([4, 1, 1, end - start])
    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([4, 1, 0,0])



    print("Location 8")
    flag = True
    while flag:

        try:
            r = requests.get(location8)
            print(r.status_code)
            if r.status_code == 200:
                counter = download_file(location8, 1)
                if not counter:
                    unzipfile(location8)
                    grep_file(location8)
                    zip_file(location8)
                    delete_file(location8)

            else:
                dateTimeObj = datetime.now()
                with open('document1.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 8, 1, 0, psutil.cpu_percent(), 0, ""])

        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('document1.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 8, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location5

    host = '80.68.250.218'
    operating_sys = platform.system()


    try:
        ping_command = ['ping', host, '-n', '1'] if operating_sys == 'Windows' else ['ping', host, '-c 1']
        shell_needed = True if operating_sys == 'Windows' else False

        start = time.time()
        ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
        success = ping_output.returncode
        end = time.time()

        if success == 0:
            print("success")
        else:
            print("fail")
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([5, 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([5, 1, 0,0])



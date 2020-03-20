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

location1 = 'https://mirror.init7.net/tdf/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location2 = 'https://mirror.dkm.cz/tdf/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location3 = 'https://libreoffice.mirror.garr.it/mirrors/tdf/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location4 = 'https://tdf.c3sl.ufpr.br/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location5 = 'https://mirror.clarkson.edu/tdf/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location6 = 'http://tdf.mirror.rafal.ca/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location7 = 'https://tdf.mirror.liteserver.nl/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'
location8 = 'https://mirrors.ukfast.co.uk/sites/documentfoundation.org/tdf/libreoffice/src/6.4.2/libreoffice-6.4.2.2.tar.xz'


with open('tva_output.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["", "Timestamp", "Server", "Tactic", "Latency", "Cost", "Reliability", ""])

with open('ping.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Timestamp", "Server", "Tactic", "PingSuccess", "PingTime"])


def download_file(url, location):
    try:
        starttime = time.time()
        results = requests.get(url)
        open('libreoffice-6.4.2.2.tar.xz', 'wb').write(results.content)
        print("File downloaded")
        endtime = time.time()
        final_time = endtime - starttime
        dateTimeObj = datetime.now()

        if (
                url == location1):
            flag = 1
        elif (
                url == location2):
            flag = 2
        elif (url == location3):
            flag = 3
        elif (
                url == location4):
            flag = 4
        elif (url == location5):
            flag = 5
        elif (
                url == location6):
            flag = 6
        elif (
                url == location7):
            flag = 7
        elif (
                url == location8):
            flag = 8


        if final_time > 120.00:
            final_time = 0

        reliability = 1

        if final_time == 0:
            reliability = 0

        with open('tva_output.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(["", dateTimeObj, flag, "1", (str)(final_time), psutil.cpu_percent(), reliability, ""])

        counter = False
        return counter


    except Exception:
        counter = True
        # dateTimeObj = datetime.now()
        with open('tva_output.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow(["", dateTimeObj, location, "1", "-1", psutil.cpu_percent(), 0, ""])
        return counter


def unzipfile(url):
    starttime = time.time()
    # fname = 'libreoffice-6.4.2.2.tar.xz'
    # if fname.endswith("tar.xz"):
    #     tar = tarfile.open(fname, "r:xz")
    #     tar.extractall()
    #     tar.close()
    # elif (fname.endswith("tar")):
    #     tar = tarfile.open(fname, "r:")
    #     tar.extractall()
    #     tar.close()
    with tarfile.open('libreoffice-6.4.2.2.tar.xz') as f:
        f.extractall('.')

    print("File unzipped")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()
    if (
            url == location1):
        flag = 1
    elif (
            url == location2):
        flag = 2
    elif (url == location3):
        flag = 3
    elif (
            url == location4):
        flag = 4
    elif (url == location5):
        flag = 5
    elif (
            url == location6):
        flag = 6
    elif (
            url == location7):
        flag = 7
    elif (
            url == location8):
        flag = 8

    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "2", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def grep_file(url):
    starttime = time.time()
    with open('libreoffice-6.4.2.2/README.md', 'r') as f:
        for line in f.readlines():
            if 'overview' in line:
                print("File grep complete")
    for i in range(1, 100000):
        for j in (1, 100000):
            k = i * j
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == location1):
        flag = 1
    elif (
            url == location2):
        flag = 2
    elif (url == location3):
        flag = 3
    elif (
            url == location4):
        flag = 4
    elif (url == location5):
        flag = 5
    elif (
            url == location6):
        flag = 6
    elif (
            url == location7):
        flag = 7
    elif (
            url == location8):
        flag = 8

    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "3", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def zip_file(url):
    starttime = time.time()
    # tar = tarfile.open("myzipfile.tar.xz", "w:xz")
    # for dirname, subdirs, files in os.walk('libreoffice-6.4.2.2'):
    #     tar.add(dirname)
    #     for filename in files:
    #         tar.add(os.path.join(dirname, filename))
    # tar.close()

    subprocess.call(['tar', '-czf', 'myzipfile.tar.xz', 'libreoffice-6.4.2.2'])

    print("File Zipped")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == location1):
        flag = 1
    elif (
            url == location2):
        flag = 2
    elif (url == location3):
        flag = 3
    elif (
            url == location4):
        flag = 4
    elif (url == location5):
        flag = 5
    elif (
            url == location6):
        flag = 6
    elif (
            url == location7):
        flag = 7
    elif (
            url == location8):
        flag = 8

    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "4", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def delete_file(url):
    starttime = time.time()
    os.remove("libreoffice-6.4.2.2.tar.xz")
    os.remove("myzipfile.tar.xz")
    shutil.rmtree('libreoffice-6.4.2.2')
    print("Files deleted")
    endtime = time.time()
    final_time = endtime - starttime
    dateTimeObj = datetime.now()

    if (
            url == location1):
        flag = 1
    elif (
            url == location2):
        flag = 2
    elif (url == location3):
        flag = 3
    elif (
            url == location4):
        flag = 4
    elif (url == location5):
        flag = 5
    elif (
            url == location6):
        flag = 6
    elif (
            url == location7):
        flag = 7
    elif (
            url == location8):
        flag = 8

    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "5", (str)(final_time), psutil.cpu_percent(), reliability, ""])


pointer = True

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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 1, 0, psutil.cpu_percent(), 0, ""])

        flag = False
        counter = False

    host = 'tdf.mirror.rafal.ca'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 6, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 6, 0, 0])

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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 2, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 2, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location7'

    host = 'tdf.mirror.liteserver.nl'
    operating_sys = platform.system()

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])

        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 7, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 7, 0, 0])



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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 3, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 3, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location8'

    host = 'mirrors.ukfast.co.uk'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 8, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 8, 0, 0])



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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 4, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 4, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = 'location1'

    host = 'mirror.init7.net'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 1, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 1, 0, 0])


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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 5, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 5, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location2
    host = 'mirror.dkm.cz'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 2, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 2, 0, 0])


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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 6, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 6, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location3
    host = 'libreoffice.mirror.garr.it'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 0, 0])

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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 7, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 7, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location4
    operating_sys = platform.system()

    host = 'tdf.c3sl.ufpr.br'
    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 4, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 4, 0, 0])


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
                with open('tva_output.csv', 'a') as fd:
                    writer = csv.writer(fd)
                    writer.writerow(["", dateTimeObj, 8, 0, psutil.cpu_percent(), 0, ""])

        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 8, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False

    # host = location5

    host = 'mirror.clarkson.edu'

    try:

        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host])
        end = time.time()

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 5, 1, end - start])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 5, 0, 0])


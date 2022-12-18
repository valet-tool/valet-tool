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
import re
import os

global counter

counter = False

location1 = 'https://downloads.apache.org/httpd/httpd-2.4.43.tar.gz'
location2 = 'http://mirror.23media.de/apache/httpd/httpd-2.4.43.tar.gz'
location3 = 'http://mirrors.estointernet.in/apache//httpd/httpd-2.4.43.tar.gz'


with open('tva_output.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["", "Timestamp", "Server", "Tactic", "Latency", "Cost", "Reliability", ""])

with open('ping.csv', 'a') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Timestamp", "Server", "Tactic", "PingSuccess", "PingMin", "PingAvg", "PingMax", "Pingstdev"])


def download_file(url, location):
    try:
        starttime = time.time()
        results = requests.get(url)
        open('httpd-2.4.43.tar.gz', 'wb').write(results.content)
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
            writer.writerow(["", dateTimeObj, location, "1", "0", psutil.cpu_percent(), 0, ""])
        return counter

################################


# Get the ping response times
def getPing(host):    
#    print("ping called")
    cmd = "ping -c {} -W {} {}".format(4, 1, host).split(' ') # format(-c = number of times to ping, -W)
#    print(cmd)

#    quit()
    try:
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        total = lines[-2].split(',')[3].split()[1]
        loss = lines[-2].split(',')[2].split()[0]
        timing = lines[-1].split()[3].split('/')
#        print(timing[1])
#        return(timing[1])
#        print(cmd)
#        print(output)
#        quit()
        # min/avg/max/stddev the format of the output
        return(timing)

#        return {
#            'type': 'rtt',
#            'min': timing[0],
#            'avg': timing[1],
#            'max': timing[2],
#            'mdev': timing[3],
#            'total': total,
#            'loss': loss,
#        }
    except Exception as e:
        print(e)
        return None


##############################




def unzipfile(url):
    starttime = time.time()

    with tarfile.open('httpd-2.4.43.tar.gz') as f:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(f, ".")

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


    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "2", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def grep_file(url):
    starttime = time.time()
    with open('httpd-2.4.43/README', 'r') as f:
        for line in f.readlines():
            if 'Export' in line:
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


    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "3", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def zip_file(url):
    starttime = time.time()

    subprocess.call(['tar', '-czf', 'myzipfile.tar.gz', 'httpd-2.4.43'])

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


    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "4", (str)(final_time), psutil.cpu_percent(), reliability, ""])


def delete_file(url):
    starttime = time.time()
    os.remove("httpd-2.4.43.tar.gz")
    os.remove("myzipfile.tar.gz")
    shutil.rmtree('httpd-2.4.43')
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


    reliability = 1

    with open('tva_output.csv', 'a') as fd:
        writer = csv.writer(fd)
        writer.writerow(["", dateTimeObj, flag, "5", (str)(final_time), psutil.cpu_percent(), reliability, ""])


pointer = True

while pointer:

    flag = True
#    print("Location 1")

    while flag:

        try:
            r = requests.get(location1)
#            print(r.status_code)
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
                    writer.writerow(["", dateTimeObj, 1, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 1, 1, 0, psutil.cpu_percent(), 0, ""])

        flag = False
        counter = False

    host = 'estointernet.in'
    print("pinging server 3")
    try:

        # min/avg/max/stddev the format of the output
        pingValue=getPing(host)

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 1,  pingValue[0],  pingValue[1],  pingValue[2],  pingValue[3]])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 0, 0])

    flag = True
    print("Location 2")

    while flag:

        try:
            r = requests.get(location2)
#            print(r.status_code)
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
                    writer.writerow(["", dateTimeObj, 2, 1,  0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 2, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False



    host = 'apache.org'
    print("pinging server 1")
    operating_sys = platform.system()

    try:

        # min/avg/max/stddev the format of the output
        pingValue=getPing(host)

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 1, 1,  pingValue[0],  pingValue[1],  pingValue[2],  pingValue[3]])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 1, 0, 0])

    print("Location 3")
    flag = True

    while flag:

        try:
            r = requests.get(location3)
#            print(r.status_code)
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
                    writer.writerow(["", dateTimeObj, 3, 1, 0, psutil.cpu_percent(), 0, ""])
        except Exception:
            print("Error")
            dateTimeObj = datetime.now()
            with open('tva_output.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow(["", dateTimeObj, 3, 1, 0, psutil.cpu_percent(), 0, ""])
        flag = False
        counter = False


    host = '23media.de'
    print("pinging server 1")

    try:

        # min/avg/max/stddev the format of the output
        pingValue=getPing(host)

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 2, 1,  pingValue[0],  pingValue[1],  pingValue[2],  pingValue[3]])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 2, 0, 0])


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

location1 = 'https://downloads.apache.org/httpd/httpd-2.4.43.tar.gzA'
location2 = 'http://mirror.23media.de/apache/httpd/httpd-2.4.43.tar.gzA'
location3 = 'http://mirrors.estointernet.in/apache//httpd/httpd-2.4.43.tar.gz1'


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


def unzipfile(url):
    starttime = time.time()

    with tarfile.open('httpd-2.4.43.tar.gz') as f:
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
#    print("pinging server 3")
    try:


        ##########################


        # https://stackoverflow.com/questions/48738684/output-only-the-ping-latency-when-using-the-ping-command-in-python

    # b'\r\nPinging estointernet.in [104.24.102.222] with 32 bytes of data:
    #\r\nReply from 104.24.102.222: bytes=32 time=8ms TTL=60\r\n\r\nPing statistics for 104.24.102.222:\r\n    
    #Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),\r\nApproximate round trip times in milli-seconds:\r\n 
    #   Minimum = 8ms, Maximum = 8ms, Average = 8ms\r\n'



        ping = subprocess.Popen(["ping", host, "-n", "1"], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
        output = ping.communicate()


        #output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', host), shell=True)
        #outputStr = str(output)

        pattern = r"Average = (\d+\S+)"
        pingValue = re.findall(pattern, output[0].decode())[0].replace("ms","")
       # ping = "" # not sure if this needed

        print(pingValue)

     #   exit()
     #   print(outputStr)
     #   print("----------------") 
     #   s = 'Denver.dwg Group Layer/Denver.dwg Annotation"'

        # this returns lowest index of first occurence of dwg
        # in this case 7
     #   idx =outputStr.find('Average =')
     #   print(idx)

        # take this index and add 3 for 'dwg'
        # get desired string
      #  subs = outputStr[:idx+15]
      #  print(subs)

#        x = [int(s) for s in re.findall(r'\b\d+\b', outputStr)]
#        pingValue = x[0]
#        print(pingValue)
      #  exit()


        ##########################

        # output = subprocess.check_output("ping -c 1 " + host + " | grep '^rtt'", shell=True)
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', host), shell=True)
        outputStr = str(output)
        x = [int(s) for s in re.findall(r'\b\d+\b', outputStr)]
        pingValue = x[0]
#        print("hereA")
#        print(pingValue)

        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 1,  pingValue/1])

    except Exception as e:
        with open('ping.csv', 'a') as fd:
            writer = csv.writer(fd)
            writer.writerow([datetime.now(), 3, 0, 0])

    flag = True
 

   
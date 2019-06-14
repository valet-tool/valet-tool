import csv
import os
import pathlib
import dateutil.parser
import datetime


TODAY = str(datetime.date.today())

def sort_file():
    py = pathlib.Path().glob("rawfiles/*.csv")
    downstamps_file_name = ''
    output_file_name = ''
    for file in py:
        filename = str(file)
        if filename.find(TODAY) != -1 and filename.find('downstamps') != -1:
            downstamps_file_name = filename
        if filename.find(TODAY) != -1 and filename.find('output') != -1:
            output_file_name = filename
    temp = "sort {}" + downstamps_file_name + '{} {}'+output_file_name+'{} > rawfiles/sorted-'+TODAY+'.csv'
    sort_command = temp.format('"', '"', '"', '"')
    print('Sorting Script')
    if os.system(sort_command):
        print('Sorting was successful')


def merge_files():
    with open('rawfiles/sorted-'+TODAY+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        flag = 0
        counter = 0
        records = []
        totalCurrentForTactic = 0
        totalPowerForTactic = 0
        servernum = -1
        tacticnum = -1
        firstStartedTimestamp = ''
        for row in csv_reader:
            if (row[1] == '1' or row[1] == '2' or row[1] == '3' or row[1] == '4' or row[1] == '5') and flag == 0:
                print('Tactic {} observed for server {}'.format(row[1], row[2]))
                flag = 1
                counter = 1
                tacticnum = int(row[1])
                servernum = int(row[2])
                firstStartedTimestamp = dateutil.parser.parse(row[0])

            elif row[1] == '0' and flag == 1:
                print('Tactic 0 observed')
                flag = 0
                averagePowerConsumed = totalPowerForTactic / counter
                endedTimestamp = dateutil.parser.parse(row[0])
                latency = str(endedTimestamp - firstStartedTimestamp)
                record = [averagePowerConsumed, str(firstStartedTimestamp), latency, servernum, tacticnum]
                records.append(record)
                totalPowerForTactic = 0
                totalCurrentForTactic = 0
                counter = 0
            elif flag == 1:
                # Total Current in mA for specific tactic
                totalCurrentForTactic += float(row[1])
                # Total power in mW for specific tactic
                totalPowerForTactic += float(row[2])
                # Increment counter
                counter += 1
    print('Done...')


if __name__ == '__main__':
    sort_file()
    merge_files()

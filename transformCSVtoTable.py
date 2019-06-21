import csv
import dateutil.parser
import datetime
import pandas

TODAY = str(datetime.date.today())
def calculate_final_data(timegroups):
    time_records_list = []
    totalPowerForTactic = 0
    with open('rawfiles/output-' + TODAY + '.csv') as time_file:
        time_reader = list(csv.reader(time_file, delimiter=','))
        for timegroup in timegroups:
            startedTimestamp = dateutil.parser.parse(timegroup[0])
            endedTimestamp = dateutil.parser.parse(timegroup[1])
            if endedTimestamp <= startedTimestamp:
                continue
            for time_row in time_reader:
                if startedTimestamp <= dateutil.parser.parse(time_row[0]) <= endedTimestamp:
                    totalPowerForTactic += float(time_row[2])
            latency_in_mins = endedTimestamp - startedTimestamp
            latency = str(latency_in_mins.total_seconds())
            servernum = timegroup[2]
            tacticnum = timegroup[3]
            record = [totalPowerForTactic, str(startedTimestamp), latency, servernum, tacticnum]
            time_records_list.append(record)
            totalPowerForTactic = 0

    return time_records_list
def create_time_groups():
    with open('rawfiles/downstamps-'+TODAY+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        records = []
        servernum = -1
        tacticnum = -1
        firstStartedTimestamp = ''
        try:
            for row in csv_reader:
                try:
                    if row[1] == '1' or row[1] == '2' or row[1] == '3' or row[1] == '4' or row[1] == '5':
                        print('Tactic {} observed for server {}'.format(row[1], row[2]))
                        tacticnum = int(row[1])
                        servernum = int(row[2])
                        firstStartedTimestamp = dateutil.parser.parse(row[0])

                    elif row[1] == '0':
                        print('Tactic 0 observed')
                        endedTimestamp = dateutil.parser.parse(row[0])
                        record = [str(firstStartedTimestamp), str(endedTimestamp), servernum, tacticnum]
                        records.append(record)

                except IndexError:
                    continue
                except ValueError:
                    continue
        except UnicodeDecodeError:
            print('Unicode Error')
    return records

if __name__ == '__main__':
    timegroups = create_time_groups()
    records = calculate_final_data(timegroups)
    pd = pandas.DataFrame(records)
    pd.columns = ['totalPowerConsumed', 'firstStartedTimestamp', 'latency', 'serverNumber', 'tacticNumber']
    today = str(datetime.date.today())
    pd.to_csv('rawfiles/results-' + today + '.csv')
    print('Done...')
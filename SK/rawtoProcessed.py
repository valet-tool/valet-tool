import pandas as pd

#Converting each of the two files into dataframes

df1 = pd.read_csv('rawfiles/downstamps-2019-06-24.csv')
df1.columns = ['DateTime', 'Tactic', 'Server']
df1.to_csv('SK/downstampswithcolumns/downstamps-2019-06-24_with_col.csv', index=False)

df2 = pd.read_csv('rawfiles/output-2019-06-24.csv', header=0,encoding = 'unicode_escape')
df2.columns = ['DateTime', 'Cost1', 'Cost2']
df2.to_csv('SK/outputwithcolumns/output-2019-06-24_with_col.csv', index=False)

#Merging the two files on Timestamp

mergedfile = pd.merge(df1, df2, how='left', on='DateTime')

mergedfile.to_csv('SK/2019-06-24_with_col.csv', index=False)


#Removing a errorneous entry

mergedfile.loc[mergedfile['DateTime'] == '2019-0', 'DateTime'] = '2019-06-24T00:03:28.000Z'

mergedfile['date'] = mergedfile['DateTime'].dt.date
mergedfile['time'] = mergedfile['DateTime'].dt.time

# if tstamp1 > tstamp2:
#     td = tstamp1 - tstamp2
# else:
#     td = tstamp2 - tstamp1
# td_mins = int(round(td.total_seconds() / 60))

# for mergedfile['DateTime'] in mergedfile:
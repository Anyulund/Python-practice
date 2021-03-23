#Given a log file with rows featuring a date, a number, and then a string of names,
#parse the log file and retur the count of unique names aggregated by month
import pandas as pd

A = [['27/08/2020',6,'billie joe armstrong'],['22/10/2020',9,'robert plant']]

df = pd.DataFrame(A, columns =['Date','Number','Name'])

m1 = df['Date'].str.split('/', n=1, expand =True)
df['Month'] = m1[1]

result = df.groupby('Month')['Name'].nunique()
#print(result)

#Given a list of timestamps in sequential order, return a list of lists grouped by weekly aggregation

ts = ['2019-01-01','2019-01-02','2019-01-08', '2019-02-01','2019-02-05']

df1 = pd.DataFrame(ts, columns = ['Date'])
df1['Date']= pd.to_datetime(df1['Date'])
df1['Week']=df1['Date'].dt.week
result2 = df1.groupby('Week')['Date'].apply(list)

print(df1)
print(result2)
#print(df['Week'])

#df = pd.DataFrame[‘Date’].dt.week.sort_values(by_Date)
#Sorted_ts = df.groupby(‘Week’)

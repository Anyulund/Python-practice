
import pandas as pd
import re
'''
iris = pd.read_csv('iris.csv')
print(iris.head())

#print(iris.describe())

#print(iris.shape[1])

#print(iris.shape)

extract = iris.iloc[3,1]
#print(extract)

values = iris['Species'].unique()
#print(values)

filtered = iris.loc[iris['Species'] == 'virginica']
#print(filtered)

#print(iris.columns)

#print(iris.iloc[0:3,:])

sum_length = iris.groupby('Species')['Petal.Length','Petal.Width'].sum()
#print(sum_length)

freq = iris['Species'].value_counts(ascending = True)
print(freq)

freq_unique = iris['Species'].nunique()
print(freq_unique)

filtered_vir = iris.loc[iris['Species'] == 'virginica']
filtered_ver = iris.loc[iris['Species'] == 'versicolor']
filtered_set = iris.loc[iris['Species'] == 'setosa']

banana = pd.concat([filtered_ver,filtered_set,filtered_vir], axis = 0)
print(banana)

print(banana.shape)

print(banana.head())

banana.reset_index(inplace = True, drop = True)

print(banana)

freq_nunique = iris['Species'].unique()
print(freq_nunique)

iris['Species']= iris['Species'].str.replace('v','V')
print(iris['Species'].unique())


sentence1 = "Hi my name is Mansi....I am an MSIS grad student."

#sentence2 = sentence1.replace('....',' ')
#sentence3 = sentence2.replace('.', ' ')

for p in "?,:;'.":
	sentence1 = sentence1.replace(p,'')

print(sentence1)

words = sentence1.split(' ')

print(words)

result = round(sum(len(word) for word in words)/len(words),2)

print(result)


A = [[27/08/2020,6,’billie joe armstrong’],[22/10/2020,9,’robert plant’]]

df = pd.dataframe[‘Date’, ‘Number’, ‘Name']
df[‘Month’] = df.[‘Date’].dt.month
df.groupby('Name').agg('Month')

# write regular expression to match legal email address


import re

text = '123 anyulund@gmail.com 123'
text2 = 'banana 168.212.226.204 cat'
pattern = re.compile(r'[\d]+\.[\d]+\.[\d]+\.[\d]+')

matches = pattern.finditer(text2)
for mat in matches:
    print(mat.span(0))
    print(mat.group(0))
    print(text2[mat.span(0)[0]:mat.span(0)[1]])

'''
#Given a list of timestamps in sequential order, return a list of lists grouped by weekly aggregation

ts = ['2019-01-01','2019-01-02','2019-01-08','2019-02-01','2019-02-05']

df = pd.Series(ts).dt.week.sort_values(by_Date)
print(df)

#Sorted_ts = df.groupby(‘Week’)

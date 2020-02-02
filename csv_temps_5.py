import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file1=open("sitka_weather_2018_simple.csv","r")
csv_file1=csv.reader(open_file1,delimiter=",")
header_row1=next(csv_file1)

open_file2=open("death_valley_2018_simple.csv","r")
csv_file2=csv.reader(open_file2,delimiter=",")
header_row2=next(csv_file2)

highs1=[]
lows1=[]
dates1=[]
highs2=[]
lows2=[]
dates2=[]

for index,column_header in enumerate (header_row1):
    #print(index,column_header)
    if column_header=='TMIN':
        min_index1=index
    elif column_header=='TMAX':
        max_index1=index
    elif column_header=='DATE':
        date_index1=index
    elif column_header=='NAME':
        name_index1=index

for row in csv_file1:
    title1=row[name_index1]
    try:
        high=int(row[max_index1])
        low=int(row[min_index1])
        current_date=datetime.strptime(row[date_index1],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(current_date)

for index,column_header in enumerate (header_row2):
    #print(index,column_header)
    if column_header=='TMIN':
        min_index2=index
    elif column_header=='TMAX':
        max_index2=index
    elif column_header=='DATE':
        date_index2=index
    elif column_header=='NAME':
        name_index2=index

for row in csv_file2:
    title2=row[name_index2]
    try:
        high=int(row[max_index2])
        low=int(row[min_index2])
        current_date=datetime.strptime(row[date_index2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)

fig,(ax1,ax2)=plt.subplots(2,sharex=True)
fig.suptitle('Temperature comparison between '+title1+' and '+title2, fontsize=12)
ax1.plot(dates1,highs1,'tab:red',alpha=1)
ax1.plot(dates1,lows1,'tab:blue',alpha=1)
ax1.fill_between(dates1,highs1,lows1,facecolor='blue',alpha=0.1)
ax1.set_title(title1, fontsize=12)

ax2.plot(dates2,highs2,'tab:red',alpha=1)
ax2.plot(dates2,lows2,'tab:blue',alpha=1)
ax2.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)
ax2.set_title(title2, fontsize=12)

fig.autofmt_xdate()
plt.show()
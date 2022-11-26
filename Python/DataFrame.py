import numpy as np
import pandas as pd
import datetime

#Create a 3 by 3 array and call it a. 
#Use random numbers to fill the contents.
a = np.random.randint(1,100, size=(3,3))
print(a)

#Convert a to a pandas data frame called a1.
#Label the columns of a1 as CO1, CO2, CO3
#rows as RO1, RO2, RO3.
a1 = pd.DataFrame(a, columns = ['CO1','CO2','CO3'], index= ['RO1','RO2','RO3'])
print(a1)

#todays date
date_time = datetime.datetime.now()
today = [date_time, date_time, date_time]
print(today)

#Add today's date as column into a1 
#call this column as t_day.
a1.insert(3,"t_day",today,True)
print(a1)

#From t_day extract 
#year, the month, the week, the day, the weekday, hour and minute
#put each into a column.
date = datetime.datetime.strptime(date_time, "%y %b %U %d %a %H:%M")
print(date)

#Convert date into array 
li = list(date.split(" "))
print(li)

#Add colums to DataFrame
a1 = a1.assign()
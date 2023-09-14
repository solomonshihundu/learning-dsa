import pandas
 
file = pandas.read_csv("D:\Work\CSV Files\Wycliffe\scoring_data.csv")
for col in file.columns:
    print(col)
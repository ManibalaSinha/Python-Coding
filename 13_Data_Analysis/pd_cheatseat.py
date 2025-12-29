import pandas as pd
df = pd.read_csv("data.csv") #loads csv file into Dataframe(table(row+cloumn)
df.head() #shows 1st 5 rows
df.info() #shows columns names, data types
df["col"] #return series(1 column)
df[["a","b"]] #return Dataframe
df[df["age"]>30] #filter rows
df.groupby("deparment")["salary"].mean()# group rows by department, select salary, calculate mean salary per department
df.groupby("type")["amount"].sum()#
df.fillna(0) #handle missing values, replaces NaN with 0
df.dropna() #drop missing rows, remove rows with NaN
#CSv,find average salary per department where age >30
df[df["age"]>30].groupby("dept")["salary"].mean()
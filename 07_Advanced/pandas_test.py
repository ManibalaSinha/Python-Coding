import pandas as pd
df = pd.DataFrame({
    "dept": ["IT", "HR", "IT"],
    "salary": [100, 200, 150]
})
print(df)
c=df.groupby("dept")["salary"].sum()
print(c)
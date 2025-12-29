import pandas as pd
df = pd.read_csv("data.csv")
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['prev'] = df.groupby('customer_id')['purchase_date'].shift(1)
df['gap'] = (df['purchase_date']-df['prev']).dt.days
result = df.groupby('customer_id')['gap'].mean().dropna()
print(result)
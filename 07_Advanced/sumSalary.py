import pandas as pd
df = pd.DataFrame({"dept":["IT","HR","IT"],"salary":[100,200,150]})
# Print sum of salaries by dept
salary_sum = df.groupby("dept")[("salary")].sum()
print(salary_sum)
import pandas as pd

df = pd.DataFrame({
    "dept": ["IT", "HR", "IT", "HR", "IT", "Finance"]
})

# Count rows per department
count_per_dept = df.groupby("dept").size()

print(count_per_dept)
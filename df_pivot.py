import pandas as pd

data = {
    'ID' : [101,102,103,104],
    'Name': ['Anubhav','Barnali', 'Charchit','Debo'],
    'Subject': ['Math', 'Science', 'Math', 'Science'],
    'Marks': [80, 75, 90, 85]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

pivot_df = df.pivot(index='Name', columns='Subject', values='Marks')

print("\nDataFrame after Pivot operation:")
print(pivot_df)

pivot_df = pivot_df.reset_index()

print("\nDataFrame after resetting index:")
print(pivot_df)
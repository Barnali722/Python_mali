import pandas as pd

data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
}

df = pd.DataFrame(data, index=['X', 'Y', 'Z'])

print(df)

new_row_index = ['X', 'Y', 'Z', 'W']
df = df.reindex(new_row_index, fill_value=100)

print("\nAfter reindexing rows:")
print(df)

new_column_index = ['A', 'B', 'C', 'D']
df = df.reindex(columns=new_column_index, fill_value=25)

print("\nAfter reindexing columns:")
print(df)

data_II = {"Name" : ["A","B","C","D","E","F","G","H"],
    "Age" : [25,44,32,34,35,19,20,22],
    "Dept" : ["IT","IT","MRKT","SALES","MRKT","SALES","IT","MRKT"],
    "Contact" : [124112,524647,1323424,33464575,464374577,32124124,5454643,3235423],
    "DOB" : ["2006/07/07","2009/08/08","2014/10/14","2021/06/22","2042/12/31","2024/04/30","2045/01/12","2006/13/23"]}

print("\nOriginal Dataset : ")
df_II = pd.DataFrame(data_II, index =[1,2,3,4,5,6,7,8])
print(df_II)

new_row = [1,2,3,4,5,6,7,8,9]
df_II = df_II.reindex(new_row, fill_value = "25")
print("\nReindexed Dataset : ")
print(df_II)

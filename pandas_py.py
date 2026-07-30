import pandas as pd
data = {"Name" : ["A","B","C","D","E","F","G","H"],
    "Age" : [25,44,32,34,35,19,20,22],
    "Dept" : ["IT","IT","MRKT","SALES","MRKT","SALES","IT","MRKT"],
    "Contact" : [124112,524647,1323424,33464575,464374577,32124124,5454643,3235423],
    "DOB" : ["2006/07/07","2009/08/08","2014/10/14","2021/06/22","2042/12/31","2024/04/30","2045/01/12","2012/09/08"]}
df = pd.DataFrame(data)
print(df)
print(df.head(3))
print(df.tail(3))
print('----Info------')
print(df.info())
df.dropna(inplace = True)
print(df)
df['DOB'] = pd.to_datetime(df['DOB'],format = 'mixed')
print(df)
print(df.info())
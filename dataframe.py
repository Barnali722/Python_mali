import pandas as pd
import numpy as np
data = {"Name" : ["A","B","C","D","E","F","G","H"],
    "Age" : [25,44,32,34,35,19,20,22],
    "Dept" : ["IT","IT","MRKT","SALES","MRKT","SALES","IT","MRKT"],
    "Contact" : [124112,524647,1323424,33464575,464374577,32124124,5454643,3235423],
    "DOB" : ["2006/07/07","2009/08/08","2014/10/14","2021/06/22","2042/12/31","2024/04/30","2045/01/12",np.nan]}
df = pd.DataFrame(data, index=[1,2,3,4,5,6,7,8])
#df = pd.DataFrame(data)
print(df)
df.fillna({"DOB" : "2045/02/12"})
print(df)
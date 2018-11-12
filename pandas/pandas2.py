import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('XLyS'))

print(df)
print(df.loc[dates[1],'S'])
df2 = pd.DataFrame({'index' : 1.,
                   'time' : pd.Timestamp('20130102'),
                   'x' : pd.Series(1,index=list(range(4)),dtype='float32'),
                   'y' : np.array([3] * 4,dtype='int32'),
                   'feature1' : pd.Categorical(["test1","train2","test3","train4"]),
                     'feature2' : 'foo' })
print(df2)
print(df2['time'])
print(df2.tail(3))
print(df2[df2['feature1'].isin(['test'])])

print(df2.iat[3,4])
list= [1,2,3,4,'test']
numpy_array = np.array(list)
print(numpy_array)
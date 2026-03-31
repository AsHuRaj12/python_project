import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('UberDataset.csv',lineterminator='\n')

df.head()

df.info()

df.describe()

df.isnull().sum()

df.columns

from datetime import datetime
df['START_DATE'] = pd.to_datetime(df['START_DATE'],errors='coerce')
print(df['START_DATE'].dtypes)


from datetime import datetime
df['END_DATE'] = pd.to_datetime(df['END_DATE'],errors='coerce')
print(df['END_DATE'].dtypes)

df.head()


from datetime import datetime
df['DATE'] = pd.DatetimeIndex(df['START_DATE']).date


df.head()

df['TIME'] = pd.DatetimeIndex(df['START_DATE']).hour


df.head()


df['DAY-NIGHT'] = pd.cut(x=df['TIME'],bins=[0,10,15,19,24],labels=['morning','afternoon','evening','night'])

df.head()

#DATA VISUALISATION

plt.figure(figsize=(20,5))


plt.subplot(1,2,1)
sns.countplot(df['CATEGORY'])

plt.subplot(1,2,2)
plt.countplot(df['PURPOSE'])


sns.countplot(df['DAY-NIGHT'])


df['MONTHS'] = pd.DatetimeIndex(df['START_DATE']).month
months_label = {1.0:'jan',2.0:'feb',3.0:'mar',4.0:'apr',5.0:'may',6.0:'jun',7.0:'jul',8.0:'aug',9.0:'sep',10.0:'oct',11.0:'nov',12.0:'dec'}
df['MONTHS'] = df.MONTHS.map(months_label)
mon = df.MONTHS.value_counts(sort=False)

df.head()
df.head()

df


df =pd.DataFrame({
    'MONTHS':mon.values,
    'VALUE COUNT':df.groupby('MONTHS',sort=False)['MILES'].max()
})
p = sns.lineplot(data=df)
p.set(xlabel='MONTHS',ylabel='VALUE COUNT')


df['DAY'] = df.START_DATE.dt.weekday
day_label = {0:'mon',1:'tues',2:'wed',3:'thurs',4:'fri',5:'sat',6:'sun'}
df['DAY'] = df['DAY'].map(day_label)

df.columns

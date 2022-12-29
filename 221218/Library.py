import datetime

today = datetime.date.today()
print(datetime.date.today())
print(datetime.datetime.now())
print(today.day)

yesterday = today - datetime.timedelta(days=1)
print(yesterday)

print(today.strftime('%Y年%m月%d日'))

import pandas as pd

df = pd.DataFrame([
            [1,2,3,4,5,6],
            [4,5,6,7,8,9],
            [7,8,9,10,11,12]
            ])
print(df)

print(df.iloc[1:, :3])
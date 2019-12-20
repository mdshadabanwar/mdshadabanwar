# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

eStud = pd.read_csv(r'C:\Users\shadab\OneDrive - Hewlett Packard Enterprise\Project\Python-Training\HPEB01-master\Classwork\day04\students.csv')
df=pd.DataFrame(eStud)

df['avg'] = (df['phy']+df['chem']+df['math']+df['bio'])/4
df['rank']=df['avg'].rank(ascending=False)
df.sort_values(('rank'), inplace=True)
print(df)

df.to_excel(r'C:\Users\shadab\OneDrive - Hewlett Packard Enterprise\Project\Python-Training\HPEB01-master\Classwork\day04\Excel_Sample.xlsx',sheet_name='Sheet1')

print (df)
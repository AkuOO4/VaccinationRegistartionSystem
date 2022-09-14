from typing import Final
import pandas as pd
from datetime import date, timedelta
import random

column_name=['ID','Name','Age','Gender','Comorbidity','Appointment_date']

# Indian-Male-Names.csv and Indian-Female-Names.csv contains raw csv of Indian names.

male_names = pd.read_csv('Indian-Male-Names.csv')
# male_names contains data available in Indian-Male-Names.csv which contain only unprocessed male names.

female_names = pd.read_csv('Indian-Female-Names.csv')
# female_names contains data available in Indian-Female-Names.csv which contain only unprocessed female names.

male_namelist = []
female_namelist = []


for names in female_names['name']:
# processing on names acailable in data.
    first_name = str(names).strip().split(' ')[0]
    male_namelist.append(first_name)

for names in male_names['name']:
# processing on names acailable in data.

    first_name = str(names).strip().split(' ')[0]
    female_namelist.append(first_name)

processed_male_namelist = []
processed_female_namelist = []

s = 'abcdefghijklmnopqrstuvwxyz'

for i in female_namelist:
# processing on names acailable in namelist which contains all male and female names .

    i = i.split('@')[0]

    i = i.split('.')[-1]

    i = i.split('-')[-1]

    i = i.strip('`').strip()

    if len(i) > 2:

        for j in i:

            if j in s:
                processed_female_namelist.append(i)



for i in male_namelist:
# processing on names acailable in namelist which contains all male and female names .

    i = i.split('@')[0]

    i = i.split('.')[-1]

    i = i.split('-')[-1]

    i = i.strip('`').strip()

    if len(i) > 2:

        for j in i:

            if j in s:
                processed_male_namelist.append(i)

Final_Data={'ID':[],'Name':[],'Age':[],'Gender':[],'Comorbidity':[],'Appointment_Date':[]}

start=date.today()-timedelta(days=20)

for i in range (500):
    if i//2==0:
        Final_Data['Age'].append(i+1)
        Final_Data['Name'].append(male_namelist[i])
        Final_Data['Gender'].append('M')

    else:
        Final_Data['Age'].append(i+1)
        Final_Data['Name'].append(female_namelist[i])
        Final_Data['Gender'].append('F')

    if i//50==0:
        Final_Data['Comorbidity'].append(True)
    else:
        Final_Data['Comorbidity'].append(False)

    rand_date=start+timedelta(days=random.randrange(30))
    Final_Data['Appointment_Date'].append(rand_date)

    

    

df=pd.DataFrame(Final_Data)
df.to_csv('Data.csv')
# for i in range (5):
#     print(male_names.name[i])

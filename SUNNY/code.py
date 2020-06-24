# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,np.asarray(new_record)))
age=census[:,0]
max_age=age.max(axis=0)
min_age=age.min(axis=0)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age,min_age,'%.2f'%age_mean,'%.2f'%age_std,)
race_0=np.arange(0,census[0].size)
race_1=np.arange(0,8)
race_2=np.arange(0,8)
race_3=np.arange(0,8)
race_4=np.arange(0,8)
for i in range(0,len(census)):
    if census[i][2]==0:
        race_0=np.concatenate((race_0,census[i]))
    elif census[i][2]==1:
        race_1=np.concatenate((race_1,census[i]))
    elif census[i][2]==2:
        race_2=np.concatenate((race_2,census[i]))
    elif census[i][2]==3:
        race_3=np.concatenate((race_3,census[i]))
    elif census[i][2]==4:
        race_4=np.concatenate((race_4,census[i]))
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
l=[len_0,len_1,len_2,len_3,len_4]
miniority_race=l.index(min(l))
print(miniority_race)
val=list(census[:,0])

senior_citizens=np.asarray([list(census[i]) for i in range(0,len(val)) if val[i]>60])

#print(senior_citizens)
p=list(senior_citizens[:,6])
working_hours_sum=sum(p)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print('%.2f'%avg_working_hours)


num=list(census[:,1])
high=np.asarray([list(census[i]) for i in range(0,len(num)) if num[i]>10])
low=np.asarray([list(census[i]) for i in range(0,len(num)) if num[i]<=10])

avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print('%.2f'%avg_pay_high)
print('%.2f'%avg_pay_low)




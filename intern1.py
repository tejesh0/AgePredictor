# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 22:48:35 2014

@author: supertramp
"""

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


path1 = "/home/supertramp/Desktop/100&life_180_data.csv"

mydf =  pd.read_csv(path1)
#xercise = sns.load_dataset(path1)

mydf['Cigarettes'] = mydf['Cigarettes'].str.replace(' ', '')
mydf['Cigarettes'] = mydf['Cigarettes'].str.replace('1-5','1-5Cigarettes/day')
mydf['Cigarettes'] = mydf['Cigarettes'].str.replace('1-5Cigarettes/dayCigarettes/day','1-5Cigarettes/day')
mydf['Cigarettes'] = mydf['Cigarettes'].str.replace('1-5Cigarettes/daycigarettesperday','1-5Cigarettes/day')
mydf['Cigarettes'] = mydf['Cigarettes'].str.replace('No','Never')
mydf['Cigarettes'] = mydf['Cigarettes'].str.replace('Neverne','Never')

mydf['Eating Out'] = mydf['Eating Out'].str.replace(' ','')
mydf['Eating Out'] = mydf['Eating Out'].str.replace('Atweekends','Attheweekends')

mydf['Alcohol'] = mydf['Alcohol'].str.replace(' ','')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('Never','Iamatee-totaler')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('No','Iamatee-totaler')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('Weekend','Icatchupfriendsintheweekendsforadrink')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('icatchupwithfriendsintheweekendforadrink','Icatchupfriendsintheweekendsforadrink')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('Icatchupfriendsinweekendsforadrink','Icatchupfriendsintheweekendsforadrink')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('Occasionally','OccasionallywhenIgoforparties')
mydf['Alcohol'] = mydf['Alcohol'].str.replace('OccasionallywhenIgoforpartieswhenIgoforparties','OccasionallywhenIgoforparties')

mydf['Meal Timings'] = mydf['Meal Timings'].str.replace(' ','')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Havemealsatregularandfixedtimings','Ifollowfixedandregulartimingsallthetime')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Havemealsatregularandfixedtimes','Ifollowfixedandregulartimingsallthetime')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('HavethemwhenIfindtime','Idonotsparetimeformeals;grabthemasandwhenpossible')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Ifollowfixedregulartimingsallthetime','Idonotsparetimeformeals;grabthemasandwhenpossible')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Idonotsparetimeformeals,grabthemasandwhenpossible','Idonotsparetimeformeals;grabthemasandwhenpossible')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Noregularroutinewhiletravelling','IdonotfollowtheroutinetimingswhenIamtravelling')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Followfixedtimingsduringworkweek','Ifollowfixedtimingsduringtheworkweek')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Ifollowfixedtimingsduringaworkweek','Ifollowfixedtimingsduringtheworkweek')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('Ifollowfixedtimingseveryday','Ifollowfixedandregulartimingsallthetime')
mydf['Meal Timings'] = mydf['Meal Timings'].str.replace('idonotfollowwentra','IdonotfollowtheroutinetimingswhenIamtravelling')

mydf['Exercise'] = mydf['Exercise'].str.replace(' ','')
mydf['Exercise'] = mydf['Exercise'].str.replace('3-4timesaweek','Iplaywithfamilyandfriendsonlyduringtheweekend')
mydf['Exercise'] = mydf['Exercise'].str.replace('Everyday','Myroutinedaystartswithexercisesandyoga')
mydf['Exercise'] = mydf['Exercise'].str.replace('Ispend2hoursinexcersiseeveryday','Myroutinedaystartswithexercisesandyoga')
mydf['Exercise'] = mydf['Exercise'].str.replace('Myroutinedaystartswithanexcercise','Myroutinedaystartswithexercisesandyoga')
mydf['Exercise'] = mydf['Exercise'].str.replace('Myroutinedaystartswithexerciseandyoga','Myroutinedaystartswithexercisesandyoga')
mydf['Exercise'] = mydf['Exercise'].str.replace('DailyWalking-50mins','Myroutinedaystartswithexercisesandyoga')
mydf['Exercise'] = mydf['Exercise'].str.replace('Routinewalking','Myroutinedaystartswithexercisesandyoga')

mydf['Exercise'] = mydf['Exercise'].str.replace('Onlyonweekends','Iplaywithfamilyandfriendsonlyduringtheweekend')
mydf['Exercise'] = mydf['Exercise'].str.replace('Iplaywithmyfamilyandfriendsduringtheweekend','Iplaywithfamilyandfriendsonlyduringtheweekend')
mydf['Exercise'] = mydf['Exercise'].str.replace('Onceortwiceaweek','Iplaywithfamilyandfriendsonlyduringtheweekend')

mydf['Exercise'] = mydf['Exercise'].str.replace('Ispend2hoursatthegym/playtennis,shuttleIplaywithfamilyandfriendsonlyduringtheweekend','Ispend2hoursatthegym/playtennis,shuttle3-4time...')
mydf['Exercise'] = mydf['Exercise'].str.replace('Ispend2hoursatthegym/playtennis;shuttleIplaywithfamilyandfriendsonlyduringtheweekend','Ispend2hoursatthegym/playtennis,shuttle3-4time...')
mydf['Exercise'] = mydf['Exercise'].str.replace('Ispend2hoursatthegym/playtennis/shuttleIplaywithfamilyandfriendsonlyduringtheweekend','Ispend2hoursatthegym/playtennis,shuttle3-4time...')

mydf['Exercise'] = mydf['Exercise'].str.replace('Ispendmostoftimeatworkandspendaquiteweekend','Ispendmostoftimeatworkandspendaquietweekend')
mydf['Exercise'] = mydf['Exercise'].str.replace('NophysicalActivity','Ispendmostoftimeatworkandspendaquietweekend')
mydf['Exercise'] = mydf['Exercise'].str.replace('Notapplicable','Ispendmostoftimeatworkandspendaquietweekend')



mydf['bmi'] = mydf['BMI'].map(lambda x : 40  if x>=30 else 37 if x>=21 and x<=30 else 31 if x>20 and x<21 else 24 if x<=20 else 15)




numcigar = {"Never":0 ,"1-5Cigarettes/day" :2.0,"10-20Cigarettes/day":3.0}

num_eat = {"Eatonlyhomemadefood" :0.0 ,"Attheweekends" :0.0 ,"onceinaweek":0.0,"3-4daysaweek":0.5 ,"Occasionallyduringparties" :0.0,"Occasionallyduringparty":0.0,"Everyday":1.0}

num_alco = {"Iamatee-totaler":0,"OccasionallywhenIgoforparties":0.0,"Icatchupfriendsintheweekendsforadrink":-0.05,"Ispendmyeveningsatthesocialclubsandhaveadrink":-0.15}

num_meal = {"Ifollowfixedandregulartimingsallthetime":0,"Ifollowfixedtimingsduringtheworkweek":-0,"IdonotfollowtheroutinetimingswhenIamtravelling":0.5,"Idonotsparetimeformeals;grabthemasandwhenpossible":1}

num_exer = {"Myroutinedaystartswithexercisesandyoga":-3,"Ispend2hoursatthegym/playtennis,shuttle3-4time...":-3,"Ispendmostoftimeatworkandspendaquietweekend":0,"Iplaywithfamilyandfriendsonlyduringtheweekend":0}

mydf['EatNum'] = mydf['Eating Out'].replace(num_eat).astype(float)

mydf['CigarNum'] = mydf['Cigarettes'].replace(numcigar).astype(float)

mydf['Age'][mydf.BMI.map(lambda x: x>=10 and x<=18)]

mydf['AlcoNum'] = mydf['Alcohol'].replace(num_alco).astype(float)

mydf['MealNum'] = mydf['Meal Timings'].replace(num_meal).astype(float)

mydf['ExerNum'] = mydf['Exercise'].replace(num_exer).astype(float)

print 'cdd'
print mydf[mydf.Age.map(lambda x :  x>55)]

new_data = mydf.drop(['Eating Out', 'Meal Timings','Exercise','Alcohol','Cigarettes','BMI'], axis=1)



new_data['Score'] = new_data.sum(axis=01) -new_data['Age'] -new_data['No']





final_data = mydf.drop(['EatNum','CigarNum','AlcoNum','MealNum','ExerNum','bmi'],axis=1) 
final_data['Predicted Age'] = new_data['Score']


N = len(new_data['Age'])

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(ind, new_data['Score'], width, color='r')
#rects1 = ax.bar(int+width,new_data.accurate,width,color='y')

rects1 = ax.bar(ind+width,new_data.Age, width, color='y')
ax.set_ylabel('Age')
ax.set_title('Ages comparision')
ax.set_xticks(ind+width)
ax.set_xticklabels(new_data['No']  )

ax.legend( (rects1[0], rects2[0]), ('CHRONOLOGICAL AGE', 'BIOLOGICAL AGE') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()

final_data.to_csv('/home/supertramp/Desktop/alldata22.csv')

print 'Done'
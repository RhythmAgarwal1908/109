import plotly.figure_factory as ff 
import csv
import pandas as pd
import random
import statistics
df = pd.read_csv("data.csv")
#fig = ff.create_distplot([df['Height(Inches)'].tolist()],["Height"],show_hist=False)
#fig.show()
#count=[]
dice_result=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    #count.append(i)

mean = sum(dice_result)/len(dice_result)
std = statistics.stdev(dice_result)
print("Mean-",mean)
print("Deviation-",std)
median=statistics.median(dice_result)
print("Median-",median)
mode= statistics.mode(dice_result)
print("Mode-",mode)
print(sum(dice_result))
fig = ff.create_distplot([dice_result],["Result"])
fig.show()
std_1_start,std_1_end=mean-std,mean+std
std_2_start,std_2_end=mean-(2*std),mean+(2*std)
std_3_start,std_3_end=mean-(3*std),mean+(3*std)
std_deviation_1=[i for i in dice_result if i > std_1_start and i<std_1_end]
std_deviation_2=[i for i in dice_result if i > std_2_start and i<std_2_end]
std_deviation_3=[i for i in dice_result if i > std_3_start and i<std_3_end]
print(len(std_deviation_1)*100/len(dice_result))
print(len(std_deviation_2)*100/len(dice_result))
print(len(std_deviation_3)*100/len(dice_result))
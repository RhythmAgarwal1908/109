import csv
import pandas as pd
import statistics
pf= pd.read_csv('data.csv')
h_list=pf["Height(Inches)"].to_list()
w_list=pf["Weight(Pounds)"].to_list()
h_mean=statistics.mean(h_list)
w_mean=statistics.mean(w_list)
h_median= statistics.median(h_list)
w_median=statistics.median(w_list)
h_mode = statistics.mode(h_list)
w_mode = statistics.mode(w_list)
print("Mean , Median , Mode Of Height is {},{} and {} respectively".format(h_mean,h_median,h_mode))
print("Mean , Median , Mode Of Weight is {},{} and {} respectively".format(w_mean,w_median,w_mode))
h_std=statistics.stdev(h_list)
w_std=statistics.stdev(w_list)
h_1_std_start, h_1_std_end = h_mean-h_std, h_mean+h_std
h_2_std_start, h_2_std_end = h_mean-(2*h_std), h_mean+(2*h_std)
h_3_std_start, h_3_std_end = h_mean-(3*h_std), h_mean+(3*h_std)

w_1_std_start, w_1_std_end = w_mean-w_std, w_mean+w_std
w_2_std_start, w_2_std_end = w_mean-(2*w_std), w_mean+(2*w_std)
w_3_std_start, w_3_std_end = w_mean-(3*w_std), w_mean+(3*w_std)

h_std_deviation_1=[i for i in h_list if i > h_1_std_start and i<h_1_std_end]
h_std_deviation_2=[i for i in h_list if i > h_2_std_start and i<h_2_std_end]
h_std_deviation_3=[i for i in h_list if i > h_3_std_start and i<h_3_std_end]

w_std_deviation_1=[i for i in w_list if i > w_1_std_start and i<w_1_std_end]
w_std_deviation_2=[i for i in w_list if i > w_2_std_start and i<w_2_std_end]
w_std_deviation_3=[i for i in w_list if i > w_3_std_start and i<w_3_std_end]

print("{}% of Data for Height Lies Within one Standard Deviation".format(len(h_std_deviation_1)*100/len(h_list)))
print("{}% of Data for Height Lies Within two Standard Deviation".format(len(h_std_deviation_2)*100/len(h_list)))
print("{}% of Data for Height Lies Within three Standard Deviation".format(len(h_std_deviation_3)*100/len(h_list)))

print("{}% of Data for Weight Lies Within one Standard Deviation".format(len(w_std_deviation_1)*100/len(w_list)))
print("{}% of Data for Weight Lies Within two Standard Deviation".format(len(w_std_deviation_2)*100/len(w_list)))
print("{}% of Data for Weight Lies Within three Standard Deviation".format(len(w_std_deviation_3)*100/len(w_list)))

##-------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:08/05/2019
#File_des:Multiple Histogram with legends and colors
##------------------------------------------------------------------------------------


from matplotlib import pyplot as plt


#Required list
hindi_grades=[30,20,40,50,80,80,60,25]
english_grades=[20,30,50,60,40,60,70,90]

'''
if you are plotting multiple bars for histogram then combine them into a single list
and other options also need to combine into single list for example

plt.hist(data,parameters)

data=[hindi_grades,english_grades]
color=['g','r'] or color=['green','red']

'''

#plot hindi and english grades using histograms

plt.hist([hindi_grades,english_grades],color=['g','y'],label=['hindi','English'])
plt.xlabel("Grades range")
plt.title("Grade analysys")

#Add Legend
plt.legend()

plt.show()

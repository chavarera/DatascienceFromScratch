##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:04/005/2019
#File_des:Introduction of Barchart
##------------------------------------------------------------------------------------------------------

from matplotlib import pyplot as plt
import numpy as np

#Create a plot with x and y axis data
movies_cat=['Drama','Action','Science','Love','Terror','Romantic','Animation']
count=[70,20,30,42,18,28,37]

# To Simple vertical bar plot use plt.bar(xaxis,yaxis)
plt.bar(movies_cat,count)

#For Horizontal bar plotting use :plt.barh(xaxis,yaxis)
#plt.barh(movies_cat,count)

#Add a Title to bar chart
plt.title("Simple verticle bar")

#Add Label to X Axis
plt.xlabel("Category",fontsize=10) #you can use different option like fontsize 

#Add Label to Y Axis
plt.ylabel("Movies Count")


#for saving barchart to local
plt.savefig("Simpleverticlebarchart.png")

plt.show()

##-------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:08/05/2019
#File_des:Introduction of Histogram
#Offical Documentation:https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
##------------------------------------------------------------------------------------

'''
Histogram

    -A histogram is an accurate representation of the distribution of numerical data.
    -It is an estimate of the probability

Syntax:
    plt.hist(data,parameters)

Parameters:

    histtype :
    -'bar' is a traditional bar-type histogram. If multiple data are given the bars are arranged side by side.
    -'barstacked' is a bar-type histogram where multiple data are stacked on top of each other.
    -'step' generates a lineplot that is by default unfilled.
    -'stepfilled' generates a lineplot that is by default filled.'
    
    bins:
        -the count of ranges bins
        -By defualt 10 bins are created
        #Example:plt.hist(data,bins=5) 5 ranges bins are created

        -to create custom bins use array of sequences list
        
        plt.hist(data,bins=[10,30,50,70,90])
        this will produces follwing ranges bins
        0-10
        11-30
        31-50
        51-70
        71-90
        
        
    color:
        you can use green or g for color
        Example:plt.hist(data,color='g')
        
    orientation:
        -Bydefault vertical orientation
        -you can set 'horizontal' orientation for horizontal histogram
        Example:plt.hist(data,orienation='horizontal')

    rwidth:
        -rwidth is a relative width of bar according to area of plotting
        Example:plt.hist(data,rwidth=0.85)
        
'''
from matplotlib import pyplot as plt
#--------------------------------------------------------------------------
#               Simple Single Histogram
#--------------------------------------------------------------------------
grades = [83, 95, 91, 87, 70, 10, 85, 82, 100, 67, 73, 77, 10]

#By defualt 10 bins are created but we can control it as we required
plt.hist(grades,bins=5,rwidth=0.85,color='g')



#--------------------------------------------------------------------------
#               Some Usefull Options
#--------------------------------------------------------------------------

#Add Label to X Axis
plt.xlabel("Grade range")

#Add Label to Y Axis
plt.ylabel("Total no of students")

#Add Title
plt.title("Student Grade Analysis")





plt.show()

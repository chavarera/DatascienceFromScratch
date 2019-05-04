##------------------------------------------------------------------------------------------------------
#Created By:Ravishankar Chavare
#version:python 3.7
#Date:04/005/2019
#File_des:Plotting simple graph chart
##------------------------------------------------------------------------------------------------------

from matplotlib import pyplot as plt


#Create a plot with x and y axis data
year=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
jobs=[12,15,1,5,1,2,1,5,1,5]

#now create a plot 
plt.plot(year,jobs,marker='.',color="red",linestyle='dotted')

'''
Syntax:
  plt.plot(xaxisdata,yaxisdata,options*)

Some of the most used options:

1)marker:
  -point('.')
  -pixel(',')
  -circle('o')
  -start('*')
  
  All possible markers are defined here:
  https://matplotlib.org/api/markers_api.html

2)color:
  -red
  -green
  -blue
  -orange
  and others

3)linestyle:
  -solid
  -dotted
  -dashed
  -dasheddotted
  -dashdotdotted
  -for more linestyle visit
  https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html
'''
#For adding label to x axis
plt.xlabel("Values")

#for adding labe to y axis
plt.ylabel("years")

#Add a main title to plot
plt.title

#Saving the plot into images
'''
The savefig Method
-The .savefig() method requires a filename be specified as the first argument. 
-This filename can be a full path and as seen above, 
can also include a particular file extension if desired. 
-If no extension is provided, the configuration value of savefig.format is used instead

Syntax:
  plt.savefig(filename)
  
some of the Advanced savefig options
-dpi: can be used to set the resolution of the file to a numeric value.
-transparent: can be set to True, which causes the background of the chart to be transparent.
-bbox_inches: can be set to alter the size of the bounding box (whitespace) around the output image. In most cases, if no bounding box is desired, using bbox_inches='tight' is ideal.
-If bbox_inches is set to 'tight', then the pad_inches option specifies the amount of padding around the image.

'''
#simple plotted graph save
plt.savefig("SimpleGraphplot.png")



#Transparent Graph save
plt.savefig("TranparentGraphplot.png",transparent=True)


#Showing the ploted graph
plt.show()

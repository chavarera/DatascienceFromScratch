'''
Following are the some important libraries used for data plotting
1.Matplotlib
2.Seaborn
3.ggplot
4.Bokeh
5.Plotly
6.Pygal
7.Altair
8.Geoplotlib
9.Gleam
10.Missingno
11.Leather


We are Learning Matplotlib
---------------------------------------------------------------------------------
                                Basic
---------------------------------------------------------------------------------
    Matplotlib is a Python 2D plotting library which produces publication
    quality figures in a variety of hardcopy formats and interactive environments across platforms.
    Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers,
    and four graphical user interface toolkits.


---------------------------------------------------------------------------------
                            Installation
---------------------------------------------------------------------------------
    Open Command shell and type following command

    >python -m pip install -U matplotlib

    and wait to install matplotlib(make sure interent is working Before Installation)

    or you can follow Official steps:
    https://matplotlib.org/users/installing.html

for official documentation visit here
https://matplotlib.org/users/index.html

'''
#Import pyplot from matplotlib
from matplotlib import pyplot as plt

'''
What is pyplot
-matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB.
-Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure,
plots some lines in a plotting area, decorates the plot with labels, etc
-
'''
#plot simple list
lst=[1,2,3,4,8,12]

plt.plot(lst) #this will plot a plot
plt.ylabel('Simple List') #Add Y axis label
plt.title("This is Simple graph")
plt.show() #Final step to show the plot




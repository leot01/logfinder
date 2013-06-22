# .*. coding: utf-8 .*.

"""
Find the files into a directory and generate a list with the 
information if the directory does not exists a error message is 
showed, also the diorectory content is verify to detect if it is empty
"""

import re
import os
import gtk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar

#-----------------------------------------------------------------------		
class Algorithm01(object):
	
	def graph_frequency(self, hit_count_list, logfile_list, string):
		
		#bin width definition
		width = 0.5

		#GTK window generation
		win = gtk.Window()
		win.connect("destroy", lambda x: gtk.main_quit())
		win.set_default_size(840,520)
		win.set_title("LogFinder Chart")

		vbox = gtk.VBox()
		win.add(vbox)

		fig = Figure(figsize=(5,4), dpi=100)
		canvas = FigureCanvas(fig)  # a gtk.DrawingArea
		
		#Axis place definition and names setting
		ax = fig.add_subplot(211)
		ax.grid(True)		
		ax.set_title('Histogram for: "' + string + '"' )
		ax.set_xlabel('Source Files')
		ax.set_ylabel('Frequecy')
		ax.bar(range(len(hit_count_list)), hit_count_list, width, color='g')
		
		#Range axis definition and configuration		
		N = len(logfile_list)
		ind = np.arange(N)  # the x locations for the groups
		ax.set_xticks(ind) #(ind+(width/2))
		ax.set_xticklabels(logfile_list, rotation = 80)

		vbox.pack_start(canvas)
		
		#Adding the toolbar
		toolbar = NavigationToolbar(canvas, win)
		vbox.pack_start(toolbar, False, False)
		
		#Adding the cursor 
		cursor = Cursor(ax, useblit=True, color='red', linewidth=0.7 )
		
		#show all
		win.show_all()
		gtk.main()

#~ a = Algorithm01()
#~ a.graph_frequency(1,2)

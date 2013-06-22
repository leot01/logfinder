# .*. coding: utf-8 .*.

"""
Name: mainWin.py
Version: 0.2.0
Date: 20120408
status: draft
Author: Ing. Leonardo Trentin
mail: leotrentin@gmail.com
"""
import re
import os
import gtk
import aboutOf
import report
import algorithm01
from system import messages

class MainWin(object):
	
	global	a, b, al
	a = b = al = ''

	def __init__(self):

		# Load Glade main window file
		objsw = gtk.Builder()
		objsw.add_from_file('views/mainWin.glade')
		
		# Get widget to use
		self.winMain = objsw.get_object('winMain')
		self.text2Find = objsw.get_object('text2find')
		self.textWildcard = objsw.get_object('textwildcard')
		self.folderDirectory = objsw.get_object('folderDirectory')
		self.freqfound = objsw.get_object('freqfound') #textview
#		self.logentry_window = objsw.get_object('logentry_window')
				
		# Connect signals to methods of the class
		objsw.connect_signals(self)
		self.winMain.show()
		
		# Create a instance of Algorithm01
		global al
		al = algorithm01.Algorithm01()	
	
	def on_winMain_destroy(self, widget):
		gtk.main_quit()

	def on_run_clicked(self, widget):
		global a, b, al 
		t2f = self.text2Find.get_text()
		tw = self.textWildcard.get_text()
		fd = self.folderDirectory.get_filenames()
		
		if tw == '':
			mostrar = messages.error(self.winMain, messages.WILDCAR_NOK)
			print mostrar		
		elif t2f == '':
			mostrar = messages.error(self.winMain, messages.STRING_NOK)
			print mostrar
		else:
			[a, b]=self.findpattern(tw, t2f, fd[0])
			
	#-----------------codigo mudado start
	def findpattern(self, wildcard, string, path):
		
		#Buffer
		buf = self.freqfound.get_buffer()
		
		#Directory file list Generation 
		logfilelist = os.listdir(path) # Generates the files list
		
		#Sort the list
		logfilelist.sort() 
					
		global hit_count_list, logfile_list, hit
		logentry = open('logentry.txt', 'w')
		hit_count_list = []
		logfile_list = []
		pattern = '(.*)'
		c = 0
		parts = string.split(wildcard)
		
		for i in parts:
			pattern = pattern + parts[c] + '(.*)'
			c = c + 1
		
		#finding algorithm
		n = 1
		all_files_count = 0
		
		iter = buf.get_end_iter()
		buf.insert(iter, '------------------start-----------------\n')
		
		for logfile in logfilelist:
						
			if os.path.isdir(os.path.join(path, logfile)) == True:
				print 'Es un directorio....:', logfile

			else:				
				file = os.path.join(path, logfile)
				text = open(file, 'r')
				
				hit_count = 0
				
				for line in text:
					if re.match(pattern, line):
						all_files_count = all_files_count + 1 
						hit_count = hit_count + 1
						print >>  logentry, str(all_files_count) + ': ' + logfile + ' | ' + line,
				hits2show = str(n) + ': ' + logfile + ' => ' + str(hit_count)
				print str(n) + ': ' + logfile + ' => ' + str(hit_count)
				n = n + 1

				#print into the window frequency of the string
				iter = buf.get_end_iter()
				buf.insert(iter, hits2show)
				iter = buf.get_end_iter()
				buf.insert(iter, '\n')
				
				#insert new line into the logentry file
				hit_count_list.append(hit_count)
				logfile_list.append(logfile)
				
				#close the file "n"
				text.close()

		#print end of the current running
		iter = buf.get_end_iter()
		buf.insert(iter, '------------------end------------------')
		iter = buf.get_end_iter()
		buf.insert(iter, '\n')
			
		#close de fill logentry file 	
		logentry.close()
		
		return hit_count_list, logfile_list
		
	#-----------------codigo mudado end	

	def on_draw_clicked(self, widget):
		global a, b, al
		if a == '' or b == '':
			mostrar = messages.error(self.winMain, messages.NO_DATA_DRAW)
			print mostrar
		else:
			print '---------------a', a
			print '---------------b', b
			
			t2f = self.text2Find.get_text()
			al.graph_frequency(a,b,t2f)
			

	def on_report_view_clicked(self, widget):
		global a, b
		if a == '' or b == '':
			mostrar = messages.error(self.winMain, messages.NO_DATA_REPO)
			print mostrar
		else:
			logfile=open('logentry.txt','r')
			f = logfile.read()
			logfile.close()
			rep = report.Report()
			rep.text2show(f)

	def gtk_widget_show(self, widget):
		aboutOf.AboutOf()

	def gtk_main_quit(self, widget):
		gtk.main_quit()

# Only executed when it is rinning as main window
if __name__ == '__main__':
	app = MainWin()
	gtk.main()
		


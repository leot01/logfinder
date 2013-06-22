# -*- coding: utf-8 -*-
"""
File: report.py 20120402 
Detail: load report and connect the events
author: Leonardo Trentin
mail: leotrentin07@gmail.com
"""

import gtk

class Report(object):

	def __init__(self):

		# Load Glade "report" window file
		objsW = gtk.Builder()
		objsW.add_from_file('views/report.glade')

		# Get widget to use 
		self.winMain = objsW.get_object('winMain')

		# Connect signals to methods of the class
		objsW.connect_signals(self)
		self.winMain.show()
		self.logentry_window = objsW.get_object('logentry_window')	
		
	def text2show(self, f):
		
		#Buffer
		buf = self.logentry_window.get_buffer()	
		
		iter = buf.get_end_iter()		
		buf.insert(iter, f)


	def on_botonCerrar_clicked(self, widget):
		self.winMain.destroy()

	def on_winMain_destroy(self, widget):
		# Esto es solamente por si se llama a la ventana como programa principal, para poder cerrarla
		if __name__ == '__main__':
			gtk.main_quit()
		else:
			self.winMain.destroy()
			
	def display(self,widget):

		textview = self.wTree.get_widget('textview1')
		textbuffer = textview.get_buffer()
		start = textbuffer.get_start_iter()
		end = textbuffer.get_end_iter()
		textlines = textbuffer.get_text(start, end) #retrieve the text
		line_count = textbuffer.get_line_count()
		char_count = textbuffer.get_char_count()
		
		self.wTree = gtk.glade.XML(gladeFile)
		self.entryForText = self.wTree.get_widget("name_of_text_widget_in_glade_file")
		
		text = self.textview1.get_buffer()
		
		print 	line_count

# Only executed when it is rinning as main window
if __name__ == '__main__':
	app = Report()
	gtk.main()

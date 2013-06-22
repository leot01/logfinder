# -*- coding: utf-8 -*-
"""
File: aboutOf.py 20120303 
Detail: load aboutOf and connect the events
author: Leonardo Trentin
mail: leotrentin07@gmail.com
"""

import gtk

class AboutOf(object):

	def __init__(self):

		# Load Glade "about" window file
		objsW = gtk.Builder()
		objsW.add_from_file('views/aboutOf.glade')

		# Get widget to use 
		self.winMain = objsW.get_object('winMain')

		# Connect signals to methods of the class
		objsW.connect_signals(self)
		self.winMain.show()

	def on_botonCerrar_clicked(self, widget):
		self.winMain.destroy()
		#print 'laal'

	def on_winMain_destroy(self, widget):
		# Esto es solamente por si se llama a la ventana como programa principal, para poder cerrarla
		if __name__ == '__main__':
			gtk.main_quit()
		else:
			self.winMain.destroy()

# Only executed when it is rinning as main window
if __name__ == '__main__':
	app = AboutOf()
	gtk.main()

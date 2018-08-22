#!usr/bin/python
# -*- coding: utf-8 -*-

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

from re import findall
import webbrowser

jobsTotal = 0

linkedInUrl   = 'https://linkedin.com/in/<user>'
portfolioUrl  = 'https://example.com/'
addressString = '742 Evergreen Terrace'
phoneString   = '5559025'
mailString    = 'example@email.com'

linkedInImagePath  = 'Images/Linkedin.gif'
portfolioImagePath = 'Images/Portfolio.gif'
addressImagePath   = 'Images/Address.gif'
phoneImagePath     = 'Images/Phone.gif'
mailImagePath      = 'Images/Mail.gif'

linkedInImage  = ''
portfolioImage = ''
addressImage   = ''
phoneImage     = ''
mailImage      = ''

JOBS_ARRAY = []

def buildLayout( root ):
	global linkedInImage
	global portfolioImage
	global addressImage
	global phoneImage
	global mailImage 
	global loadButton

	linkedInImage = tk.PhotoImage(file=linkedInImagePath)
	portfolioImage = tk.PhotoImage(file=portfolioImagePath)
	addressImage = tk.PhotoImage(file=addressImagePath)
	phoneImage = tk.PhotoImage(file=phoneImagePath)
	mailImage  = tk.PhotoImage(file=mailImagePath)
	
	linkedInButton = tk.Button(root, width=32, height=32, image=linkedInImage,
								command=lambda: setClipboard(root, linkedInUrl))
	linkedInButton.grid(row = 0, column = 0, padx=(0,2))

	itchioButton = tk.Button(root, width=32, height=32, image=portfolioImage,
								command=lambda: setClipboard(root, portfolioUrl))
	itchioButton.grid(row = 0, column = 1, padx=(5,2))

	addressButton = tk.Button(root, width=32, height=32, image=addressImage,
								command=lambda: setClipboard(root, addressString))
	addressButton.grid(row=0, column=2, padx=(5,2))

	phoneButton = tk.Button(root, width=32, height=32, image=phoneImage,
								command=lambda: setClipboard(root, phoneString))
	phoneButton.grid(row=0, column=3, padx=(5,2))

	mailButton = tk.Button(root, width=32, height=32, image=mailImage,
								command=lambda: setClipboard(root, mailString))
	mailButton.grid(row=0, column=4, padx=(5,2))

	loadButton = tk.Button(root, text='  Load  ', height=2,
								command=lambda: loadButtonCallback(root))
	loadButton.grid(row=0, column=5,padx=(5,0))

def loadButtonCallback( root ):
	global JOBS_ARRAY
	global jobsTotal
	global jobLabel

	if len(JOBS_ARRAY) == 0:
		jobData = root.clipboard_get()
		JOBS_ARRAY = findall('(http\S*)', jobData)
	else:
		if len(JOBS_ARRAY) > 0:
			webbrowser.open(JOBS_ARRAY.pop(), new=2, autoraise=True)
	
	jobsTotal = len(JOBS_ARRAY)

	if jobsTotal > 0:
		loadButton.config(text = '{0}'.format(jobsTotal).center(10))
	else:
		root.clipboard_clear()
		loadButton.config(text='  Load  ')

def setClipboard( root, text ):
	root.clipboard_clear()
	root.clipboard_append( text )

def main(): 
	root = tk.Tk()
	buildLayout( root )
	root.wm_title('Job Application Helper')
	root.wm_attributes("-topmost", 1)
	root.mainloop()

if __name__ == '__main__':
	main()
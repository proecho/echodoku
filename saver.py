import sys
import tkinter
from tkinter import filedialog



def saver(listoflist,window):
	window.filename = filedialog.asksaveasfilename(initialdir = "/echo/echodoku/savesudos", title = "save sudoku", defaultextension = ".sud" )
	filesave = open(window.filename,"w")
	for listing in listoflist:
		filesave.write(",".join([str(box.get()) for box in listing]))
		filesave.write("\n")

	filesave.close()


def loader(listoflist,window):
	listofvalue =[]
	window.filename = filedialog.askopenfilename(initialdir = "/echo/echodoku/savesudos",title = "Select saved sudoku",filetypes = [("sudoku files" , "*.sud" )])
	fileload = open(window.filename,"r")
	line = fileload.readline()
	while line:
		listed = line.split(",")
		listofvalue.append(listed)
		line = fileload.readline()
	fileload.close()
	jointlist = zip(listoflist,listofvalue)
	for list1,list2 in jointlist:
		for box1,box2 in zip(list1,list2):
			box1.delete(0,10)
			box1.insert(0,int(box2))
	
	

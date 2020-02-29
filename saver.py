import sys
import tkinter


def saver(listoflist):
	filesave = open(input("what filename?"),"w")
	for listing in listoflist:
		filesave.write([str(box.get()) for box in listing].join(","))
		filesave.write("\n")

	filesave.close()


def loader(listoflist):
	listofvalue =[]
	fileload = open(input("what filename?"), "r")
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
	
	

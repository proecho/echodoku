from solveintfunctions import answercheck
from solveintfunctions import optionsboxgen 
from solveintfunctions import onlycheck 
from sudchecker import validcheck
import tkinter




def solvesud(listoflist,listofbox):
	validcheck(listoflist,listofbox) 
	finishcount = 0
	finish = False
	while finish == False:
		
		finish = True
		
		infolist,finish = answercheck(listoflist,listofbox,finish)	
		
		transoptionslist = optionsboxgen(listoflist,listofbox,infolist)
	
		
					
		onlycheck(listoflist,listofbox,infolist,transoptionslist,finish)
		

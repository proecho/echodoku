from solvebasicfunctions import valueinserter
import tkinter


def answercheck(listoflist,listofbox,finish):	
	infolist=[]
	for row in listoflist: #check for only answer
		rowcount=0
		inforow = []
		for box in row:
			options = []
			for a in range(1,10):
				options.append(a)
			
			checkcount = 0	
			for checkbox in row:
				if rowcount != checkcount: # ummmm WORRIES ABOUT THIS 
					if options.count(int(checkbox.get())) > 0:
						options.remove(int(checkbox.get()))
				checkcount += 1 # ummmmm
					
			for checkrow in listoflist:
				
				if options.count(int(checkrow[rowcount].get())) >0:
					options.remove(int(checkrow[rowcount].get()))
					
			
			for tranlist in listofbox:
				for tranbox in tranlist:
					if box == tranbox:
						for checktranbox in tranlist:
							if options.count(int(checktranbox.get())) >0:
								options.remove(int(checktranbox.get()))
			inforow.append(options)
			finish = valueinserter(options,box,finish)
			rowcount += 1
		infolist.append(inforow)

	return (infolist, finish)

def optionsboxgen(listoflist,listofbox,infolist):
	transoptionslist = []
	

	for tranlist in listofbox: #construct box list of options
		
		transoptionsrow = []
		for	tranbox in tranlist:
			transcolumncount = 0
			
			for row in listoflist:
				transrowcount = 0
				for box in row:
					if tranbox ==box: #is finding one value for each is finding each box once
					
						
						transinforow = infolist[transcolumncount]
						transoptions = transinforow[transrowcount]
						transoptionsrow.append(transoptions)
					transrowcount += 1
				transcolumncount += 1
		transoptionslist.append(transoptionsrow)	
	
	return transoptionslist
	
def onlycheck(listoflist,listofbox,infolist,transoptionslist,finish):
	columncount = 0
	
	for row in listoflist: #only place for answer check
				rowcount=0
				for box in row:
					inforow=infolist[columncount]
					
					options = []
					for a in inforow[rowcount]:
						options.append(a)
					for checkoptions in inforow:
						for check in checkoptions:
							if options.count(check) > 0:
								options.remove(check)
								 
					finish = valueinserter(options,box,finish)
					
					options = []
					for a in inforow[rowcount]:
						options.append(a)
					for checkrow in infolist:
						for check in checkrow[rowcount]:
							if options.count(check) > 0:
								options.remove(check)
					finish = valueinserter(options,box,finish)
					
					options = []
					for a in inforow[rowcount]:
						options.append(a)	
					transcolumncount = 0
					for translist in listofbox:
						transrowcount = 0						
						for transbox in translist:							
							if box == transbox: #is correctly only finding one option is also finding one for all 81 ever
								transinforow =[]
								for a in transoptionslist[transcolumncount]:
									transinforow.append(a)

								currentcount=0
								for transoptions in transinforow:
									if transrowcount != currentcount:
										for transcheck in transoptions:
											if options.count(transcheck) > 0:
												options.remove(transcheck)
								
									currentcount += 1
								finish = valueinserter(options,box,finish)
					
							transrowcount += 1
						transcolumncount += 1 
						
				
					
					rowcount +=1
				columncount +=1
	return(finish)

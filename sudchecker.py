def checklegitamitelines(listoflist):
	for a in listoflist:
		for b in a:
			if b.get!=0:
				if a.count(b.get) > 1:
					return(1)
	return(0)
					

def checklegitamitecolumns(listoflist):
	for a in range(0,9):
		countinglist=[]
		for b in listoflist:
			if b[a].get !=0:
				countinglist.append(b[a].get)
				if countinglist.count(b[a].get) > 1:
					return(1)
	return(0)


 
def makecubelist(listoflist): #makes a list of list where each list is all the elemements in a given square 
	listofbox = []
	workingblist=[]
	count1 = 0
	count3 = 0
	for row in listoflist:
		count2 = 0
		if count1 == 0 or count1 == 3 or count1 == 6:
			for box in row:
				count2 += 1
				workingblist.append(box)
				if count2 == 3 or count2 == 6 or count2 == 9:
					listofbox.append(workingblist)
					workingblist = []
			count1 += 1
			count3 +=1
		else:
			for box in row:
				count2 += 1
				workingblist.append(box)
				if count2 == 3 or count2 == 6 or count2 == 9:
					for boxb in workingblist:
						listofbox[int((count2 /3 + (count3 - 1)*3))-1].append(boxb)
					workingblist =[]
			count1 += 1
	return listofbox

def checklegitamitesquare(listofbox):			
		for alist in listofbox:
			for box in alist:
				if box.get != 0:
					if alist.count(box.get) > 1:
						return(1)
		return(0)
			
		
def validcheck(listoflist,listofbox):
	if checklegitamitecolumns(listoflist) + checklegitamitelines(listoflist) + checklegitamitesquare(listofbox) > 0:
		raise Exception("not a sudoku")



import tkinter
from solvingfinal import solvesud
from sudchecker import makecubelist
from saver import saver		
from saver import loader

window=tkinter.Tk()
window.title("sudoku")

listoflist=[]
for a in range(0,9):
	blist = []
	for b in range(0,9):
		a1 = (tkinter.Entry(window,width=1))	
		a1.grid(row = a, column = b)
		blist.append(a1)
	listoflist.append(blist)
listofbox = makecubelist(listoflist)

for row in listoflist:
	for box in row:
		box.insert(0,0)






#test1 =listoflist[0]
#test1[0].delete(0,10)
#test1[0].insert(0,2)
#test2 =listoflist[1]
#test2[3].delete(0,10)
#test2[3].insert(0,2)
#test3 =listoflist[8]
#test3[8].delete(0,10)
#test3[8].insert(0,2)
#test4 =listoflist[5]
#test4[7].delete(0,10)
#test4[7].insert(0,2)

buttonsolve = tkinter.Button(text = "solve", command = lambda: solvesud(listoflist,listofbox))
buttonsolve.grid(row =10,column = 10)

buttonsave = tkinter.Button(text = "save", command = lambda: saver(listoflist))
buttonsave.grid(row =11,column = 10)

buttonload = tkinter.Button(text = "Load", command = lambda: loader(listoflist))
buttonload.grid(row =12,column = 10)

window.mainloop()

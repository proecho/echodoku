	
def valueinserter(options,box,finish):
	if len(options) == 1:
		if int(box.get()) == 0:
					value = str(options[0])
					box.delete(0,10)
					box.insert(0,value)
					return False
		
	return finish
					
	


##Declaring Empty List
myUniqueList=[]
myLeftovers=[]


##Function Definition
def listgenerator(a):

	if a not in myUniqueList:
		myUniqueList.append(a)	
	else:
		leftlistgen(a)
	return

def leftlistgen(a):
	myLeftovers.append(a)
	return

##Test Inputs

listgenerator(1)
listgenerator(2)
listgenerator(3)
listgenerator(1)

##Output Display
print(myUniqueList)
print(myLeftovers)




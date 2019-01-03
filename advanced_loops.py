##Defining the rows and columns of the board game
def boardgame(n):
	if n<=51:
		for row in range(n):
			if row%2 == 0:
				for column in range(n):
					if column%2 == 0:
						print("|",end="")
					else:
						print(" ",end="")
				print(" ")
			else:
				for column1 in range(n):
					print("-",end="")
				print(" ")
		print(True)
	else:
		print(False)

boardgame(51)


	
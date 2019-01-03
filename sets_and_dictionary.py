#Attributes about a song
Dictionary = {"singer":"Ed Sheeran", "genre":"pop","RuntimeInMinutes":233,"year":"2017","producer":"Steve Mac","Studio":"Rock Stone Studio"}
#Printing the Variables
for i in Dictionary:
	print(i)
	print(Dictionary[i])

#Guess the song competition
def guess_the_song(i,j):
	if i in Dictionary:
		if Dictionary[i] == j:
			print(True)
		else:
			print(False)
	else:
		print(False)
	return

i=input("Song Attribute Name\n")
j=input("Song Attribute Value\n")

guess_the_song(i,j)


"""
I am a the 9th all-time popular song

"""
import random 
numer = int (input("whats the maximum?"))
ran=random.randint(1, numer)
while True:
	guess=int(input("guess"))
	if guess == ran:
		print("yay!you won!")
	else:
		print ("try again")

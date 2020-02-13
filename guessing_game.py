from random import randint
print (
'''
####### LET'S PLAY THE GUESSING GAME ######
You have to guess a number that the code has generated randomly.
1) If your guess is less than 1 or greater than 100, the message is "OUT OF BOUNDS"
2) If on your first turn, your guess is within 10 of the number, the message is "WARM!"
3) If the guess is further than 10 away from the number, the message is "COLD!"
On all subsequent turns, if your guess is:
1) Closer to the number than the previous guess the message is "WARMER!"
2) Further from the number than the previous guess, the message is "COLDER!"
When your guess equals the number, the game is over and you can see many guesses it took!

Have fun !

###########################################
''')
number = randint(1,100)
count = 0
last_guess=None
while True:
	guess = int(input("What is your guess? "))
	count = count+1
	if guess < 0 or guess > 100:
		print("OUT OF BOUNDS")
		continue
	diff = abs(number-guess)
	if diff == 0:
			print("Found on {} try".format(count))
			break
	if count == 1:
		if diff <=10:
			print("WARM!")
		elif diff > 10:
			print("COLD!")
		last_guess=guess
	else:
		last_diff=abs(number-last_guess)
		if last_diff < diff:
			print("COLDER!")
		elif last_diff >= diff:
			print("WARMER!")
		last_guess=guess
		continue
import random
x = random.randint(1, 100)
while True:
	r = input('Enter the number you think between 1 to 100: ')
	if int(r) == int(x):
		print('You are correct!')
		break
	elif int(r) != int(x):
		print('You entered the wrong answer, please try again.')
		if int(r) > int(x):
			print('your answer is bigger than the real answer.')
		elif int(r) < int(x):
			print('your answer is smaller than the real answer.')
import time
import math as m

def stopwatch():
	inp = input(">>> Press enter to start and stop")
	print(">>> Started")
	start = time.time()
	input()
	print(">>> Stop!")
	end = time.time()
	print(end-start)

def accuracy():
	inp = float(input(">>> For how many seconds should I wait?\n    "))
	input(">>> When you press enter, the timer will start.")
	print(">>> Stop me after", inp, "seconds")
	start = time.time()

	# whilst input is not given keep printing the time in seconds

	input()
	print(">>> Stop!")
	end = time.time()
	print(">>> You stopped me after", (end-start), "seconds")
	acc = m.fabs(((end-start))-inp)
	acc = round(acc, 4)
	print(">>> You were accurate to", acc, "seconds")

again = "Y"

while again.lower() in ["y","yes"]:
	mode = input(">>> Write 's' for stopwatch, 'a' for accuracy\n    ")
	if mode in ["s","S"]:
		stopwatch()
	if mode in ["a","A"]:
		accuracy()
	again = input(">>> Again? Y/N\n    ")

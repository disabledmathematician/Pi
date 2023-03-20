def PiCharles():
	odd_numbers = list(2 * number + 1 for number in range(1, 2000000, 1))
	Pi = 1 # Until the summands are completed
	for index in range(1, 2000000, 1):
		if index % 2 != 0:
			Pi -= 1/odd_numbers[index - 1]
		else:
			Pi += 1/odd_numbers[index - 1]
	Pi *= 4
	print("Pi is approximately: {}".format(Pi))
	print("Charles Thomas Wallace Truscott")
if __name__ == "__main__": PiCharles()
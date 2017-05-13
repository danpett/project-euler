def additor():
	add = 0
	N =1000

	for number in range(1,N):
		if number % 3 == 0 or number % 5 == 0:
			add += number

	print add

if __name__ == "__main__":
    additor()

def main():

	st = input("Enter string\n")
	p=0
	for i in reversed(st):
		p = 10*p +ord(i)
	print(p)
if __name__ == '__main__':
	main()

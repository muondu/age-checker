def prompt():
	global input1
	input1 = int(input("Enter your age:  "))
	
def  main():
	prompt()
	if input1 > 18 and input1 == 18:
		print("Is an adult")
	else:
		print("Is not an adult")
main()
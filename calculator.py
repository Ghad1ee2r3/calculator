
def main():
	#write your code here
	pass

	#write your code here
	
	num1= input("Enter a number one:")
	num2= input("Enter a number two:")
	int_num1= int(num1)
	int_num2= int(num2)

	op= input("Choose the operation (+, -, /, *): ")
	if op=="+":
		print(int_num1+int_num1)
	else:
		if op=="-":
			print( int_num1-int_num1)
		else:
			if op=="*":
				 print( int_num1*int_num1)
			else:
				if op=="/":
					print( int_num1/int_num1)


	



if __name__ == '__main__':
	main()

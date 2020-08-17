
def main():
	#write your code here

	num1= input("Enter a number one:")
	num2= input("Enter a number two:")
	if num1.isdigit() and num2.isdigit() :
		int_num1= int(num1)
		int_num2= int(num2)
		op= input("Choose the operation (+, -, /, *): ")
		if op=="+":
			print(int_num1+int_num2)
		elif op=="-":
			print( int_num1-int_num2)
		elif op=="*":
			print( int_num1*int_num2)
		elif op=="/":
			print( int_num1/int_num2)
		else:
			print( "you are enter invalid operation")

	else:
		print(" invalid")
	#int_num1= int(num1)
	#int_num2= int(num2)





	#if op=="+":
	#	print(int_num1+int_num1)
	#else:
	#	if op=="-":
		#	print( int_num1-int_num1)
		#else:
		#	if op=="*":
		#		 print( int_num1*int_num1)
		#	else:
		#		if op=="/":
		#			print( int_num1/int_num1)






if __name__ == '__main__':
	main()

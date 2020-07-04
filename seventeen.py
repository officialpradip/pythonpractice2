'''Write a program that serves as a basic calculator. It asks for
 two numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.'''

def add(num1, num2): 
	return num1 + num2 
def subtract(num1, num2): 
	return num1 - num2 
def multiply(num1, num2): 
	return num1 * num2  
def divide(num1, num2): 
	return num1 / num2 
print("Choose operation -\n"  
		"1. Add\n" 
		"2. Subtract\n"  
		"3. Multiply\n" 
		"4. Divide\n") 
 
select = int(input("Select operations form 1, 2, 3, 4 :")) 
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
try:
    if select == 1: 
        print(num1, "+", num2, "=", add(num1, num2)) 

    elif select == 2: 
        print(num1, "-", num2, "=", subtract(num1, num2)) 

    elif select == 3: 
        print(num1, "*", num2, "=", multiply(num1, num2)) 

    elif select == 4: 
        print(num1, "/", num2, "=", divide(num1, num2)) 
    else: 
        print("Invalid input") 
except ZeroDivisionError:
    print("Divide by 0 Error")


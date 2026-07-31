num1 = float(input("enter first number:"))
num2 = float(input("enter your second number:"))

operation = input("Choose operation (+,-,*,/):")

if operation == "+":
    result = num1 + num2 

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2 

else: 
    result = "invalid oparation"
 
print("==================================") 
print (num1 , operation, num2, "=", result)
print("==================================")
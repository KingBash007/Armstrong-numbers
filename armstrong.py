#Program to find if a number is an armstrong number
#Take input from the user
number = int(input("input your number:"))
#Calculate number of digits
digits = len(str(number))
#initialize result variable
resultnumber = 0
#Find the sum of the A^digits of each digit
temp = number
while temp>0:
    digit = temp % 10
    resultnumber += digit**digits
    temp//=10
#Display the results
if number== resultnumber:
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")    
    

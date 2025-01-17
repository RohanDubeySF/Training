#Write a program that asks the user to input a number. The program should attempt to multiply the number by 2. If the number is negative, it should attempt to calculate the square root
import math
try : 
    num=int(input("Enter a Number: "))
    if num<0:
        print(math.sqrt(num))
    else:
        print(num*2)

except Exception as e:
    print(e)
    
finally:
    print("Task Done")


"""Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.

    The program should take input from console or args and should handle unexpected inputs    

    Constraints:

        - For loop is not allowed

        - input should be in words:

            - e.g.: onetwo = 12, sixone = 61

        - words will be within zero to nine

        - Cannot use inbuilt methods like max, min, or any math function    

    Example 1:

        - Input 1: onezero

        - Input 2: twozero

        - Output: onezero

    Example 2:

        - Input 1: twosix

        - Input 2: twofour

        - Output: two       """


num = ['zero','one','two','three','four','five','six','seven','eight','nine'] 

def convert(no):
    no=no.lower()
    i=0
    while i<10:
        if num[i] in no:
          no=no.replace(num[i],str(i))
        i+=1
    return int(no)

def word(n):
   result=str(n)
   i=0
   while i<10: 
        result=result.replace(str(i),num[i])
        i+=1
   return result 

"""
def gcd(Num1,Num2):
   Num1=convert(Num1)
   Num2=convert(Num2)
   minimum=Num1 if Num1<Num2 else Num2
   i,factor=2,1
   if Num1<0 or Num2<0:
      raise Exception
   elif Num1==0 and Num2==0:
      print(f"The GCD is {num[0]}")
   elif Num1>0 and Num2>0:
      while i<minimum:
         while Num1%i==0 and Num2%i==0 :
            Num1,Num2=Num1/i,Num2/i
            factor*=i
         i+=1
      fac=word(factor)
      print(f"The GCD is {fac}")
"""
def gcd(num1,num2):
   if num2==0:
      fac=word(num1)
      print(f"The GCD is {fac}")
   elif num1==0 and num2==0:
       print(f"The GCD is {num[0]}")
   else :
      if num1>num2:
         num1,num2=num2,num1%num2
         gcd(num1,num2)
      else:
         gcd(num2,num1)

try:
  Num1=input("Enter 1st Number: ")
  Num2=input("Enter 2nd NUmber: ")
  Num1=convert(Num1)
  Num2=convert(Num2)
  if Num1<0 or Num2<0:
      raise Exception
  gcd(Num1,Num2)
except Exception :
   print("Invalid Input")

   


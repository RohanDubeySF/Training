try:
    num1=int(input("Enter num1: "))
    num2=input("Enter num2: ")
    result=num1/num2
except Exception as e:
    print(f"you have encountered {e} Exception")
else:
    print(f"{result}")

finally:
    print("Task Completed")
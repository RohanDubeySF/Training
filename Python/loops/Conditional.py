#Python program that takes a list of integers from the user and prints the second largest number in the list.
def secondmax(num):
    max=l[0]
    max2=l[0]
    for a in range(1,len(l)):
        if l[a]>max:
            max=l[a]
    for a in range(1,len(l)):
        if l[a]<max and l[a]>max2:
            max2=l[a]
    else:
        if max==max2:
            print("all the elements are same")
        else:
            print(max,max2)


num=input("Enter a number:")
l=list(map(int, num.split(" ")))
secondmax(l)

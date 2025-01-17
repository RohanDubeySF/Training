dict={"Name":"Rohan","Surname":"Dubey","Branch":"AIML"}

print("Dict Keys:")
for a in dict:
    print(a,end=" ")

print("\nDict Values:")
for a in dict:
    print(dict[a],end=" ")
print()

print("Update Dictionary")
key=input("Enter a key:")
value=input("Enter a Value:")
dict.update({key: value})
print(dict)
import array as arr

a=arr.array('i',[1,2,3,4])
print("Creating Array\n")
for i in range(0, len(a)):
    print(a[i], end=" ")
print()

print("\nadding Element")
a.insert(4,5)
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
print("\nDeleting Element using Pop")
a.pop()
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
print("\nDeleting Element using Remove")
a.remove(2)
for i in range(0, len(a)):
    print(a[i], end=" ")
print()
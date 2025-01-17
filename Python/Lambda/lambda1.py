
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even=list(filter(lambda x : x %2==0, numbers) )
print(even)


words = ["apple", "banana", "cherry", "date"]

res=(list(map(lambda x : len(x), words)))
print(res)
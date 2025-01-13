#Given a list of integers, create a new list that contains the squares of all the even numbers from the original list.

orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq=[x**2 for x in orig if x%2==0]

print(sq)
#iven a list of tuples, where each tuple contains a student's name and their score, use a lambda function to sort the list in descending order based on the scores.

cores = [("Alice", 85), ("Bob", 70), ("Charlie", 95), ("David", 60)]

res=list(sorted(cores , key=lambda x : x[1] , reverse=True))
print(res)


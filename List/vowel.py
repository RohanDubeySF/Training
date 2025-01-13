
og = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]

res=[x for x in og if x[0].lower() in ['a','e','i','o','u']]

print(res)
#Write a function called is_palindrome(string) that takes a string as input and returns True if the string is a palindrome (reads the same backward as forward), and False otherwise. Ignore case and spaces while checking.

def palindrome(line):
    line=line.lower().replace(" ", "")
    if line==line[::-1]:
        return "True"
    else:
        return "False"


line=input("Enter a string: ")
#l=list(map(str,line.split(" ")))
print(palindrome(line))
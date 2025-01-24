"""2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Constraints:

        - 1 <= n <= 8

    Example 1:

        - Input: n = 3

        - Output: ["((()))","(()())","(())()","()(())","()()()"]

        - Example 2:

    Example 2:

        - Input: n = 1

        - Output: ["()"] 
"""

def parenthesis(n):
    open,close=0,0
    stack=[]
    res=[]

    def rec(open,close):
        if open==close==n:
            res.append("".join(stack))
            return
        if open<n:
            stack.append("(")
            rec(open+1,close)
            stack.pop()

        if close<open:
            stack.append(")")
            rec(open,close+1)
            stack.pop()
    rec(open,close)
    print(res)


try:
    N=int(input("Enter the Number: "))
    if N>8 or N==-1:
        print("Number Should be greater than -1 and less than 8")
    else:
        parenthesis(N)
except :
    print("Invalid Input")
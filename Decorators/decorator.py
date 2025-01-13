"""Create a decorator named time_it that measures the execution time of a function. Use this decorator to measure the time taken by a
function calculate_sum that computes the sum of all numbers from 1 to ( n ).""" 

import time

def time_it(function):
    def wrapper_f(*args,**kwargs):
        print("This is a decorator")
        start=time.perf_counter()
        res=function(*args,**kwargs)
        end=time.perf_counter()
        total=end-start
        print("Time taken {} seconds".format(round(total)))
    return wrapper_f

@time_it
def sum(n):
    sum=0
    for a in range(n):
        sum+=a
        time.sleep(1)
    print(sum)

sum(5)
import sys

def multiply_by_add(num1, times):
    if times == 1:
      return num1
    else:
       return num1 + multiply_by_add(num1, times -1)
    
# every recursive call creates another function call/frame. recursion has a cost
def factorial(n):
    if n==1:
       return 1
    else:
       return n* factorial(n-1)



print(sys.getrecursionlimit())
# You can modify the limit:
sys.setrecursionlimit(2000)

print(multiply_by_add(5, 5))
print(factorial(5))
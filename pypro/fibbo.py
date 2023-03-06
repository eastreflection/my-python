"""
Fibonacci Series in Python
"""

def fibbonacci():
    n = int(input("Enter Number\n"))
    n1 = 0
    n2 = 1
    print(n1, n2)
    for i in range(3, n+1):
        n3 = n2+n1
        n1 = n2
        n2 = n3
        print(n3, end=" ")


fibbonacci()

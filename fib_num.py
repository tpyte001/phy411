#homework 1 phy411
import numpy

# gives you specific Fibonocci number
def fib_number(n):
    n = (n-2)+(n-1)
    print(n)

fib_number(10000)

# generates Fibonocci sequence
def fib_seq(n):
    fib = []
    for i in range(n):
        a = (i-1)
        b = (i-2)
        c = a + b
        fib.append(c)
    print(fib)

# check
# fib_seq(n)

def fib_seq_while(n):
    a = 0
    b = 1
    s = 1
    while (s < 10,000):
        print(s)
        s = s + b
        b = s
        a = b


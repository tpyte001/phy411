# homework 1 phy411
import numpy

#maybe draw with turtle 
# F_{n} = F_{n-2} + F_{n-1}



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
    

n = 100

if fib_number(n) == fib_seq(n):
    print("You can go to bed now.")
else:
    print("Keep trying.")



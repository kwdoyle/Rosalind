def fib(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return k
    oneGen = fib(n-1, k)
    twoGen = fib(n-2, k)
    if n <= 4:
        return oneGen + twoGen
    return (oneGen + (twoGen * k))


print fib(30, 2)


# OR
def fib2(n, k):
    old,new = 1,1
    for i in range(2, n):
        old,new = new,k*old+new
    return new

print fib2(5,3)



# Recursively
def fibboh(n, k):
    if n==1:
        return 1
    if n==2:
        return 1
    Fn = fibboh(n-1, k) + k * fibboh(n-2, k)
    return Fn

print fibboh(5,3)

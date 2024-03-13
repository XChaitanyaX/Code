def isprime(n):
    return factors(n)==[1,n]

def factors(n):
    factors=[]
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors

def primesupto(n):
    l=[]
    for i in range(1,n+1):
        if isprime(i):
            l.append(i)
    return l

def nprimes(n):
    count,i,plist=0,1,[]
    while count<n:
        if isprime(i):
            count,plist=count+1,plist+[i]
        i=i+1
    return plist 
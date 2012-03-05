# 5 guys 1 monkey with n number of coconuts
# n % 5 != 0
# 
# while 5 guys
#  n - (n1 - 1 % 5 == 0) 
#  m += 1
#
# n = (n  - 1/5 ) % 5 = 0
# 

def f(n):
    # my solution
    # int(n)
    # n = (n - 1) - (n/5)
    # video solution
    return (n -1)/5 * 4
    

def f6(n):
    for i in range(6):
        n = f(n)
    return n

def is_int(n):
    return abs(n - int(n)) < 0.000001

n = 0
found = False
while not found:
    n += 1
    found = is_int(f6(float(n)))
print n


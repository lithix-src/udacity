#!/usr/bin/env python

# build a probability vector

def pvector(n):
    """Returns a vector of n length populated with 1./n probabilities"""
    return [1./n for p in range(n)]

def sense(p, Z, W, hit, miss, norm=True):
    """Returns a vector of p(Xi..|Z) in world W, 
    with weights hit,miss. If norm=True, the vector will be normalized (default)"""
    q = []
    for i in range(len(p)):
        prob = p[i]
        if Z == W[i]:
            q.append(prob * hit)
        else:
            q.append(prob * miss)
    if norm:
        n = sum(q)
        return [p/n for p in q]
    return q
    
p = pvector(5)
world = ['green', 'red', 'red', 'green', 'green']

# multiple sensor sweeps
def sweep_sensors(readings):
    return readings

def multi_sense_pvector(sweep_results, p, W, weights):
    pv = []
    for i in sweep_results:
        pv.extend(sense(p, i, W, weights[0], weights[1]))
    return pv

# robot motion quizz
world = [ 1./9, 1./3, 1./3, 1./9, 1./9 ]
def move(p, U=0):
    q = []
    for i in range(len(p)):
        # this part is wierd, think not of p being shifted to the right
        # think of q acquiring information from cells in p
        # each cell in q has to grab its value from the cell in p that
        # is to the left
        q.append(p[(i-U) % len(p)])
    return q

print world    
print move(world,2)

world = [0.2,0.2,0.2,0.2]
print world
print move(world,2)


print "inexact motion"
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def move(p, U=0):
    q = []
    for i in range(len(p)):
        # the total probability of state s
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

print move([0, 1, 0, 0, 0],1)

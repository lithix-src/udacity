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
print sense(p, 'red', world, 0.6, 0.2)

# multiple sensor sweeps
def sweep_sensors(readings):
    return readings

def multi_sense_pvector(sweep_results, p, W, weights):
    pv = []
    for i in sweep_results:
        pv.extend(sense(p, i, W, weights[0], weights[1]))
    return pv

print "multi sensor sweep"
print multi_sense_pvector(sweep_sensors(['red', 'green']),
                          pvector(5),
                          world,
                          (0.6, 0.2))

# robot motion quizz
world = [ 1./9, 1./3, 1./3, 1./9, 1./9 ]
def move_right(locality, cells, W):
    state = W.index(locality)
    new_state = [s for s in W[cells:]]
    new_state.extend(W[:state+1])
    return new_state
    
print world
print move_right(world[0], 1, world)

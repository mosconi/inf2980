from multiprocessing import Pool
from instance import instance
from permutation import permutation
from math import floor

from itertools import izip, repeat

import sys, random

permutations = [] 
shakes = []

def localsearch(instance,startpoint):
    best_order = None
    best_cost = 0
    has_better_order = True
    better_neigh_order = startpoint
    better_neigh_cost = instance.cost(better_neigh_order)
    while has_better_order:
        best_cost = better_neigh_cost
        best_order = better_neigh_order
        for  i in permutations:
            this_order = i(best_order)
            this_cost = instance.cost(this_order)
            if this_cost > better_neigh_cost:
                print "improve cost, from %d to %d" % (best_cost, this_cost)
                better_neigh_order = this_order
                better_neigh_cost = this_cost
                has_better_order = True
        else:
            has_better_order = False
    return {'cost': best_cost,'order':best_order}

def localsearch2(l):
    return localsearch(*l)

if len(sys.argv)!=2:
    sys.exit("precisa passar a instancia")
instance = instance(sys.argv[1],"bz2")

print dir(instance)

instance.load()

size = instance.size()

print "hipotetical cost: %d " % instance.hipotetical_cost()

for i in xrange(size -1):
    permutations.append(permutation(size,[i, i+1]))

pool = Pool()

curr_order = instance.becker_order()
    
minima = localsearch(instance, curr_order)

shakes = []
k= int(floor(size/4))
print "size: %d; k: %d; 4*k: %d" % (size, k, 4*k)
for s in range(k):
    p={}
    for i in range(k):
        s1 = (i+4*s)%k
        s3 = (2*k + (i+s)%k)
        s2 = (1*k + (i+2*s)%k)
        s4 = (3*k + (i+3*s)%k)
        
        p[i] = s3
        p[s3] = s2
        p[s2] = s4
        p[s4] = s1
        
    print p
    shakes.append(permutation(size,p))

shaked = []

print minima

for i in shakes:
    shaked.append(i(minima['order']))

print " ----- "
print shaked

pool_outputs = pool.map(localsearch2, izip(repeat(instance), shaked))
pool.close()
pool.join()

print pool_outputs

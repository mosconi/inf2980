from multiprocessing import Pool
from instance import instance
from permutation import permutation

#from itertools import izip, repeat

import sys, random

permutations = [] 
shakes = []

def localsearch(instance,startpoint):
    curr_order = startpoint
    curr_cost = instance.cost(curr_order)
    best_cost = curr_cost
    best_order = curr_order
    for p in permutations:
        new_order = p(curr_order)
        new_cost = instance.cost(new_order)
        if new_cost > curr_cost:
            print "applying %s: curr cost: %d new cost: %d" % (i, curr_cost, new_cost)
            instance.order(new_order)
            if new_cost > best_cost:
                best_cost = new_cost
                best_order = new_order
                best_changed = True
                break
            else:
                local_minima = True
    return {'cost': best_cost,'order':best_order}

def localsearch2(l):
    return localsearch(*l)

if len(sys.argv)!=2:
    sys.exit("precisa passar a instancia")
    instance = instance(sys.argv[1],"bz2")

print dir(instance)

instance.load()

size = instance.size()

for i in xrange(size -1):
    permutations.append(permutation(size,[i, i+1]))

pool = Pool()

curr_order = instance.becker_order()
    
minima = localsearch(instance, curr_order)

shakes = [permutation(size,[1,33,32,3,31]),
          permutation(size,random.sample(range(size),size/4))
    ]

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

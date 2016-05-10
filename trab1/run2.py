from multiprocessing import Pool
from instance import Instance
from permutation import Permutation
from math import floor

import sys, random, getopt

permutations = [] 
shakes = []

_debug=0

global _ls_runs
global _ils_runs

_ls_runs =0
_ils_runs =0


def localsearch(_instance,startpoint):
    global _ls_runs
    if _debug>0: print " ------"
    best_order = None
    best_cost = 0
    has_better_order = True
    better_neigh_order = startpoint
    startcost = _instance.cost(startpoint)
    better_neigh_cost = startcost
    while has_better_order:
        best_cost = better_neigh_cost
        best_order = better_neigh_order
        has_better_order = False
        _instance.order(best_order)
        for  i in permutations:
#           this_order = i(best_order)
            this_delta_cost = _instance.deltacost(i)
#           this_cost = _instance.cost(this_order)
            if this_delta_cost +best_cost > better_neigh_cost :
                better_neigh_order = i(best_order)
                better_neigh_cost = this_delta_cost + best_cost
                if _debug>0: print "LS improve cost to %d (+%d)" % (better_neigh_cost, this_delta_cost)
                has_better_order = True
        if not has_better_order:
            if _debug >0: print "no more improves on LS, cost (%d-> %d)" % (startcost,best_cost)
    _ls_runs+=1
    return {'cost': best_cost,'order':best_order}

def ils(_instance,_ils_startpoint,shakes):
    global _ils_runs
    _ils_best_order = None
    _ils_best_cost = 0
    _ils_has_better_order = True
    _ils_better_neigh_order = _ils_startpoint
    _ils_startcost = _instance.cost(_ils_startpoint)
    _ils_better_neigh_cost = _ils_startcost
    while _ils_has_better_order:
        _ils_best_cost = _ils_better_neigh_cost
        _ils_best_order = _ils_better_neigh_order
        _ils_has_better_order = False
        for shake in shakes:
            _ils_this_order = shake(_ils_best_order)
            _ils = localsearch(_instance,_ils_this_order)
            if _ils['cost'] > _ils_better_neigh_cost:
                if _debug>0: print "ILS improve cost, ( %d -> %d)" % (_ils_best_cost, _ils['cost'])
                _ils_better_neigh_order = _ils['order']
                _ils_better_neigh_cost = _ils['cost']
                _ils_has_better_order = True
        if not _ils_has_better_order:
            if _debug >0: print "no more improves on ILS, cost (%d -> %d)" % (_ils_startcost, _ils_best_cost)
        _ils_runs+=1
    return {'cost': _ils_best_cost,'order': _ils_best_order}
    

def localsearch2(l):
    return localsearch(*l)

opts, args  = getopt.getopt(sys.argv[1:],"d")
for o,a in opts:
    if o == "-d": _debug=1
    else:
        assert False, "opcao desconhecida"
        
for argv in sys.argv[1:]:
    _ls_runs=0
    _ils_runs=0

    print " ----- "
    print "instancia: %s" % argv    
    _instance = Instance(argv,"bz2")

    _instance.load()

    size = _instance.size()
    
    hcost = _instance.hipotetical_cost()

    for i in xrange(size -1): permutations.append(Permutation(size,[i, i+1]))
    shakes = []
    k= int(floor(size/4))
    if _debug>0: print "size: %d; k: %d; 4*k: %d" % (size, k, 4*k)
    for s in range(k):
        p ={}
        p1={}
        p2={}
        p3={}
        p4={}
        p1_2={}
        p1_3={}
        p1_4={}
        p2_3={}
        p2_4={}
        p3_4={}
        p5={}
        p6={}
        p7={}
        for i in range(k):
            s1 = (i+4*s)%k
            s3 = (2*k + (i+s)%k)
            s2 = (1*k + (i+2*s)%k)
            s4 = (3*k + (i+3*s)%k)
            p1[i] = s1
            p2[i+k] = s2
            p3[i+2*k] = s3
            p4[i+3*k] = s4
            p1_2[i]= s2
            p1_2[s2]= s1
            p1_3[i]= s3
            p1_3[s3]= s1
            p1_4[i]= s4
            p1_4[s4]= s1
            p2_3[i+k]= s3
            p2_3[s3]= s2
            p2_4[i+k]= s4
            p2_4[s4]= s2
            p3_4[i+k*2]= s4
            p3_4[s4]= s3
            p[i] = s3
            p[s3] = s2
            p[s2] = s4
            p[s4] = s1
        
        shakes.append(Permutation(size,p))
        shakes.append(Permutation(size,p1))
        shakes.append(Permutation(size,p2))
        shakes.append(Permutation(size,p3))
        shakes.append(Permutation(size,p4))    
        shakes.append(Permutation(size,p1_2))
        shakes.append(Permutation(size,p1_3))
        shakes.append(Permutation(size,p1_4))
        shakes.append(Permutation(size,p2_3))
        shakes.append(Permutation(size,p2_4))
        shakes.append(Permutation(size,p3_4))

    if _debug>0: print "----- \n\n"
    
    curr_order = _instance.becker_order()

    if _debug>0: print "first local search"
    _start = time.time()

    maxima = localsearch(_instance, curr_order)

    if _debug>0: print "creating shakes ..."


    if _debug>0: print "starting ILS"
    i_out = ils(_instance,maxima['order'],shakes)
    _stop = time.time()
    
    print "best: %s" % i_out
    print "LS/ILS: %d / %d" % (_ls_runs, _ils_runs)
    print "time: %f" % (_stop - _start)

    del(_instance)

else:
    sys.exit("precisa passar a instancia")

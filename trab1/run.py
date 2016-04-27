from instance import instance
from permutation import permutation
import sys

if len(sys.argv)!=2:
    sys.exit("precisa passar a instancia")
instance = instance(sys.argv[1],"bz2")

instance.load()

size = instance.size()

permutations = {}
for i in range(size-1):
    n= "( %04u %04u )" % (i,i+1)
    permutations[n]=permutation(size, [i, i+1])
    n= "( %04u %04u )" % (i,i+2)
    permutations[n]=permutation(size, [i, i+1])
    n= "( %04u %04u )" % (i,i+3)
    permutations[n]=permutation(size, [i, i+1])

#caso especial de swap consecutivo (wrap)
#n= "( %04u %04u )" % (size-1,0)
#permutations[n]=permutation(size, [size-1, 0])

id=permutation(size)
shakes1={}
for i in range(size/4):
    s = int(size/4)
    n= "( %04u %04u %04u %04u )" % (i, i+2*s, i+s, i+3*s)
    shakes1[n]=permutation(size,   [i, i+2*s, i+s, i+3*s])
    n= "( %04u %04u )( %04u %04u )" % (i, i+2*s, i+1,i+2*s+1)
    shakes1[n]=permutation(size,   {i:i+2*s, i+2*s:i, i+1:i+2*s+1,i+2*s+1:i+1})
#    n= "( %04u %04u %04u %04u )" % (i, i+3*s, i+2*s, i+s)
#    shakes1[n]=permutation(size,   [i, i+3*s, i+2*s, i+s])

hipotetical_cost = instance.hipotetical_cost()
print "hipotetical maximal: %d" % hipotetical_cost

best_order = instance.becker_order()
print "best_order: " + str(best_order)
instance.order(best_order)
best_cost = instance.cost(best_order)

print "initial cost: %d" % best_cost

best_changed = False
for s in ["id" ] + sorted(shakes1.keys()):
    if s != "id":
        print "shaking: %s" % s 
        shaked_order = shakes1[s](best_order)
        instance.order(shaked_order)

    print "starting LS cost: %d " % instance.cost() 
    local_minima = False
    while local_minima is False:
        
        curr_order = instance.order()
        curr_cost = instance.cost()
        if curr_cost == hipotetical_cost:
            print "got hipotetical_cost"
            local_minima = True
            break
        for i in sorted(permutations.keys()):
            new_order = permutations[i](curr_order)
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
                
    if  hipotetical_cost == instance.cost():
        break

print "best order: " + str(best_order)
print "best cost: %d" % best_cost


    

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
#caso especial de swap consecutivo (wrap)
n= "( %04u %04u )" % (size-1,0)
permutations[n]=permutation(size, [size-1, 0])

id=permutation(size)
shakes1={}
for i in range(size/2):
    n= "( %04u %04u )" % (i,i+size/2)
    shakes1[n]=permutation(size, [i, i+size/2])

hipotetical_cost = instance.hipotetical_cost()
print "hipotetical minimal: %d" % hipotetical_cost

best_order = instance.order()
best_cost = instance.cost() 

for s in ["id" ] + shakes1.keys() ++ shakes2.keys:
    if s != "id":
        print s
        shaked_order = shakes[s](instance.order())
        instance.order(shaked_order)
    local_minima = False
    while local_minima is False:
        curr_order = instance.order()
        curr_cost = instance.cost()
        if curr_cost == hipotetical_cost:
            print "got hipotetical_cost"
            local_minima = True
            break
        for i in permutations:
            new_order = permutations[i](curr_order)
            new_cost = instance.cost(new_order)
            if new_cost == 0:
                continue
            if new_cost < curr_cost:
                best_cost = new_cost
                best_order = new_order
                print "applying %s: new cost: %d" % (i, new_cost)
                instance.order(new_order)
                break
        else:
            local_minima = True
    if  hipotetical_cost == instance.cost():
        break

print "best order: " + str(instance.order())
print "best cost: %d" % instance.cost()    

print "cost: %d" % instance.cost([3,2,0,1]) 
print "cost: %d" % instance.cost([2,3,0,1]) 
print "cost: %d" % instance.cost([2,0,3,1]) 
print "cost: %d" % instance.cost([2,0,1,3]) 

    

from instance import instance
from permutation import permutation
import sys

if len(sys.argv)!=2:
    sys.exit("precisa passar a instancia")
instance = instance(sys.argv[1],"bz2")

instance.load()

size = instance.size()

permutations = []
for i in range(size-1):
    permutations.append(permutation(size, [i, i+1]))
#caso especial de swap consecutivo (wrap)
permutations.append(permutation(size, [0, size-1]))

print instance.order()
print instance.cost()

for i in range(len(permutations)):
    this_order = instance.order()
    new_order = permutations[i](this_order)
    print new_order
    print instance.cost(new_order)
    if i>5:
        break

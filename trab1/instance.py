

class instance:
    def __init__(self,filename,compressed=None):
        self.filename = filename
        self.compressed=compressed
        if self.compressed is not None:
            open_name = "_open_" + compressed
        else:
            open_name = "_open_plain"
        self.open=getattr(self,open_name)
        self._data=[]
        self._order=[]

    def load(self):
        self._file=self.open()
        sz_str = self._file.readline()
        self._size=int(sz_str)
        self._data = [ map(int,line.split()) for line in self._file ]
        self._file.close()
        self._order = [i for i in range(self._size)]
        num_elements = 0
        elements = []
        for i in range(self._size):
            for j in range(self._size):
                if i==j:
                    continue
                if self._data[i][j]>0:
                    num_elements +=1
                elements.append(self._data[i][j])
        elements.sort()
        if num_elements < self._size*(self._size-1)/2:
            self._hipotetical_cost = elements[0]
        else:
            k = num_elements - self._size*(self._size-1)/2
            self._hipotetical_cost = sum(elements[0:k])

    def hipotetical_cost(self):
        return self._hipotetical_cost

    def __getitem__(self,index):
        return self.data[index]

    def order(self,order=None):
        if order is None:
            return self._order
        self._order = order[:]

    def cost(self,order=None):
        if order is None:
            order=self._order

        if order.__class__.__name__ is 'permutation':
            return self._do_cost_permutation(dict)
        c = 0
        for i in range(1,self._size):
            o_i = order[i]
            for j in range(0,i+1):
                o_j = order[j]
                c = c + self._data[o_i][o_j]
        return c

    def _do_cost_permutation(self,perm):
        perm.collapse()
        if len(perm.permutation) == 2 :
            return self._do_cost_permutation_quick(perm)
        
        
    def _do_cost_permutation_quick(self,perm):
        k = perm.permutation.keys().sort()
        i = k[0]
        j = k[1]
        return self._data[i][j] - self._data[j][i] 

    def becker_order(self):
        order = []
        q={}
        for i in range(self._size):
            _upper=0
            _down=0
            for j in range(self._size):
                _upper = _upper + self._data[i][j]
                _down = _down + self._data[j][i]
            q[i] = (_upper+1)/(_down+1)
        while(len(q)>0):
            i_max = q.keys()[0]
            for i in range(len(q)):
                if i not in q.keys(): continue
                if q[i] > q[i_max]:
                    i_max=i
            order.append(i_max)
            del q[i_max]
        return order
                
    def size(self):
        return self._size
    
    def _open_plain(self):
        return open(self.filename, "rU")

    def _open_bz2(self):
        import bz2
        return bz2.BZ2File(self.filename, "rU")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

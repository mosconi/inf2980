

class Instance:
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
        s = 0
        for i in range(self._size):
            for j in range(self._size):
                if i==j:
                    self._data[i][j]=0
                if self._data[i][j]>0:
                    s = s+ self._data[i][j]
                    num_elements = num_elements +1
                elements.append(self._data[i][j])
        elements.sort()
        k = num_elements - self._size*(self._size-1)/2
        if k < 0:
            self._hipotetical_cost = s
        else:
            self._hipotetical_cost = sum(elements[k:])

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

        c = 0
        for i in range(self._size-1):
            o_i = order[i]
            for j in range(i+1,self._size):
                o_j = order[j]
                c = c + self._data[o_i][o_j]
        return c

    def deltacost(self,order):
        if order.__class__.__name__ is 'Permutation':
            return self._do_deltacost_permutation(order)
        
    def _do_deltacost_permutation(self,perm):
        perm.collapse()
        if len(perm.permutation) == 2 :
            return self._do_deltacost_permutation_quick(perm)
        
        
    def _do_deltacost_permutation_quick(self,perm):
        k = perm.permutation.keys()
        k.sort()
        i = k[0]
        j = k[1]
        oi=self._order[i]
        oj=self._order[j]
        return self._data[oj][oi] - self._data[oi][oj] 

    def becker_order(self):
        q={}
        for i in range(self._size):
            _upper=0
            _down=0
            for j in range(self._size):
                _upper = _upper + self._data[i][j]
                _down = _down + self._data[j][i]
            q[i] = (_upper+1)/(_down+1)
        order = sorted(q, key = q.get,reverse = True)
        return order
                
    def size(self):
        return self._size
    
    def _open_plain(self):
        return open(self.filename, "rU")

    def _open_bz2(self):
        import bz2
        return bz2.BZ2File(self.filename, "rU")

    def __getstate__(self):
        odict={}
        odict['_data'] = self._data
        odict['_order'] = self._order
        odict['_size'] = self._size
        return odict

    def __setstate__(self,dict):
        self.__dict__.update(dict)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

"""


"""

class permutation:
    def __init__(self,size,permutation=None,complete=False):
        """
        Cria um elemento de permutacao

        Argumentos: 
        size -- Informa
        rcycle -- 
        rcycle -- 
        """
        self.permutation={}
        self.maxsize=size
        if complete:
            self.permutation={ i:i for i in range(self.maxsize)}
      
        if permutation is not None:
            method_name = "_init_from_" + permutation.__class__.__name__
            method = getattr(self,method_name)
            self.permutation=method(permutation)

    def _init_from_list(self,_list):
        _l=_list[:]+[_list[0]]
        p={}
        for i in range(len(_list)):
            p[_l[i]]=_l[i+1]
        return p

    def _init_from_dict(self,_dict):
        p={}
        for k,v in _dict.iteritems():
            p[k]=v
        return p

    def __repr__(self):
        return "%s(%u,%s)" % (self.__class__,self.maxsize, self.permutation )
        
    def __getitem__(self, index):
        return self.permutation.get(index,index)

    def __call__(self,_other):
        method_name = "_do_" + _other.__class__.__name__
        method = getattr(self,method_name)
        return method(_other)

    def _do_list(self,_list):
        if len(_list) != self.maxsize:
            raise Exception("size mismatch")
        s=_list[:]
        for k,v in self.permutation.iteritems():
            s[v]=_list[k]
        return s

    def _do_permutation(self,_p):
        if _p.maxsize != self.maxsize:
            raise Exception("size mismatch")
        s=_p.permutation.copy()
        for k,v in self.permutation.iteritems():
            s[v]=_p[k]
        return permutation(self.maxsize,s)

    def collapse(self):
        for i in range(self.maxsize):
            if self.permutation[i]==i:
                del self.permutation[i]

    def expand(self):
        for i in range(self.maxsize):
            if i not in self.permutation:
                self.permutation[i]=i

    def __eq__(self,other):
        if self.maxsize != other.maxsize:
            return False
        return all([self[i]==other[i] for i in range(self.maxsize)])

if __name__ == '__main__':
  import doctest
  doctest.testmod()

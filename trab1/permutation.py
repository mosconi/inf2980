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
            method_name = "__init_from_" + type(permutation).__name__
            method = getattr(self,method_name)
            self.permutation=method(permutation)

    def __init_from_list(self,_list):
        l=_list+[_list[0]]
        p={}
        for i in range(len(_list)):
            p[_list[i]]=_list[i+1]
        return p

    def __init_from_dict(self,_dict):
        p={}
        for k,v in _dict.iteritems():
            p[k]=v
        return p

    def __repr__(self):
        return "%s(%u,%s)" % (self.__class__,self.maxsize, self.permutation )
        
    def __getitem__(self, index):
        return self.permutation.get(index,index)

    def __call__(self,_other):
        method_name = "_do_" + type(_other).__name__
        method = getattr(self,method_name)
        return method(_other)

    def __do_list(self,_list):
        s=_list[:]
        for k,v in self.permutation.iteritems():
            s[v]=_list[k]
        return s

    def __do_dict(self,_dict):
        d=_dict.copy()
        for k,v in self.permutation.iteritems():
            d[k]=_dict[v]
        return d

if __name__ == '__main__':
  import doctest
  doctest.testmod()



class Instance:
    def __init__(self,filename):
        self.filename = filename
        self.data=[]

    def load(self):
        f=open(self.filename,"rU")
        sz_str = f.readline()
        self.size=int(sz_str)
        self.data = [ map(int,line.split()) for line in f ]
    
    def __getitem__(self,index):
        return self.data[index]

    def size(self):
        return self.size


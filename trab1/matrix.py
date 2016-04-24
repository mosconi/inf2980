

class Instance:
    def __init__(self,filename):
        self.filename = filename
        self.data=[]

    def load(self):
        f=open(self.filename,"r")
        self.size=int(f.readline)
        self.data=[ map(int,line.split(',')) for line in f ]
    
    def __getitem__(self,index):
        return self.data[index]

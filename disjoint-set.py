class quickFind:
    _id = []
    _count = 0

    def __init__(self, N):
        self._id = list(range(0,N))
        self._count = N
    #Quick-find
    def find(self, p):
        return self._id[p]

    def union(self,p, q):
        self._pID = self.find(p)
        self._qID = self.find(q)
        if (self._pID == self._qID):
            return None

        for i in self._id:
            if (self._id[i] == self._qID):
                self._id[i] = self._pID
        self._count = self._count-1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
    def count(self):
        return self._count


class quickUnion:
    _id = []
    _count = 0

    def __init__(self, N):
        self._id = list(range(0,N))
        self._count = N
    
    #Quick-union
    def find(self, p):
        while (self._id[p] != p):
            p = self._id[p]
        return p

    def union(self, p, q):
        self._rootP = self.find(p)
        self._rootQ = self.find(q)

        if (self._rootP == self._rootQ):
            return None

        self._id[self._rootQ] = self._rootP

        self._count = self._count-1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
    def count(self):
        return self._count


class weightedQuickUnion:
    _id = []
    _sz = []
    _count = 0

    def __init__(self, N):
        self._id = list(range(0,N))
        self._count = N
        self._sz = [1]*N
        print(self._sz)
    
    #Quick-union
    def find(self, p):
        while (self._id[p] != p):
            p = self._id[p]
        return p

    def union(self, p, q):
        self._rootP = self.find(p)
        self._rootQ = self.find(q)

        if (self._rootP == self._rootQ):
            return None
        
        if (self._sz[self._rootP]<self._sz[self._rootQ]):
            self._id[self._rootP] = self._rootQ
            self._sz[self._rootQ] += self._sz[self._rootP]
        else:
            self._id[self._rootQ] = self._rootP
            self._sz[self._rootP] += self._sz[self._rootQ]

        self._count = self._count-1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
        
    def count(self):
        return self._count
        
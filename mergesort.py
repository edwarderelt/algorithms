class mergeSort:
    _aux = []
    
    def __init__(self):
        pass

    def sort(self, a):
        self._aux = [None]*len(a)
        self.__sort(a, 0, len(a)-1)
    
    def __sort(self, a, lo, hi):
        if (hi <= lo):
            return
        mid = lo + (hi - lo)//2
        self.__sort(a, lo, mid)
        self.__sort(a, mid+1, hi)
        self.__merge(a, lo, mid, hi)
        
    def __merge(self, a, lo, mid, hi):
        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self._aux[k] = a[k]

        for k in range(lo, hi+1):
            if (i > mid):
                a[k] = self._aux[j]
                j += 1
            elif (j > hi):
                a[k] = self._aux[i]
                i += 1
            elif (self._aux[j]<self._aux[i]):
                a[k] = self._aux[j]
                j += 1
            else:
                a[k] = self._aux[i]
                i += 1
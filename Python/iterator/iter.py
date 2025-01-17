class even():
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        else:
            if self.start %2 ==0 :
                num=self.start
                self.start+=1
                return num
            else:
                self.start+=1
                return self.__next__()
            


e =even(1,6)
for i in e:
    print(i)
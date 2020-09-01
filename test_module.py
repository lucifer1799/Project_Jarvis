class Person:
    def __init__(self,initialPos,ticketsToBuy):
        self.initialPos=initialPos
        self.ticketsToBuy=ticketsToBuy
        self.ticketsBought=0
        self.timespend=0

    def timeSpand(lst):
        m=max(lst)
        arr=[0]*(m+1)
        for i in lst:
            arr[i]+=1
        for j in range(1,m+1):
            arr[j]+=arr[j-1]
        print(arr)



lst=[1,2,3,4,5]
Person p
p.timeSpend(lst)

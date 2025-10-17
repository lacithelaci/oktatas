from keres import *

class Királynő(Feladat):
    def __init__(self,ke,c):
        super().__init__(ke,c)
        self.S=c-1 #8

    def célteszt(self, állapot):
        return állapot[self.S]==self.cél

    def rákövetkező(self, állapot):
        lépések=[] #list()
        s=állapot[self.S]
        for i in range(1,self.S+1):
            előfeltétel=True
            for m in range(1,állapot[self.S]):
                if állapot[m-1]!=i and abs(m-s)!=abs(i-állapot[m-1]):
                    előfeltétel=True
                else:
                    előfeltétel=False
                    break
            if előfeltétel:
                állapot_új=list(állapot)
                állapot_új[s-1]=i
                állapot_új[self.S]=állapot[self.S]+1
                állapot_új_2=tuple(állapot_új)
                lépések.append(('semmi',állapot_új_2))
        return lépések

    def __str__(self):
        str=''
        for i in self.kezdő[:self.S]:
            if i==0:
                str+='x  '*self.S+'\n'
            else:
                str+='x  '*(i-1)+'Q  '+'x  '*(self.S-i)+'\n'
        return str

q8=Királynő((0,0,0,0,0,0,0,0,1),9)
print(q8)
# while q8.célteszt(q8.kezdő)==False:
#     pot=q8.rákövetkező(q8.kezdő)
#     print(pot)
#     i=int(input('Adj egy számot:'))
#     lep=pot[i-1]
#     q8=Királynő(lep,9)
#     print(q8)

a=szélességi_fakeresés(q8)
print(a.út())
b=szélességi_gráfkeresés(q8)
c=mélységi_fakeresés(q8)
d=mélységi_gráfkeresés(q8)

print(Királynő(a.állapot,9))
print(Királynő(b.állapot,9))
print(Királynő(c.állapot,9))
print(Királynő(d.állapot,9))



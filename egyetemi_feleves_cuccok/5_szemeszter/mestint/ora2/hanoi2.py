from keres import *
from  collections import namedtuple


State = namedtuple('State',['korong','rud'])

class Hanoi(Feladat):
    def __init__(self,n):
        super().__init__('1'*n,'3'*n)

    # def célteszt(self, állapot):
    #     return állapot==self.cél

    def result(self,state:str,action:State): # '111' , 0 , '2'
        korong,rud=action  # 0 , '2'
        return state[0:korong] + rud + state[korong+1: ] #211



    def rákövetkező(self, állapot:str):
        lepesek=[]
        f1 = állapot.find('1') # melyik koron a legkisebb az 1-es rúdon
        f2 = állapot.find('2') #-1
        f3 = állapot.find('3')

        if f1 > -1 and (f1 < f2 or f2 == -1):
            tmp = self.result(állapot,State(f1,"2")) # '211'
            text = '{} korongot {} rúdra'.format(State(f1,"2").korong+1,State(f1,"2").rud)
            lepesek.append((text,tmp))


        if f1 > -1 and (f1 < f3 or f3 == -1):
            tmp = self.result(állapot,State(f1,"3")) # '311'
            text = '{} korongot {} rúdra'.format(State(f1,"3").korong+1,State(f1,"3").rud)
            lepesek.append((text,tmp))

        if f2 > -1 and (f2 < f3 or f3 == -1):
            tmp = self.result(állapot,State(f2,"3")) #
            text = '{} korongot {} rúdra'.format(State(f2,"3").korong+1,State(f2,"3").rud)
            lepesek.append((text,tmp))

        if f2 > -1 and (f2 < f1 or f1 == -1):
            tmp = self.result(állapot,State(f2,"1"))
            text = '{} korongot {} rúdra'.format(State(f2,"1").korong+1,State(f2,"1").rud)
            lepesek.append((text,tmp))

        if f3 > -1 and (f3 < f1 or f1 == -1):
            tmp = self.result(állapot,State(f3,"1"))
            text = '{} korongot {} rúdra'.format(State(f3,"1").korong+1,State(f3,"1").rud)
            lepesek.append((text,tmp))

        if f3 > -1 and (f3 < f2 or f2 == -1):
            tmp = self.result(állapot,State(f3,"2"))
            text = '{} korongot {} rúdra'.format(State(f3,"2").korong+1,State(f3,"2").rud)
            lepesek.append((text,tmp))

        return lepesek

K=Hanoi(8) # 2^n - 1

print(len(szélességi_gráfkeresés(K).megoldás()))







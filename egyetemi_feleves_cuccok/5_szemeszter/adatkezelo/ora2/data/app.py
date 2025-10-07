from http.client import CannotSendRequest

from ora2.data.basic.generator import generate_people
from ora2.data.basic.handler.csv_list import write_people
from ora2.data.basic.model_dataclasses import Person, Car, Airport
import pandas as pd

p1 = Person("001", "Name-001", 12,True)
p2 = Person("002", "Name-002", 14,True)
p3 = Person("003", "Name-003", 16,False)
p4_not_in_list = Person("004", "Name-004", 18, False)

person_list = [p1, p2, p3]


df1 = pd.DataFrame.from_records([p.__dict__ for p in person_list])
print(df1)

print()

r1 = Car('s','w',1999,True)
r2 = Car('s','w',1999,True)
r3 = Car('s','w',1999,True)
r4 = Car('s','w',1999,True)

car_list  = [r1, r2, r3]
df2 = pd.DataFrame.from_records([p.__dict__ for p in car_list])
print(df2)


r1 = Airport('a','b','c','d','e')
r2 = Airport('a','b','c','d','e')
r3 = Airport('a','b','c','d','e')
print()
airport_list  = [r1, r2, r3]
df3 = pd.DataFrame.from_records([p.__dict__ for p in airport_list])
print(df3)


print(generate_people(10))


write_people(generate_people(10),path='.')
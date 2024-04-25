"""
Ez a rész arról szól, hogyan hozhatunk létre és vizsgálhatunk meg kódokat,
amelyek elágazó (branching) utasításokat használnak.
Ilyenek lehetnek az if, elif, else utasítások, amelyek lehetővé teszik,
hogy a kód a feltételektől függően különböző ágakon fusson.
Emellett a "nested" (egymásba ágyazott) és "compound" (összetett) feltételes kifejezések is fontosak,
amikor összetett feltételeket kívánunk megadni a programban.
"""
# Egyszerű elágazás if-else segítségével
age = 20

if age >= 18:
    print("Ön már felnőtt.")
else:
    print("Ön még nem felnőtt.")

# Többszörös elágazás if-elif-else segítségével
grade = 85

if grade >= 90:
    print("Jeles")
elif grade >= 80:
    print("Jó")
elif grade >= 70:
    print("Közepes")
else:
    print("Elégtelen")

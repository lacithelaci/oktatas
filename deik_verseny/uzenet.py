s = ""
t = input()
while t != "":
    s += t[0]
    t = t[1:][::-1]
print(s[::-1])
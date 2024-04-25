a = "al*as*ma"
b = "alm*sam*"
c = ""
d = ""
for i in range(len(a)):
    d = ""
    if a[i] != "*":
        d = a[i]
    if b[i] != "*":
        d = b[i]
    c += d
print(c)

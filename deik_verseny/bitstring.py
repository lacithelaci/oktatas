a = input()
maximum = 0
indexek = []
masolando_sztring = None
for i in range(0, len(a)):
    if a[i] == "0":
        masolando_sztring = a[0:i] + "1" + a[i + 1:]
    if masolando_sztring != None:
        masolando_sztring = masolando_sztring.split("0")
        for y in masolando_sztring:
            if len(y) > maximum:
                maximum = len(y)
    masolando_sztring = None

print(maximum)

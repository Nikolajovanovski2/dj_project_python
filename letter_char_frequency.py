chars = []
with open('example.txt', 'r') as fileInput:
    for line in fileInput:
        for c in line:
            chars.append(c.upper())

d = {}
for i in chars:
    d[i] = d.get(i, 0) + 1
for k, v in sorted(d.items()):
    print("{}: {}".format(k, v))


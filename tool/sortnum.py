line = input()
charnumlist = line.split(",")
numlist = []
for num in charnumlist:
    a = int(num)
    numlist.append(a)

numlist.sort()
numlist.reverse()

for num in numlist:
    print(num, end="")


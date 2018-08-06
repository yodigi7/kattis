toPrint = int(input())
printers = 1
day = 1
while not printers >= toPrint:
    printers *= 2
    day += 1
print(day)
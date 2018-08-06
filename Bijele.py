import sys
kings, queens, rooks, bishops, knights, pawns = input().split()
print(str(1 - (int(kings))) + " " + str(1 - int(queens)) + " " + str(2 - int(rooks)) + " " + str(2 - int(bishops)) + " " + str(2 - int(knights)) + " " + str(8 - int(pawns)))

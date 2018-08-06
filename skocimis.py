kangaroos = input().split()
kangaroos = [int(x) for x in kangaroos]
print(max(kangaroos[1]-kangaroos[0], kangaroos[2]-kangaroos[1])-1)
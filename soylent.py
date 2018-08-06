cases = int(input())
for a in range(cases):
    caloriesPerDay = int(input())
    drinks = currCalories = 0
    while currCalories < caloriesPerDay:
        drinks += 1
        currCalories += 400
    print(drinks)
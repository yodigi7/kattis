monthDays = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}

days = {"1": "Thursday", "2": "Friday", "3": "Saturday", "4": "Sunday", "5": "Monday", "6": "Tuesday", "0": "Wednesday"}

day, month = input().split()
day, month = int(day), int(month)

for i in range(1,month):
    day += monthDays[str(i)]

print(days[str(day%7)])

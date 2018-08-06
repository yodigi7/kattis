try:
    while True:
        nums = input().split()
        nums = [float(x) for x in nums]
        print((abs(nums[0]-nums[2])**nums[4]+abs(nums[1]-nums[3])**nums[4])**(1/nums[4]))
except IndexError:
    pass
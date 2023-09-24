nums = [2,7,11,15]
target = 9


len_list = len(nums)
for num1 in range(len_list - 1):
    print(num1)
    for num2 in range(num1 + 1, len_list):
        print(num2)
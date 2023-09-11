num_list = [int(nums) for nums in input().split()]
counter = []

for nums in range(len(num_list)):
    print(num_list[nums])
    counter.append(num_list[nums])

print(counter)
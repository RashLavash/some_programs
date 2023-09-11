num1, num2 = (int(input()) for _ in range(2))
summ = 0
counter = 0

for nums in range(num1, num2 + 1):
    if nums % 3 == 0:
        summ += nums
        counter += 1
        
print(summ / counter)
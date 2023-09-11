num1, num2 = (int(input()) for _ in range(2))
noz = max(num1, num2)

while noz % num1 != 0 or noz % num2 != 0:
    noz += max(num1, num2)
    print(noz)

print(noz)
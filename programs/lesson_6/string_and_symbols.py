# userstring = input()
# counter = 0

# for symbols in range(len(userstring)):
#     print(symbols)
#     if 'g' in userstring[symbols].lower() or 'c' in userstring[symbols].lower():
#         counter += 1
        
# print((counter / len(userstring)) * 100)

user_string = input()
counter = 0


# for symbols_s in range(len(user_string) - 1):
#     if user_string[symbols_s] == user_string[symbols_s + 1]:
#         print(symbols_s)
#         counter += 1
#     elif user_string[symbols_s] != user_string[symbols_s + 1]:
#         print(user_string[symbols_s], counter,  sep='', end='')
#         counter = 1
# print(user_string[symbols_s], counter,  sep='', end='')    
for symbols_s in range(len(user_string) - 1):
    print(user_string[symbols_s], counter, sep='', end='')
    counter += 1
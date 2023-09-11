import json


# my_nums = [1, 2, 3, 4, 5]



# new_list = (x *2 for x in my_nums)
# print(new_list)

WORD_LIST = ('плов', 'курзе', 'омлет', 'каша гречневая')


# def word_filter(word):
#     return len(word) <= 5


# filtered_data = filter(word_filter, WORD_LIST)


# for elem in filtered_data:
#     print(elem)

# print(filtered_data)


# # map
# changed_data = map(lambda x: x[::-1], WORD_LIST)


# for elem in changed_data:
#     print(elem)
# print(changed_data)


# with open('text-file.txt', 'w', encoding='UTF-8') as my_file:
#     my_file.write('suetishko')

# student_score = {
#     'Магомед': 80,
#     'Мурад': 30
# }

# with open('json_file.json', 'w', encoding='UTF-8') as my_json:
#     json.dump(student_score, my_json, ensure_ascii=False, indent=2)


result = ', '.join(WORD_LIST)
print(result)
print(result.split())

my_word_list = list(WORD_LIST)
print(my_word_list)
print()
# my_word_list.sort(key=lambda x: len(x))
my_word_list.sort(key=lambda x: -len(x))
print(my_word_list)
my_word_list.sort(key=lambda x: (len(x), x[0]))
print(my_word_list)









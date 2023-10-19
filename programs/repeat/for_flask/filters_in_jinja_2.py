# Фильтры и макросы

from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300},
    {'model': 'Volkkswagen', 'price': 21300}
]
# Фильтр sum
# Конструкция : sum(итерируемый объект, attribute=итерируемый атрибут, start=число (в конце фильтрации сверху прибавит указанное число))
# tpl = "Суммарная цена автомобилей {{cars | sum(attribute='price')}}"
# tpl = "Суммарная цена автомобилей {{cars | max(attribute='price')}}" # max() - возвращает максимальное значение
# tpl = "Суммарная цена автомобилей {{cars | min(attribute='price')}}" # min() - возвращает минимальное значение
# tpl = "Суммарная цена автомобилей {{(cars | max(attribute='price')).model}}" # max() - такая форма возвращает значение по ключу
# tpl = "Случайное авто {{ (cars | random) }}" # random - возвращает случайное значение
# tpl = "Случайное авто {{ (cars | replace('o', 'O')) }}" # replace - заменяет одни элементы значений на другие


# tm = Template(tpl)
# message = tm.render(cars = cars)

# print(message)



persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5},
    {'name': 'Иван', 'old': 28, 'weight': 82.3},
    {'name': 'Николай', 'old': 33, 'weight': 94.0}
]
# блок {% filter %} ... {% endfilter %}
# Внутри блока for перебираем значение нашего списка
# и с помощью блока filter зададим филтр upper

# tpl = '''
# {% for user in users -%}
# {% filter upper %}{{user.name}}{% endfilter %}
# {% endfor -%}
# '''

# tm = Template(tpl)
# message = tm.render(users=persons)

# print(message)

# macro - макроопределение, нужно дял создание сразу нескольких полей с определенными значениями

# my_html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}", name="{{ name }}", value="{{ value | e }}", size=" {{ size }} ">
# {% endmacro %}

# <p>{{ input('username') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password') }}</p>

# '''
my_html = '''
{% macro list_users(list_of_user) -%}
<ul>
{%- for user in list_of_user %}
<li>{{ user.name }} {{caller(user)}}</li>
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
<ul>
    <li>user.age</li>
    <li>user.weight</li>
</ul>
{% endcall %}
'''
tm = Template(my_html)
message = tm.render(users=persons)
print(message)
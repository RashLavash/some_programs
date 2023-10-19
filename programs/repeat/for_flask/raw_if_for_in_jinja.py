from jinja2 import Template, pass_context


data = '''
Мое имя {{ name }}, запомни его.
'''


# {{ raw }} ... {{ endraw }} - raw нужен для того, чтобы блокировать работу шаблонов внутри этого блока

data = '''
{% raw %}Мое имя {{ name }}, запомни его.{% endraw %}
'''
tm = Template(data)
message = tm.render(name='Рашидбег')

# print(message)



# В этом случае записав текст в переменной link,
# в HTML тег <a> сработает именно как тег, отобразив текст внутри себя положенным образом.
# Чтобы строчка "<a href='#'>Ссылка</a>" в HTML документе отобразился текстом, 
# Используем экранизатор 'e' - escape. Используем его следуюзим образом:

link = '''
В HTML ссылки определяются так : <a href='#'>Ссылка</a>
'''
tm = Template("{{ link | e }}") # e - экранирование
msg = tm.render(link=link) # получившаяся белеверда отобразится в html документе так, как мы и хотели.

# print(msg)

cityes = [
    {'id': 1, 'city': 'Москва'},
    {'id': 5, 'city': 'Тверь'},
    {'id': 7, 'city': 'Минск'},
    {'id': 8, 'city': 'Смоленск'},
    {'id': 11, 'city': 'Калуга'},
]


# {% for ... in ... %} ... {% endfor %} - переборка элементов 
# {% if ... %} ... {% elif %} ... {% else %} ... {% endif %} - шаблон условия

# С помощью минуса перед знаком % убираем лишние переносы ( -% )
cityes_link = '''
<select name="cityes">
{% for city in cityes -%}
{% if city.id > 6 -%} 
    <option value="{{ city['id'] }}">{{ city['city'] }}</option>
{% elif city.city == 'Москва' -%}
    <option>{{ city['city'] }}</option>
{% else -%}
    <p>{{ city['city'] }}</p>
{% endif -%}
{% endfor -%}   
</select>
'''

tm = Template(cityes_link)
msg = tm.render(cityes = cityes)

print(msg)
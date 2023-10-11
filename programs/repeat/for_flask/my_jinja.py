from jinja2 import Template


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

pers = Person("Рашидбег", 19)
tm = Template("Привет {{ person.name }}, тебе {{person.age}} лет")
msg = tm.render(person = pers)

print(msg)
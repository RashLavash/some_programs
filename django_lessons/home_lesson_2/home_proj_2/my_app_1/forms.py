from django.forms import CharField, IntegerField
from django.forms import Form


class AddWorkerForm(Form):
    name = CharField(label='Имя', max_length=100)
    second_name = CharField(label='Фамилия', max_length=100)
    salary = IntegerField(label='Зарплата')



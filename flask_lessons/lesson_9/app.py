from flask import render_template, redirect, url_for

from models import User, Address
from forms import UserForm, AddressForm
from config import app, db



@app.route('/')
def index():

    users = User.query.all()

    # Обычный способ создания объекта записи пользователя с id адреса,
    # взятым из таблицы адресов через filter_by().
    # town = Address.query.filter_by(town_name='Махачкала').first()
    # user = User(user_name='Магомед', address_id=town.id)
    # print(user.user_name, user.address_id)

    # Добавим несколько записей в таблице Address.
    # town1 = Address(town_name='Каспийск')
    # town2 = Address(town_name='Дербент')
    # db.session.add(town1)
    # db.session.add(town2)
    # db.session.commit()
    # Добавим несколько записей в таблице User,
    # в качестве внешнего ключа address_id у которых
    # указан id созданной записи в таблице Address.
    # user1 = User(user_name='Гасей', address_id=2)
    # user2 = User(user_name='Сидредин', address_id=2)
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.commit()

    # В модель Address добавлено поле users типа relationship.
    # Теперь при желании мы можем получить у любого объекта таблицы Address
    # список всех объектов пользователей, которые указывают на объект Address
    # через поле users.
    address = Address.query.get(2)
    # Выведем всех пользователей, проживающих в городе address.
    for user in address.users:
        print(user.user_name)

    # Кроме того, посредством атрибута backref поля users в таблице Address
    # мы добавили таблице User дополнительный указатель user_address,
    # через который можно получить объект таблицы Address,
    # на который указывает внешний ключ записи в таблице User.
    # user2 = User.query.get(2)
    # Выведем название города, где проживает пользователь user2.
    # print(user2.user_address.town_name)

    # db.session.commit()
    return render_template('index.html', users=users)



@app.route('/users', methods=['GET', 'POST'])
def users():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user_name = user_form.user_name.data
        address = user_form.address.data

        users = User(user_name=user_name, address_id=address)

        db.session.add(users)
        db.session.commit()
    
    users = User.query.all()
    
    return render_template('users.html', form=user_form, users=users)

@app.route('/spec_users', methods=['GET', 'POST'])
def get_user():
    user_form = UserForm()

    user = db.session.execute(db.select(User).filter_by(user_name='Lavash')).scalar()
    
    return render_template('users.html', form=user_form, users=user)

@app.route('/towns', methods=['GET', 'POST'])
def get_towns():
    address_form = AddressForm()

    if address_form.validate_on_submit():
        town_name = address_form.town_name.data
        town = Address(town_name=town_name)
        db.session.add(town)
        db.session.commit()

    towns = Address.query.all()

    return render_template('towns.html', towns=towns, form=address_form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
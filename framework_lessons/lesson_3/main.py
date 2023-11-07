from flask import Flask
from flask import url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    params = {
        'name': 'qwerty',
        'surname': 'Lavash'
    }
    
    return render_template('home.html', params=params)


@app.route('/about')
def about():
    # staff = ['Maga', 'Rash', 'Sidredin']
    staff = ['Maga', 'Rash', 'Sidredin']

    return render_template('about.html', staff=staff)

@app.route('/product')
def products():
    product_list = ['Мясо', 'Молоко', 'Бананы']

    return render_template('products.html', product=product_list)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)

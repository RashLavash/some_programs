import sqlalchemy as db

engine = db.create_engine(
    'sqlite:///framework_lessons/sql_alchemy/db/products_sqlalchemy.db'
)

con = engine.connect()

metadata = db.MetaData()

products = db.Table('products', metadata, 
      db.Column('product_id', db.Integer, primary_key=True),                  
      db.Column('product_name', db.Text),
      db.Column('supplier_name', db.Text),
      db.Column('price_per_tonne', db.Integer)
)

metadata.create_all(engine)

insertion_query = products.insert().values([
    {"product_name": "bananas", "supplier_name": "United Bananas", "price_per_tonne": 7000},
    {"product_name": "avacado", "supplier_name": "United Avacados", "price_per_tonne": 12000},
    {"product_name": "tomatoes", "supplier_name": "United Tomatoes", "price_per_tonne": 7000}
])

# con.execute(insertion_query)
# con.commit()

# select_all_query = db.select(products)
# select_all_results = con.execute(select_all_query)

# print(select_all_results.fetchall())

# select_price_query = db.select(products).where(products.columns.price_per_tonne==12000)
# select_price_results = con.execute(select_price_query)

# print(select_price_results.fetchall()) 

# UPDATE

# update_query = db.update(products).where(products.columns.product_name=='bananas').values(product_name='apples')
# con.execute(update_query)

# select_all_query = db.select(products)
# select_all_results = con.execute(select_all_query)

# print(select_all_results.fetchall())

# DELETE

delete_query = db.delete(products).where(products.columns.product_name == 'bananas')
con.execute(delete_query)

select_all_query = db.select(products)
select_all_results = con.execute(select_all_query)

print(select_all_results.fetchall())


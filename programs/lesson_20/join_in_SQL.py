import sqlite3


con = sqlite3.connect('lesson_20/databases_with_join.db')
cursor = con.cursor()


cursor.executescript('''
CREATE TABLE IF NOT EXISTS cats(
    shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);
            
CREATE TABLE IF NOT EXISTS shops(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopname VARCHAR(100)
);
''')

query = ''' 
INSERT INTO cats(name) VALUES(?);
INSERT INTO shops(shopname) VALUES(?)
'''

query_list = [
    ('Vlas'),
    ('Nemo'),
]

query_list_2 = [
    ('Four Paws'),
    ('Mr.Zoo'),
]
cursor.executemany(query, query_list)

# cursor.execute('''
# SELECT name, shopname FROM cats JOIN shops ON shop_id = id
# ''')
print(cursor.fetchall())


con.commit()
cursor.close()
con.close()
import sqlite3
# connect to a db
conn = sqlite3.connect(database='customer.db')

# create a cursor
cursor = conn.cursor()

many_customers = [
    ('We', 'Brown', 'brown.co.cor'),
    ('Lorenz', 'Do', 'dokwon@gmail.com'),
    ('Louren', 'Peters', 'petersss@gmail.com'),
]
other_customers = [('Tomas', 'Vazqiez', 'vazquezt2018@gmail.com'),
                   ('Lorenzo', 'Gimenez', 'lolo@gmail.com')]
# create a table
cursor.execute(
    "SELECT * FROM customers"
)
items = cursor.fetchall()

# formated
for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()

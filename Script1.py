import sqlite3
from faker import Faker
from datetime import datetime

# Making a database
conn = sqlite3.connect('people.db')
c = conn.cursor()

# Creating table for names, email, age, city, province, and bio. 
c.execute('''CREATE TABLE IF NOT EXISTS people
             (id INTEGER PRIMARY KEY,
              first_name TEXT,
              last_name TEXT,
              email TEXT,
              age INTEGER,
              city TEXT,
              province TEXT,
              bio TEXT,
              created_at TEXT,
              updated_at TEXT)''')

# Creating a table with labels
faker = Faker()
for i in range(200):
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    age = faker.random_int(min=1, max=100)
    city = faker.city()
    province = faker.state()
    bio = faker.text()
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO people (first_name, last_name, email, age, city, province, bio, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (first_name, last_name, email, age, city, province, bio, created_at, updated_at))

conn.commit()
conn.close()

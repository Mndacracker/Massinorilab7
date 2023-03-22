import sqlite3
import pandas as pd
from datetime import datetime

# Creating database
conn = sqlite3.connect('people.db')
c = conn.cursor()

# Creating database for people over 50
c.execute("SELECT first_name, last_name, age FROM people WHERE age >= 50")

# Printing first and last name
results = c.fetchall()
for result in results:
    first_name, last_name, age = result
    print(f"{first_name} {last_name} is {age} years old.")

# Saving into a CSV file 
df = pd.DataFrame(results, columns=["First Name", "Last Name", "Age"])
filename = f"old_people_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
df.to_csv(filename, index=False)

# Data is finally closed
conn.close()

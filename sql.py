import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the table (if it doesn't exist already)
table_info = """
Create table if not exists STUDENT(
NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25),
MARKS INT
);
"""
cursor.execute(table_info)

# Insert 50 records with diverse data
records = [
    ('Nidhi', 'Data Science', 'A', 90),
    ('Nia', 'Data Science', 'B', 100),
    ('Tanya', 'Data Science', 'A', 86),
    ('Lakshay', 'DEVOPS', 'A', 50),
    ('Raghav', 'DEVOPS', 'A', 35),
    ('Amit', 'Web Development', 'B', 78),
    ('Sakshi', 'Machine Learning', 'C', 92),
    ('Riya', 'Data Science', 'B', 88),
    ('Karan', 'Web Development', 'A', 61),
    ('Megha', 'DEVOPS', 'C', 45),
    ('Ishaan', 'Machine Learning', 'A', 97),
    ('Priya', 'Web Development', 'B', 83),
    ('Sam', 'Data Science', 'C', 55),
    ('Anjali', 'DEVOPS', 'B', 72),
    ('Rohan', 'Machine Learning', 'C', 65),
    ('Sneha', 'Web Development', 'A', 74),
    ('Rahul', 'Data Science', 'B', 89),
    ('Neha', 'Machine Learning', 'C', 99),
    ('Vikram', 'DEVOPS', 'A', 40),
    ('Shreya', 'Data Science', 'C', 95),
    ('Ankit', 'Data Science', 'A', 81),
    ('Simran', 'DEVOPS', 'B', 60),
    ('Vivek', 'Web Development', 'C', 68),
    ('Pooja', 'Machine Learning', 'A', 78),
    ('Kavya', 'Data Science', 'B', 92),
    ('Mohit', 'DEVOPS', 'C', 59),
    ('Arjun', 'Web Development', 'A', 73),
    ('Alia', 'Machine Learning', 'B', 88),
    ('Manish', 'Data Science', 'A', 94),
    ('Dev', 'DEVOPS', 'C', 48),
    ('Tanvi', 'Web Development', 'B', 77),
    ('Zoya', 'Machine Learning', 'A', 91),
    ('Ritika', 'Data Science', 'C', 84),
    ('Nakul', 'DEVOPS', 'A', 43),
    ('Yash', 'Web Development', 'B', 76),
    ('Niharika', 'Machine Learning', 'C', 87),
    ('Siddharth', 'Data Science', 'A', 79),
    ('Aisha', 'DEVOPS', 'B', 54),
    ('Aditya', 'Web Development', 'A', 83),
    ('Bhavana', 'Machine Learning', 'C', 95),
    ('Mohan', 'Data Science', 'A', 60),
    ('Ritu', 'DEVOPS', 'C', 68),
    ('Suresh', 'Web Development', 'B', 70),
    ('Tina', 'Machine Learning', 'A', 85),
    ('Harsh', 'Data Science', 'C', 93),
    ('Kiran', 'DEVOPS', 'A', 52),
    ('Meera', 'Web Development', 'B', 67),
    ('Deepak', 'Machine Learning', 'C', 98)
]

# Insert the 50 records
cursor.executemany('''Insert Into STUDENT values (?, ?, ?, ?)''', records)

# Display all the records
print("The inserted records are:")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes into the database
connection.commit()
connection.close()

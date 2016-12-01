# 
import os
import sqlite3
import datetime

# Создание файла базы данных

db_filename = 'todo.db'
conn = sqlite3.connect(db_filename)
conn.close()


# Создание схемы
# Схема определяет таблицы в базе данных

os.remove(db_filename)
with sqlite3.connect(db_filename) as conn:
    conn.execute("""
        create table project (
            name        text primary key,
            description text,
            deadline    date
        );
        """)

    # Insert
    for i in range(10):
        conn.execute("""
            insert into project (name, description, deadline) VALUES (?,?,?)""", (
                'project %s'%i, 
                'project %s description'%i, 
                datetime.date.today()+datetime.timedelta(days=i**2)
            )
        )

with sqlite3.connect(db_filename) as conn:
    # Select
    # Объекты connection имеют атрибут row_factory, который позволяет вызывать
    # код, контролирующий тип объкта, создаваемого для каждой строки в запросе
    # Объекты Row дают доступ к данным по индексу и имени
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from project")
    for row in cur.fetchall():
        print(row)
        name, description, deadline = row
        print(name, description, deadline)

    # Update
    cur.execute("update project set deadline=:deadline where name=:name", 
        {'deadline': '2013-09-15', 'name': 'project 0'})












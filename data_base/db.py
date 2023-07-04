import random
import sqlite3

db = sqlite3.connect("bot.sqlite3")
cursor = db.cursor()


def sql_create():
    if db:
        print("База данных подключена!")

        db.execute("CREATE TABLE IF NOT EXISTS anketa "
                   "(namee VARCHAR (100) NOT NULL,"
                   "age INTEGER NOT NULL,"
                   "direction VARCHAR (100),"
                   "groupp VARCHAR(20))")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa "
                       "(namee, age, direction, groupp) "
                       "VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(users)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_all_ids():
    return cursor.execute("SELECT telegram_id FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()

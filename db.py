import sqlite3

database = sqlite3.connect("user_inf.db")
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user (
    username TEXT,
    phone TEXT,
    email TEXT,
    password TEXT
)""")

database.commit()


def sign_up(usernm, ph, mail, passw):
    nm = cursor.execute(f'SELECT username FROM user WHERE username = "{usernm}"').fetchone()
    ml = cursor.execute(f'SELECT email FROM user WHERE email = "{mail}"').fetchone()
    if nm != None:
        return 'Пользователь с таким именем сущесвует'
    elif ml != None:
        return 'Пользователь с таким email сущесвует'
    else:
        cursor.execute('INSERT INTO user(username, phone, email, password) VALUES (?, ?, ?, ?)',
                       (f'{usernm}', f'{ph}', f'{mail}', f'{passw}'))

        database.commit()
        return 'Успешная регистрация'


def log_in(usern, password):
    pas = cursor.execute(f'SELECT password FROM user WHERE username = "{usern}"').fetchone()
    if pas is None:
        return 'Пользователь с таким именем не найден'
    else:
        if str(pas[0]) == str(password):
            return 'Успешный вход!'
        else:
            return 'Неверный пароль'


if __name__ == '__main__':
    print(cursor.execute('SELECT * FROM user').fetchall())

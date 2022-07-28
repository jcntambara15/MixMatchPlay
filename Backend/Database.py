import requests
import sqlite3


def get_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print(str(db_file + ' file not found'))
        return None
    return conn

def get_playlists(user_id):
    conn = get_connection('database.db')
    cursor = conn.cursor()
    command = ("SELECT * FROM playlists WHERE user_id=?;")
    cursor.execute(command, (user_id,))
    rows = cursor.fetchall()
    # data = []
    # for row in rows:
    #     data.append(row)
    # return data

def create_tables():
    conn = get_connection('database.db')
    cursor = conn.cursor()
    users_command = ("CREATE TABLE IF NOT EXISTS users(" +
                "id integer primary key autoincrement," +
                "email text," +
                "password text);")
    playlist_command = ("CREATE TABLE IF NOT EXISTS playlists(" + 
                "id integer primary key autoincrement," +
                "user_id integer,"+
                "number_of_playlists integer ",+
                "playlist_id text," +
                "number_of_songs integer," +
                "date text);")
    get_playlist_command = ("CREATE TABLE IF NOT EXISTS playlist")

    cursor.execute(users_command)
    cursor.execute(playlist_command)
    conn.commit()


def insert_user(email, pswd):
    conn = get_connection('database.db')
    cursor = conn.cursor()
    command = ("INSERT INTO users(email, password)" +
                "VALUES(?, ?);")
    cursor.execute(command, (email, pswd))
    conn.commit()


def find_user(email, pswd):
    conn = get_connection('database.db')
    cursor = conn.cursor()
    command = ("SELECT * FROM users WHERE email=?;")
    cursor.execute(command, (email,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    row = rows[0]
    if row[1] == email and row[2] == pswd:
        return row[0]
    return False


def user_exists(email):
    conn = get_connection('database.db')
    cursor = conn.cursor()
    command = ("SELECT * FROM users WHERE email=?;")
    cursor.execute(command, (email,))
    if len(cursor.fetchall()) > 0:
        return True
    return False
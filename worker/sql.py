import pymysql

from config        import SQL_INFO
from worker.errors import NotFoundException


def create_connection(db_info = SQL_INFO):
    conn   = pymysql.connect(**db_info)
    cursor = conn.cursor()

    return conn, cursor


def close_connection():
    conn, _ = create_connection()
    conn.close()


def update_user_type(user_pk):
    conn, cursor = create_connection()

    query = f'UPDATE users SET type="graduated" WHERE id={user_pk}'
    cursor.execute(query)
    conn.commit()

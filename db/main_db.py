import sqlite3
from db import queries
from config import db_path


def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_GOODS)
    conn.commit()
    conn.close()


def add_goods(goods):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_GOODS, (goods,))
    conn.commit()
    goods_id = cursor.lastrowid
    conn.close()
    return goods_id


def get_goods(filter_type='all'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_GOODS_COMPLETED)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.SELECT_GOODS_UNCOMPLETED)
    else:
        cursor.execute(queries.SELECT_GOODS)

    goods = cursor.fetchall()
    conn.close()
    return goods 


def delete_goods(goods_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_GOODS, (goods_id,))
    conn.commit()
    conn.close()


def update_goods(goods_id, new_goods=None, completed=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if new_goods is not None and completed is not None:
        cursor.execute("UPDATE goods SET goods = ?, completed = ? WHERE id = ?", (new_goods, completed, goods_id))
    elif new_goods is not None:
        cursor.execute(queries.UPDATE_GOODS, (new_goods, goods_id))
    elif completed is not None:
        cursor.execute("UPDATE goods SET completed = ? WHERE id = ?", (completed, goods_id))

    conn.commit()
    conn.close()


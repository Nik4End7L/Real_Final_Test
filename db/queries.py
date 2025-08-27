CREATE_GOODS = """
    CREATE TABLE IF NOT EXISTS goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goods TEXT NOT NULL,
    completed INTEGER DEFAULT 0
    )
"""

INSERT_GOODS = "INSERT INTO goods (goods) VALUES (?)"

SELECT_GOODS = "SELECT id, goods, completed FROM goods"

SELECT_GOODS_COMPLETED = "SELECT id, goods, completed FROM goods WHERE completed = 1"
SELECT_GOODS_UNCOMPLETED = "SELECT id, goods, completed FROM goods WHERE completed = 0"

UPDATE_GOODS = "UPDATE goods SET goods = ? WHERE id = ?"

DELETE_GOODS = "DELETE FROM goods WHERE id = ?"

from sqlalchemy import create_engine, text
from sqlalchemy import inspect

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
engine = create_engine(db_connection_string)


# получить список таблиц
def test_db_connection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[2] == "company"


# получение строк из таблицы
def test_select():
    connection = engine.connect()
    result = connection.execute(text("select * from company"))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1['id'] == 2
    assert row1['name'] == "Автоматизация тестирования"
    connection.close()


# строка по одному фильтру
def test_select_1_row():
    connection = engine.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 51})
    rows = result.mappings().all()
    assert len(rows) == 1
    assert rows[0]["name"] == "Velo"


# поиск по двум фильтрам
def test_select_1_row_with_two_filters():
    connection = engine.connect()
    sql_statement = text("select * from company where \"is_active\" = :is_active and id > :id")
    rows = connection.execute(sql_statement, {"is_active": True, "id": 10}).fetchall()
    assert rows[0].id == 15


#  тот же метод, но с параметрами из словаря
def test_select_1_row_with_two_filters_2():
    connection = engine.connect()
    sql_statement = text("select * from company where \"is_active\" = :is_active and id > :id")
    params = {
        "is_active": True,
        "id": 10
    }
    rows = connection.execute(sql_statement, params).fetchall()
    assert rows[0].id == 15


# добавление компании
def test_insert():
    connection = engine.connect()
    transaction = connection.begin()
    sql = text("""INSERT INTO company ("name", "is_active", "create_timestamp", "change_timestamp")
VALUES (:new_name, true, now(), now())""")
    connection.execute(sql, {"new_name": "Velo2233"})
    transaction.commit()
    connection.close()


# изменение описания компании (description)
def test_update():
    connection = engine.connect()
    transaction = connection.begin()
    sql = text("update company set description = :descr where id = 56")
    connection.execute(sql, {"descr": 'ktm', "id": 56})
    transaction.commit()
    connection.close()


# удаление компании по номеру id
def test_delete_company():
    connection = engine.connect()
    transaction = connection.begin()
    sql = text("delete from company where id = :id_1")
    connection.execute(sql, {"id_1": 55})
    transaction.commit()
    connection.close()

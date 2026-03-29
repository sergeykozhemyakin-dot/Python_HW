from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


# проверка длинны списка компаний через api и через БД
def test_get_company_list():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)


# активные компании через API и через БД
def test_get_active_company():
    raw_list = api.get_company_list()
    full_list = [c for c in raw_list if c['is_active'] is True]
    db_list = db.get_active_companies()
    print(f"API (активные): {len(full_list)}")
    print(f"БД (активные): {len(db_list)}")
    assert len(full_list) == len(db_list)


# добавление новой компании
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1

    found = False
    for company in body:
        if company["name"] == name:
            found = True
            assert company["description"] == descr
            break

    assert found


def test_get_one_company():
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    new_company = api.get_company(max_id)
    db.delete(max_id)

    assert new_company["name"] == name
    assert new_company["is_active"] is True


def test_delete():
    # Добавили компанию через базу:
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    # Проверили по ID, что компании нет в базе:
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0


# Деактивация компании
def test_deactivate():

    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    body = api.set_active_state(new_id, False)
    assert body["is_active"] is False

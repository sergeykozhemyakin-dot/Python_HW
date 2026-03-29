from CompanyApi import CompanyApi

api = CompanyApi("http://5.101.50.27:8000")


def get_company_list():
    body = api.get_company_list()
    assert len(body) > 0


def test_get_active_company():
    full_list = api.get_company_list()
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    assert len(full_list) > len(filtered_list)


def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    name = "Autotest"
    descr = "Descr"
    api.create_company(name, descr)
    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr


def test_get_one_company():
    name = "VS Code"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]
    new_company = api.get_company(new_id)
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True


def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True

    body = api.get_company_list()
    len_before = len(body)

    api.delete_company(new_id)

    body = api.get_company_list()
    len_after = len(body)
    assert len_before - len_after == 1

    deleted = api.get_company(new_id)
    assert deleted['detail'] == 'Компания не найдена'

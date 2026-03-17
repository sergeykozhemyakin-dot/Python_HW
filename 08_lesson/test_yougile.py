import pytest
from YouGileApi import YouGileApi


@pytest.fixture(scope="session")
def api():
    obj = YouGileApi()
    obj.auth()
    return obj


def test_create_project_positive(api):
    resp = api.create_project("New Stable Project")
    assert resp.status_code == 201
    assert "id" in resp.json()


def test_create_project_negative_empty_title(api):
    resp = api.create_project("")  # Пустое название
    assert resp.status_code == 400


def test_get_project_positive(api):
    p_id = api.create_project("Find Me").json()["id"]
    resp = api.get_project(p_id)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Find Me"


def test_get_project_negative_wrong_id(api):
    resp = api.get_project("invalid-uuid-123")
    assert resp.status_code in [404, 400]


def test_update_project_positive(api):
    p_id = api.create_project("Before Update").json()["id"]
    resp = api.update_project(p_id, {"title": "After Update"})
    assert resp.status_code == 200

    info = api.get_project(p_id).json()
    assert info["title"] == "After Update"


def test_update_project_negative_not_found(api):
    resp = api.update_project("00000000-0000-0000-0000", {"title": "Fail"})
    assert resp.status_code == 404

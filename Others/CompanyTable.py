from sqlalchemy import create_engine, text


class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
        "select only active": text("SELECT * FROM company "
                                   "WHERE \"is_active\" = true  AND deleted_at IS NULL"),
        "delete by id": text("DELETE FROM company WHERE id =:id_to_delete"),
        "insert_new": text("""INSERT INTO company ("name", "is_active", "create_timestamp", "change_timestamp") 
        VALUES (:new_name, true, now(), now())"""),
        "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
        "select by id": text("SELECT * FROM company "
                             "WHERE id =:select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_active_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select only active"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete by id"],
            {"id_to_delete": id}
        )
        conn.commit()
        conn.close()

    def create(self, name):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {"new_name": name, "is_active": True, })
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def get_company_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select by id"],
            {"select_id": id}
        )
        company = result.mappings().all()
        conn.close()
        return company

    def set_active_state(self, id, is_active):
        client_token = self.get_token()

        url_with_token = f"{self.url}/company/status_update/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token,
                              json={"is_active": is_active})
        return resp.json()
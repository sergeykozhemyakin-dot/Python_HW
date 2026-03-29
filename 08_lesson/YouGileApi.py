import requests
import os
from dotenv import load_dotenv

load_dotenv()


class YouGileApi:

    def __init__(self, base_url='https://ru.yougile.com/api-v2/'):
        self.base_url = base_url
        self.login = os.getenv("YOUGILE_LOGIN")
        self.password = os.getenv("YOUGILE_PASSWORD")
        self.my_company_id = None
        self.api_key = None
        self.project_id = None
        self.headers = None

    def auth(self):
        auth_data = {"login": self.login, "password": self.password}
        resp = requests.post(f"{self.base_url}auth/companies", json=auth_data)
        resp.raise_for_status()
        company_id = resp.json()["content"][0]["id"]
        auth_data["companyId"] = company_id
        key_resp = requests.post(f"{self.base_url}auth/keys", json=auth_data)
        key_resp.raise_for_status()
        token = key_resp.json()["key"]
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        return requests.post(f"{self.base_url}projects", json={"title": title}, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base_url}projects/{project_id}", headers=self.headers)

    def update_project(self, project_id, payload):
        return requests.put(f"{self.base_url}projects/{project_id}", json=payload, headers=self.headers)

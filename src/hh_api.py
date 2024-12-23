import requests
from requests import Response

from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "page": 0, "only_with_salary": True}
        self.__vacancies = []

    def get_response(self, keyword, per_page, salary_rang) -> Response:
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        self.__params[""] = salary_rang
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
        return requests.get(self.__url, headers=self.__headers, params=self.__params)

    def get_vacancies(self, keyword: str, per_page: int, salary_rang: int):
        return self.get_response(keyword, per_page, salary_rang).json()["items"]

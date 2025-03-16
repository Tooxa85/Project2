from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""
    list_vacancies: list = []
    __slots__ = ("name", "alternate_url", "salary_from", "area_name", "requirement", "responsibility")

    def __init__(self, name: str = "не указан",
                 alternate_url: str = "не указан",
                 salary_from: str | None | dict = None,
                 area_name: str = "не указан",
                 requirement: str = "не указан",
                 responsibility: str = "не указан"
                 ):
        """Конструктор класса"""

        self.name: str = name
        self.alternate_url: str = alternate_url
        self.salary_from = self.__validate(salary_from)
        self.area_name: str = area_name
        self.requirement: str = requirement
        self.responsibility: str = responsibility

        dict_vacancy = {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
        self.list_vacancies.append(dict_vacancy)

    def __str__(self) -> str:
        """Строковое представление вакансии"""

        return (
            f"Наименование вакансии: {self.name}\n"
            f"Ссылка на вакансию: {self.alternate_url}\n"
            f"Зарплата: от {self.salary_from}\n"
            f"Место работы: {self.area_name}\n"
            f"Краткое описание: {self.requirement}\n"
            f"{self.responsibility}\n"
        )


    def validate(self) -> None:
        if not self.name or not self.alternate_url:
            raise ValueError("Название и ссылка на вакансию обязательны.")

    @staticmethod
    def __validate(salary_from):
        """Метод валидации зарплаты"""
        if salary_from is None:
            return {"from": 0, "to": 0}
        if isinstance(salary_from, str):
            try:
                from_salary, to_salary = map(int, salary_from.split(" - "))
                return {"from": from_salary, "to": to_salary}
            except ValueError:
                return {"from": 0, "to": 0}
        elif isinstance(salary_from, dict):
            from_salary = salary_from.get('from', 0)
            to_salary = salary_from.get('to', 0)
            return {"from": from_salary, "to": to_salary}
        else:
            return {"from": 0, "to": 0}


    def __ge__(self, other):
        """Метод сравнения вакансий по зарплате (верхний порог)"""
        self_salary_to = self.salary_from.get("to", 0)
        other_salary_to = other.salary_from.get("to", 0)
        return self_salary_to >= other_salary_to

    @classmethod
    def from_hh_dict(cls, vacancy_data: dict) -> Any:
        """Метод возвращает экземпляр класса в виде списка"""

        salary = vacancy_data.get("salary")

        cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
            vacancy_data["snippet"]["responsibility"],
        )
        return cls.list_vacancies

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.list_vacancies:
            if vacancies["salary"].get("from", 0) >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в виде словаря"""

        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }


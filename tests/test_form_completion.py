import os
import datetime

import pytest

from models.FormPage import FormPage
from conftest import browser
from utils import *

url = "https://demoqa.com/automation-practice-form"


@pytest.mark.smoke
def test_form_completion(browser):
    page = FormPage(browser)
    page.open(url=url)

    state_city = get_random_state_city_pair()

    data = [
        "Medet",
        "Malikov",
        "aaa@gmail.com",
        "Male",
        "7774533669",
        datetime.date(2000, 8, 4),
        get_random_subject(),
        get_random_hobby(),
        f"{os.getcwd()}\\files\\avatar1.jpg",
        "Lorem ipsum",
        state_city[0],
        state_city[1],
    ]

    page.complete_values(*data)
    result = page.collect_data()

    data_assertion(data, result)

@pytest.mark.smoke
def test_form_completion_two(browser):
    page = FormPage(browser)
    page.open(url=url)

    state_city = get_random_state_city_pair()

    data = [
        "Aidana",
        "Nurieva",
        "bbb@gmail.com",
        "Female",
        "7007007070",
        datetime.date(2000, 12, 2),
        get_random_subject(),
        get_random_hobby(),
        f"{os.getcwd()}\\files\\avatar2.png",
        "Lorem ipsum",
        state_city[0],
        state_city[1],
    ]

    page.complete_values(*data)
    result = page.collect_data()

    data_assertion(data, result)

@pytest.mark.xfail
def test_form_completion_fail(browser):
    page = FormPage(browser)
    page.open(url=url)

    state_city = get_random_state_city_pair()

    data = [
        "Medet",
        "Malikov",
        "aaa@gmail.com",
        "Male",
        "7774533",
        datetime.date(2000, 8, 4),
        get_random_subject(),
        get_random_hobby(),
        f"{os.getcwd()}\\files\\avatar3.jpg",
        "Lorem ipsum",
        state_city[0],
        state_city[1],
    ]

    page.complete_values(*data)
    result = page.collect_data()

    data_assertion(data, result)

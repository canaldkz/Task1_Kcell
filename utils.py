import datetime
import random


def get_random_subject():
    return random.choice([
        "Hindi",
        "English",
        "Maths",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Commerce",
        "Accounting",
        "Economics",
        "Arts",
        "Social Studies",
        "History",
        "Civics",
    ]) 

def get_random_state_city_pair():
    states = {
    "NCR": ["Delhi", "Gurgaon", "Noida"],
    "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
    "Haryana": ["Karnal", "Panipat"],
    "Rajasthan": ["Jaipur", "Jaiselmer"],
}
    state = random.choice(list(states.keys()))
    return (state, random.choice(states[state]))


def get_random_hobby():
    return random.choice(["Sports", "Reading", "Music"])


def data_assertion(data, result):
        assert f'{data[0]} {data[1]}' == result[0].text, 'Incorrect First name / Last name pair'
        assert data[2] == result[1].text, 'Incorrect Email'
        assert data[3] == result[2].text, 'Incorrect gender'
        assert data[4] == result[3].text, 'Incorrect phone number'
        assert datetime.datetime.strftime(data[5], '%d %B,%Y') == result[4].text, 'Incorrect date of birth'
        assert data[6] == result[5].text, 'Incorrect subject'
        assert data[7]  == result[6].text, 'Incorrect hobby'
        assert data[8].split('\\')[-1] == result[7].text, 'Incorrect file name'
        assert data[9] == result[8].text, 'Incorrect address'
        assert f'{data[10]} {data[11]}' == result[9].text, 'Incorrect State / City'
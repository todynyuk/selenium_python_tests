import random

from data.data import Person, Color
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_file():
    path=f"/Users/tarasodynyuk/PycharmProjects/web_tests/resource/text{random.randint(0, 999)}.txt"
    text_file = open(path, "w")
    text_file.write(f'Hello World{random.randint(0, 999)}')
    text_file.close()
    return text_file.name, path

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

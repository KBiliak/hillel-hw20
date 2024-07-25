animal_data = [
    ('Lion', 'yellow', '01-01-2000'),
    ('Eagle', 'grey', '05-12-2010'),
    ('Snake', 'red', '23-09-2015'),
]


class MyAnimal:
    def __init__(self, name, color, birth_date):
        self.name = name
        self.color = color
        self.birth_date = birth_date


def create_animals(raw_animals: list[tuple]) -> list[MyAnimal]:
    result = []
    for name, color, birth_date in raw_animals:
        result.append(MyAnimal(name, color, birth_date))
    return result


def print_animal_data(animals_list: list[MyAnimal]):
    for i in animals_list:
        print(f"Name: {i.name}, Color: {i.color} Birth :  {str(i.birth_date)}")


if __name__ == "__main__":
    animals = create_animals(animal_data)
    print_animal_data(animals)

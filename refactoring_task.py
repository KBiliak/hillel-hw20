animal_data = [
    ('Lion', 'yellow', '01-01-2000'),
    ('Eagle', 'grey', '05-12-2010'),
    ('Snake', 'red', '23-09-2015'),
]


class My_animal:
    def __init__(
            self, name, color, birth_date):
        self.name = name
        self.color = color
        # self.species = species
        self.birth_date = birth_date


def create_animals(
        animal_data: list = []
):
    animals = []
    for animal_tuple in animal_data:
        name = animal_tuple[0]
        color = animal_tuple[1]
        birth_date = animal_tuple[2]
        from datetime import datetime
        birth_date= datetime.strptime(birth_date, '%d-%m-%Y').date()
        animal = My_animal(name=name, color=color, birth_date=birth_date)
        animals.append(animal)
    return animals


def print_table_data(table_data):
    for i in table_data:
        print("Name: " + i.name + " Color: " + i.color + " Birth : " + str(i.birth_date))


if __name__ == "__main__":
    animals=create_animals(animal_data)
    print_table_data(animals)




import csv
from random import randint

EMAIL = ["maxi985049@gmail.com", "doskochynska83@gmail", "sapiy_mariya@gmail.com", "ubuntumaks@gmail.com",
         "wertyui@gmail.com", "uegydwisuhaijdf@gmail.com", "tdrfytguhuijilko@gmail.com", "hbrfnejidk@ukr.net",
         "dmbkiwi@yahoo.com", 'hoangle@hotmail.com',
         'msroth@mac.com', 'gastown@gmail.com', 'jschauma@live.com', 'pmint@aol.com', 'chlim@yahoo.ca',
         'boftx@sbcglobal.net', 'gregh@live.com', 'rafasgj@hotmail.com']

FULL_NAME = ["Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha", "Maksym", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna",
             "Khristina", "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha",
             "Mariya", "Denys", "Vlad", "Roman", "Sviatoslav", "Andriy", "Oleg", "Pavlo", "Taras", "Anna", "Khristina",
             "Olha"]


def generate_data():
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        for i in range(1000):
            request_data = []
            id = i + 1
            request_data.append(id)
            full_name = FULL_NAME[randint(0, len(FULL_NAME) - 1)]
            request_data.append(full_name)
            email = EMAIL[randint(0, 17)]
            request_data.append(email)
            password = 'none'
            request_data.append(password)
            writer.writerow(request_data)


generate_data()

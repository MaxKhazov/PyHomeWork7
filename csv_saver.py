
def surname_save(data):
    with open ('phonebook.csv', 'a') as file:
        file.write('Surname: {}\n'.format(data))

def name_save(data):
    with open ('phonebook.csv', 'a') as file:
        file.write('Name: {}\n'.format(data))

def number_save(data):
    with open ('phonebook.csv', 'a') as file:
        file.write('Number: {}\n'.format(data))

def discription_save(data):
    with open ('phonebook.csv', 'a') as file:
        file.write('Discription: {}\n\n'.format(data))

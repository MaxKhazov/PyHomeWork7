def get_surname():
    return input('Введите фамилию: ')

def get_name():
    return input('Введите имя: ')

def get_number():
    return input('Введите телефон: ')

def get_discription():
    return input('Введите описание контакта: ')

def data_collection():
    return(get_surname(), get_name(), get_number(), get_discription())

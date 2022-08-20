import data_collect as dc
import csv_saver as cs

def surname_view():
    data = dc.get_surname()
    cs.surname_save(data)
    return data 

def name_view():
    data = dc.get_name()
    cs.name_save(data)
    return data 

def number_view():
    data = dc.get_number()
    cs.number_save(data)
    return data 

def discription_view():
    data = dc.get_discription()
    cs.discription_save(data)
    return data 
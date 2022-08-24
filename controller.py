from main import Ui_MainWindow
import csv_saver as cs


def surname_view():
    data = Ui_MainWindow.get_surname()
    cs.surname_save(data)
    return data 

def name_view():
    data = Ui_MainWindow.get_name()
    cs.name_save(data)
    return data 

def number_view():
    data = Ui_MainWindow.get_number()
    cs.number_save(data)
    return data 

def discription_view():
    data = Ui_MainWindow.get_discription()
    cs.discription_save(data)
    return data 
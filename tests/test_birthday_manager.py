from lib.birthday_manager import *
from lib.birthday_object import *
from datetime import datetime

    
"""
create instance of birthday manager and add one birthday object
"""

def test_birthday_manager_init():
    birthday_manager = BirthdayManager()
    birthday_object = BirthdayObject('name', 'birthdate')

    birthday_manager.add_to_record(birthday_object) 
    print()
    assert len(birthday_manager.records) == 1



"""
update birthdate of a birthday object given a name

"""

def test_update_birthdate():

    birthday_manager = BirthdayManager()
    birthday_object = BirthdayObject('name', 'birthdate')

    birthday_manager.add_to_record(birthday_object) 
    birthday_manager.update_birthday('name', 'new_date')
    assert birthday_object.birthdate == 'new_date'



"""

update name of a birthday object given a name

"""
def test_update_name():

    birthday_manager = BirthdayManager()
    birthday_object = BirthdayObject('name', 'birthdate')

    birthday_manager.add_to_record(birthday_object) 
    birthday_manager.update_name('name', 'new_name')

    assert birthday_object.name == 'new_name'


"""
find birthdays coming up

"""
def test_birthdays_coming_up():

    birthday_manager = BirthdayManager()
    birthday_object = BirthdayObject('name', '1987-08-17')

    birthday_manager.add_to_record(birthday_object) 
    assert birthday_manager.birthday_coming_up() == [{'name', ''}]

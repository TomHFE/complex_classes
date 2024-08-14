# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

noun: record, names, birth date
verbs: keep; to add and store 

class => 


As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayManager:
    # User-facing properties:
    #   name: string

    def __init__(self, record):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet
        self.record = []

    def add_to_record(self, birthday_obj):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet
        self.record.append(birthday_obj)

    def update_birthday(self, name, new_date):
        for record in self.records:     
            if record.name == name:
                birthdate = new_date


    def update_name(self, name, new_name):
        for record in self.records:     
            if record.name == name:
                name = new_name

    def birthday_coming_up(self):
        curr_date = date.datetime.today()
        birthday_comping_up = []
        for record in self.records:     
            if record.date < curr_date.days + 11 and not record.date < curr_date.days:
                birthdays_coming_up.append(record)
        return birthdays_coming_up

    def calculate_age(self, name):
        upcoming_birthdays = birthday_coming_up()
        curr_date = date.datetime.today()
        age_appropriate_dict = {}
        for birthday in upcoming_birthdays:
            age = curr_date - birthday.birthdate
            age_appropriate_dict[name] = age
        return age_appropriate_dict



class BirthdayObject:
    # User-facing properties:
    #   name: string

    def __init__(self, name, birthday ):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet
        self.name = name
        self.birthdate = birthdate

    def access_birthday_object(self):
        birthday_object = {
            name = self.name,
            birthdate = self.birthdate
        }
        return birthday_object


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
create instance of birthday manager and add one birthday object
"""
birthday_manager = BirthdayManager()
birthday_object = BirthdayObject('name', 'birthdate')

birthday_manager.add_to_record(birthday_object) 
=> len(birthday_manager) == 1

"""
update birthdate of a birthday object given a name

"""

birthday_manager = BirthdayManager()
birthday_object = BirthdayObject('name', 'birthdate')

birthday_manager.add_to_record(birthday_object) 
birthday_manager.update_birthday('name', 'new_date')

=> birthday_manager.access info of 'name' == 'new_date'


"""
update name of a birthday object given a name

"""

birthday_manager = BirthdayManager()
birthday_object = BirthdayObject('name', 'birthdate')

birthday_manager.add_to_record(birthday_object) 
birthday_manager.update_name('name', 'new_name')

=> birthday_manager.access info of 'name' == 'new_name'


"""
find birthdays coming up

"""

birthday_manager = BirthdayManager()
birthday_object = BirthdayObject('name', 'birthdate')

birthday_manager.add_to_record(birthday_object) 
birthday_manager.birthday_coming_up()
=> access birthdays and return birthdays which are within the next 10 days
# => birthday_manager.access info of 'name' == 'new_name'
assert birthday_manager.birthday_coming_up() == birthday_object('name', 'birthdate')


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

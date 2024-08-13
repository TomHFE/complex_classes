from datetime import datetime, timedelta

class BirthdayManager:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        self.records = []

    def add_to_record(self, birthday_obj):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        self.records.append(birthday_obj)

    def update_birthday(self, name, new_date):
        for record in self.records:     
            if record.name == name:
                record.birthdate = new_date

    def update_name(self, name, new_name):
        for record in self.records:     
            if record.name == name:
                record.name = new_name

    def birthday_coming_up(self):
        curr_date = datetime.today().date()
        curr_date = curr_date + timedelta(days = 0)
        curr_date_plus_11 = curr_date + timedelta(days = 11)

        print(f'curr date  == {curr_date}')

        birthdays_coming_up = []
        for record in self.records:     
            formatted_date = datetime.strptime(record.birthdate, '%Y-%m-%d').date()
            print(f'record date  == {formatted_date}')
            if formatted_date < curr_date_plus_11:
                    print('true')
                    birthdays_coming_up.append(record)
        return birthdays_coming_up
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

        # (date_before_1970 - epoch).total_seconds()

        print(f'curr date  == {curr_date}')

        birthdays_coming_up = []
        for record in self.records:     
            birthday = datetime.strptime(record.birthdate, '%Y-%m-%d').date()
            birthday_if_curr_year = datetime.strptime(record.birthdate, '%Y-%m-%d').date().replace(year = curr_date.year)
            print(f'record date  == {birthday}')
            if birthday < curr_date_plus_11 and curr_date < birthday_if_curr_year:
                    print('true')
                    birthdays_coming_up.append({'name': record.name, 'birthday': record.birthdate})
        return birthdays_coming_up
    
    def birthday_age(self):
        birthday_list = self.birthday_coming_up()
        curr_date = datetime.today().date()
        birthday_ages = []
        for record in birthday_list:
            birthday = datetime.strptime(record['birthday'], '%Y-%m-%d').date()
            birthday_if_curr_year = datetime.strptime(record['birthday'], '%Y-%m-%d').date().replace(year = curr_date.year)
            curr_age = int((birthday_if_curr_year - birthday).days / 365.25)
            birthday_ages.append({'name': record['name'] , "age": curr_age})
            print(birthday_ages)
        return birthday_ages
            

    # today 1 2 3 4 5 6 7 8 9 10 
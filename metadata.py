from datetime import date

def get_current_date():
    print(type(date.today().year))
    print(date.today())

get_current_date()
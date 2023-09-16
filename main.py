from datetime import date
current_date = date.today()

from application.salary import calculate_salary #sal, w_day
from application.db.people import get_employees #last_name, first_name


if __name__ == '__main__':

    print(current_date, calculate_salary(500, 20))
    print(current_date, get_employees('Грибоедов', 'Зигмунд'))
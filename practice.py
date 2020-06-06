from datetime import datetime
from datetime import timedelta
import operator

my_dict = {}

a = int(input("No. of inputs: "))

for x in range(0, a):
    date = input("Enter the date in format(YYYY-mm-dd): ")
    try:
        datetime.strptime(date, format("%Y-%m-%d"))
        k = int(input("Enter the key: ")) #to get missing values keys also integer, we have to provide all even number keys (or difference between the keys must be greater than 1).
        my_dict[k] = date
    except:
        print("Dates must be given in format(YYYY-mm-dd).")

def daterange(date1, date2):
    for n in range(1, int((date2 - date1).days)):
        yield date1 + timedelta(n)

sorted_my_dict = sorted(my_dict.items(), key=operator.itemgetter(1))

for x in range(0, a):
    y = x + 1
    if y < a :
        starting_date = list(sorted_my_dict)[x]
        ending_date = list(sorted_my_dict)[y]
        starting_date_str = starting_date[1]
        ending_date_str = ending_date[1]
        starting_date_key = starting_date[0]
        ending_date_key = ending_date[0]
        datetime_std_object = datetime.strptime(starting_date_str, '%Y-%m-%d').date()
        datetime_end_object = datetime.strptime(ending_date_str, '%Y-%m-%d').date()
        number_of_days = (datetime_end_object - datetime_std_object).days
        missing_dates_key = (starting_date_key + ending_date_key)/2
        for dt in daterange(datetime_std_object, datetime_end_object):
            m_dates = str(dt.strftime('%Y-%m-%d'))
            my_dict[int(missing_dates_key)] = m_dates

print(my_dict)

new_sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))

print(new_sorted_dict)
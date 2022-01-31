from datetime import date
import time

# Generates current date
def generate_date():
    current_date = str(date.today())
    date_items = current_date.split('-')

    year, month, day = date_items[0], date_items[1], date_items[2]

    if month=='01':
        month = 'January'
    elif month=='02':
        month = 'February'
    elif month=='03':
        month = 'March'
    elif month=='04':
        month = 'April'
    elif month=='05':
        month = 'May'
    elif month=='06':
        month = 'June'
    elif month=='07':
        month = 'July'
    elif month=='08':
        month = 'August'
    elif month=='09':
        month = 'September'
    elif month=='10':
        month = 'October'
    elif month=='11':
        month = 'November'
    elif month=='12':
        month = 'December'

    return(f"Today is {month} {day}, {year}.")

# Generates current time
def generate_time():
    current_time = time.localtime()
    current_time_f = time.strftime("%H:%M:%S", current_time)
    return current_time_f
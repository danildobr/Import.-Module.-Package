import datetime

def get_employees():
    print(f'запустился модуль с именем- {__name__}')
    
def data_time():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.replace(microsecond=0)
    print(f'Текущая дата и время: {formatted_datetime}')
    
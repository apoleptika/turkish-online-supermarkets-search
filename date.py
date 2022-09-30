from  datetime import datetime

today = datetime.today().__str__()
# today = datetime.today().date().__str__()
print(today)
date = datetime.strftime(today, '%d.%m.%Y hh:mm')
# date = datetime.strptime(datetime.today().date().__str__(), '%d.%m.%Y')
# print(date)

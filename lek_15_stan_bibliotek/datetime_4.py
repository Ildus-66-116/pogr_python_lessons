from datetime import datetime, timedelta

date_1 = datetime(1979, 7, 4)
date_2 = datetime(2024, 6, 21)
delta = date_2 - date_1
print(f'{delta = }\t-\t{delta}')

birthday = datetime(1503, 12, 14)
dlt = timedelta(days=365.25 * 33)
new_date = birthday + dlt
print(f'{new_date = }\t-\t{new_date}')

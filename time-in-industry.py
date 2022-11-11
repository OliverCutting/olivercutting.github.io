import datetime

start_date = datetime.datetime(2022,1,4)
end_date = datetime.datetime.now()

time_in_industry = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

print(time_in_industry)
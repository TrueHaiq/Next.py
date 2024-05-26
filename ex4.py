def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for min in range(60):
        yield min

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield f"{hour:02d}:{min:02d}:{sec:02d}"

def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    total_days = 30
    if month in {1, 3, 5, 7, 8, 10, 12}:
        total_days = 31
    elif month == 2:
        if leap_year: total_days = 29
        else: total_days = 28

    for day in range(total_days):
        yield day+1

def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        for month in gen_months():
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for sec in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{sec:02d}"

date_generator = gen_date()
i = 0
while(True):
    date = next(date_generator)
    if(i%1000000 == 0): print(date)
    i += 1
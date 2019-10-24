def _is_leap(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

year_leap_bool = _is_leap

print(year_leap_bool(800))

print(id(year_leap_bool))
print(id(_is_leap))

print(type(year_leap_bool))
print(type(_is_leap))
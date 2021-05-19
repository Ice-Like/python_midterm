list1=['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
year = int(input(''))
if year < 2008:
    y = (12-(2008-year)%12)%12
    print(list1[y])
else:
    y = (year-2008)%12
    print(list1[y])
def y_date(day, month, year):
    i=1
    last_day=[31,28,31,30,31,30,31,31,30,31,30,31]
    if day==1:
        if month==1:
            month=12
            day=31
            year=year-1
        else:
            while i!=month:
                i=i+1
            print(i)
            if (i==3) and (year%4==0):
                    last_day[i]=last_day[i-2]+1
                    day=last_day[i]
            else:
                day=last_day[i-2]
            month=month-1
    else:
        day=day-1
    return day, month, year
 
def n_date(day, month, year):
    i=1
    next_day=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (day==31) and (month==12):
        year=year+1
        day=1
        month=1
    else:
        while i!=month:
            i=i+1
        if (i==2) and (year%4==0) and (day==28) :
                next_day[i]=next_day[i-1]+1
                day=next_day[i]
        else:
            if day==next_day[i-1] or (i==2) and (day==29):
                month=month+1
                day=1
            else:
                day=day+1
        return day, month, year
(day, month, year) = [int(i) for i in input().split()]

print(y_date(day, month, year))
print(n_date(day, month, year))
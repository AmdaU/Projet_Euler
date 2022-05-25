months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nombre = 0

#premier samedi du sciècle
day = 6
month = 1
year = 1901

while(year < 2001):
    day += 7
    if(day > months[month-1]):
        day -=months[month-1]
        month +=1
        if(month > 12):
            month = 1
            year += 1
            if(year % 4 == 0):
                months[1] = 29
            else:
                months[1] = 28
    if(day == 1):
        nombre += 1

print(nombre)

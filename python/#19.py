months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

nombre = 0

# premier samedi du sciècle
day, month, year = 6, 1, 1901

while (year < 2001):
    new_m = ((day := day+7) > months[month-1])
    day -= months[(month := month + new_m) - 1 - new_m]*new_m
    months[1] = 28 + 1 * ((year := year + (month > 12)) % 4 == 0)
    month = (month-1) % 12 + 1
    nombre += day == 1

print(nombre)

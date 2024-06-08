# The task is to create dict with key = country, value = cities
# you will get n strings like this "Германия Берлин Мюнхен Гамбург Дортмунд",
# then m cities on different lines
# you need to search for cities in values and print key (country), if find city in values


dct = {}
for i in range(int(input())):               # creating dict
    el = str(input()).split(" ")
    dct[el[0]] = el[1:]

for i in range(int(input())):               # reading cities and printing countries
    city = str(input())
    for key, value in dct.items():          # searching for city in values
        if city in value:
            print(key)

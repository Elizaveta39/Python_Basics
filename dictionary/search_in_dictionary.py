# The task is to create a dictionary with n items,
# then read m words (keys) and print their values

dct = {}
for i in range(int(input())):               # creating dict
    el = str(input()).split(": ")
    dct[el[0].lower()] = el[1]

for i in range(int(input())):               # reading and printing values
    word = str(input().lower())
    print(dct.get(word, "Не найдено"))
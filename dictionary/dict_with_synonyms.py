# The task is to create a dictionary with n pairs of synonyms,
# then read word and print its synonym

dct = {}
for i in range(int(input())):                   # creating dict
    key, value = str(input()).split(" ")
    dct[key] = value

word = str(input())

for key, value in dct.items():                  # searching for word in keys and values
    if word == key:
        print(dct[key])
    elif word == value:
        print(key)
# The task is to print the least frequent word in text
# if you have > 1 least frequent word -> print the shortest one

text = str(input())
symbols = ".,!?:;-"

for el in symbols:                          # getting rid of symbols in text
    text = text.replace(el, "")

list_txt = text.lower().split()             # bringing text to low case and convert it into list of words

doubles = {}                                # counting words and put it into dict
for el in list_txt:
    doubles[el] = doubles.get(el, 0) + 1

minims = []

for key, value in doubles.items():          # create list with the least frequent keys
    if value == min(doubles.values()):
        minims.append(key)

print(min(minims))

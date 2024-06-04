# The task is to find and print word that is the most frequent in s string
# if there are few of them you need to print the smallest one (shortest)

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
    'barley '

my_list = s.split(" ")[:-1]                 # create list with words without " "

doubles = {}

for el in my_list:
    doubles[el] = doubles.get(el, 0) + 1    # create dict with key = word, value = quantity of word in string

maxims = []

for key, value in doubles.items():          # create list with most frequent keys
    if value == max(doubles.values()):
        maxims.append(key)

print(min(maxims))                          # print the shortest key


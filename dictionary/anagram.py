# The task is to read 2 texts and decide if it is anagram or not

dct1, dct2 = {}, {}

for c in input():                               # creating dict with quantity of every el in word 1
    if c not in '.,!?:;- ':                     # or if c.isalpha()
        dct1[c.lower()] = dct1.get(c, 0) + 1

for c in input():                               # creating dict with quantity of every el in word 2
    if c not in '.,!?:;- ':                     # or if c.isalpha()
        dct2[c.lower()] = dct2.get(c, 0) + 1

print('YES' if dct1 == dct2 else 'NO')          # compare and print result

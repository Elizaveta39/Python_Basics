# The task is to create dictionary with all letters from text as keys and
# number of their doubles as values

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for el in text:
    result[el] = result.get(el, 0) + 1

print(result)
# The task is to get string of IDs, find duplicates and number them

text = str(input()).split(" ")                                  # get string and create list of IDs


result = []
double_count = {}

for el in text:
    double_count[el] = double_count.setdefault(el, -1) + 1      # calculate quantity of every ID

    if el not in result:
        result.append(el)                                       # add uniq ID into final list
    elif el in result:
        result.append(el + "_" + str(double_count.get(el)))     # number and add duplicate to final list

print(*result)

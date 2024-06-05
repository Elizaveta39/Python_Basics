# The task is to create a dictionary with pets owners data as a key and pets names as value
# if owner has > 1 pet, you need to add to value all his pets names

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]


result = {}

#for pet in pets:                                                      # without i and range()
    #owners = pet[1:]
    #print(owners)
    #pet_name = pet[0]
    #print(pet_name)
    #result[owners] = result.get(owners, []) + [pet_name]


for i in range(len(pets)):                                              # with i and range()
    result[pets[i][1:]] = result.get(pets[i][1:], []) + [pets[i][0]]    # we use + not append(),
# bacause he append() method adds an element to the end of an existing list but returns None. Therefore, it can't be
# used in the context of dictionary value assignment. On the other hand, the + operator concatenates two lists to
# create a new list. In this case, we create a new list consisting of the current pet list and the new pet name,
# then assign this new list as the dictionary value. So, instead of modifying the original list (as append() does),
# we create a new list and assign it as the dictionary value using +.

print(result)

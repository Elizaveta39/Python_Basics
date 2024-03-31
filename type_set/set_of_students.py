# The task is to find students that attend to all lessons
# you will get m - number of lessons,
# then m sets of n (number of students on a lesson) and n names of students on the lesson
# you need to print the result on different strings and in alphabetical order

m = int(input())  # number of lessons

mylist = []     # creating empty list

for i in range(m):  # adding to list sets of n students
    n = int(input())  # number of pupils on a lesson
    mylist.append({input() for el in range(n)}) # set of n students

result = mylist[0]  # defining first set

for el in mylist[1:]:   # finding intersection of m sets
    result &= el

print(*sorted(result), sep='\n')    # printing the result

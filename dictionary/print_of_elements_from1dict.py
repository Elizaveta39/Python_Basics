# This script is another way of solving task from file "print_of_elements_with_f-string.py"

my_dict = {
    'CS101': ('3004', 'Хайнс', '8:00'),
    'CS102': ('4501', 'Альварадо', '9:00'),
    'CS103': ('6755', 'Рич', '10:00'),
    'NT110': ('1244', 'Берк', '11:00'),
    'CM241': ('1411', 'Ли', '13:00'),
}

course_number = input()
audience, teacher, time = my_dict[course_number]
print(f'{course_number}: {audience}, {teacher}, {time}')
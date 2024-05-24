courses = [{'course': 'CS101', 'room': '3004', 'teacher': 'Хайнс', "time": "8:00"},
         {'course': 'CS102', 'room': '4501', 'teacher': 'Альварадо', "time": "9:00"},
         {'course': 'CS103', 'room': '6755', 'teacher': 'Рич', "time": "10:00"},
         {'course': 'NT110', 'room': '1244', 'teacher': 'Берк', "time": "11:00"},
         {'course': 'CM241', 'room': '1411', 'teacher': 'Ли', "time": "13:00"}]

c_num = str(input())

for el in courses:
    if el["course"] == c_num:
        print(f"{c_num}: {el['room']}, {el['teacher']}, {el['time']}")
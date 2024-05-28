# The task is to get text and print what numbers and how many times of each number user
# should press given the fact that we type on Nokia 3310

nokia = {                               # dictionary with numbers - keys and symbols - values
    '1': [".", ",", "?", "!", ":"],
    '2': ["A", "B", "C"],
    '3': ["D", "E", "F"],
    '4': ["G", "H", "I"],
    '5': ["J", "K", "L"],
    '6': ["M", "N", "O"],
    '7': ["P", "Q", "R", "S"],
    '8': ["T", "U", "V"],
    '9': ["W", "X", "Y", "Z"],
    '0': [" "]
}

my_text = []
my_text.extend(str(input().upper()))    # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D', '!']

for el in my_text:                      # taking 1 symbol from input
    for key, values in nokia.items():   # looking for match in values of the dictionary
        if el in values:
            print(key * (values.index(el) + 1), end="")
# The task is to find total number of different words in a string
# you will not need punctuation from the string (try to remove it)

text = str(input()).lower()  # reading the string

# removing punctuation
for el in text:
    if el in [".", ",", ";", ":", "-", "?", "!"]:
        text = text.replace(el, "")

# printing result
print(len(set(text.split())))

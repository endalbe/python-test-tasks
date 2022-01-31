i = 0

percent = input("Please enter percent: ")

while i <= int(percent):
    value = i % 100
    number = value % 10
    text = ''

    if number > 1 and number < 5:
        text = '%\tпроцента'

    if number == 1:
        text = '%\tпроцент'

    if value > 10 and value < 20 or number >= 5 or number == 0:
        text = '%\tпроценов'

    print(i, text)

    i += 1

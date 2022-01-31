number = 1
result = 0

while number <= 1000:
    number = number + 1

    if number % 2 != 0:
        cube_number = number ** 3
        current_number = cube_number
        sum_of_number = 0

        while current_number > 0:
            sum_of_number = sum_of_number + current_number % 10
            current_number = int(current_number / 10)

        if sum_of_number % 7 == 0:
            result = result + number
            print('Result:', result, '\t | Decimal number: ',
                  number, '| Cube of number:', cube_number)

#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        number = []
        for i in roman_string:
            if i == 'I':
                number.append(1)
            elif i == 'V':
                number.append(5)
            elif i == 'X':
                number.append(10)
            elif i == 'L':
                number.append(50)
            elif i == 'C':
                number.append(100)
            elif i == 'D':
                number.append(500)
            elif i == 'M':
                number.append(1000)
        for i in range(len(number)):
            if i != len(number) - 1:
                if number[i] < number[i + 1]:
                    number[i] = -number[i]
        return sum(number)
    else:
        return 0
